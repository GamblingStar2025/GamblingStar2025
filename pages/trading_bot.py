import numpy as np
import pandas as pd
import streamlit as st


st.set_page_config(page_title="📈 Trading Bot Lab", layout="wide")
st.title("📈 Trading Bot Lab – Aktien, ETF & Krypto")
st.caption("Fokus: Tagestrading, Candlestick-Systeme, Marktanalyse und Strategie-Ideen.")

st.markdown(
    """
Mit dieser Seite kannst du schnell prüfen, ob ein Markt eher **Trend**, **Range** oder **hohe Volatilität** zeigt.
Zusätzlich erhältst du Signale für ein einfaches **EMA + RSI**-System sowie eine kompakte
**Candlestick-Muster-Erkennung**.
"""
)

with st.expander("📥 CSV-Format (OHLCV)", expanded=False):
    st.code(
        """Date,Open,High,Low,Close,Volume
2026-04-01,100.2,101.5,99.8,101.0,1523000
2026-04-02,101.0,102.8,100.6,102.2,1830000
...""",
        language="text",
    )

uploaded = st.file_uploader("Lade Kursdaten hoch (CSV)", type=["csv"])


def _normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    mapping = {c.lower().strip(): c for c in df.columns}

    candidates = {
        "date": ["date", "datetime", "timestamp", "time"],
        "open": ["open", "o"],
        "high": ["high", "h"],
        "low": ["low", "l"],
        "close": ["close", "c", "adj close", "adj_close"],
        "volume": ["volume", "vol", "v"],
    }

    selected = {}
    for target, aliases in candidates.items():
        for alias in aliases:
            if alias in mapping:
                selected[target] = mapping[alias]
                break

    required = ["date", "open", "high", "low", "close"]
    missing = [col for col in required if col not in selected]
    if missing:
        raise ValueError(
            f"Fehlende Spalten: {', '.join(missing)}. Benötigt: Date/Open/High/Low/Close"
        )

    normalized = df.rename(columns={v: k for k, v in selected.items()})
    return normalized[[c for c in ["date", "open", "high", "low", "close", "volume"] if c in normalized.columns]]


def _calculate_signals(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out["ema_fast"] = out["close"].ewm(span=9, adjust=False).mean()
    out["ema_slow"] = out["close"].ewm(span=21, adjust=False).mean()

    delta = out["close"].diff()
    gain = np.where(delta > 0, delta, 0)
    loss = np.where(delta < 0, -delta, 0)
    avg_gain = pd.Series(gain, index=out.index).rolling(14).mean()
    avg_loss = pd.Series(loss, index=out.index).rolling(14).mean()
    rs = avg_gain / avg_loss.replace(0, np.nan)
    out["rsi"] = 100 - (100 / (1 + rs))

    out["signal"] = "NEUTRAL"
    long_mask = (out["ema_fast"] > out["ema_slow"]) & (out["rsi"] > 52)
    short_mask = (out["ema_fast"] < out["ema_slow"]) & (out["rsi"] < 48)
    out.loc[long_mask, "signal"] = "LONG-BIAS"
    out.loc[short_mask, "signal"] = "SHORT-BIAS"

    out["returns"] = out["close"].pct_change()
    out["volatility_20"] = out["returns"].rolling(20).std() * np.sqrt(20)
    out["trend_strength"] = (out["ema_fast"] - out["ema_slow"]) / out["close"]

    return out


def _candle_patterns(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    body = (out["close"] - out["open"]).abs()
    upper_wick = out[["open", "close"]].max(axis=1) - out["low"]
    lower_wick = out["high"] - out[["open", "close"]].max(axis=1)

    out["hammer"] = (upper_wick > 2 * body) & (lower_wick < body)

    prev_open = out["open"].shift(1)
    prev_close = out["close"].shift(1)
    bullish_prev = prev_close < prev_open
    bearish_prev = prev_close > prev_open

    out["bullish_engulfing"] = bullish_prev & (out["close"] > out["open"]) & (out["open"] < prev_close) & (out["close"] > prev_open)
    out["bearish_engulfing"] = bearish_prev & (out["close"] < out["open"]) & (out["open"] > prev_close) & (out["close"] < prev_open)
    return out


if not uploaded:
    st.info("👈 Lade eine CSV, um Analyse und Signale zu berechnen.")
    st.stop()

try:
    raw_df = pd.read_csv(uploaded)
    df = _normalize_columns(raw_df)
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df = df.dropna(subset=["date", "open", "high", "low", "close"]).sort_values("date")

    for col in ["open", "high", "low", "close", "volume"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.dropna(subset=["open", "high", "low", "close"])

    analysis = _calculate_signals(df)
    analysis = _candle_patterns(analysis)

except Exception as err:
    st.error(f"Fehler beim Verarbeiten der Datei: {err}")
    st.stop()

latest = analysis.iloc[-1]

col1, col2, col3, col4 = st.columns(4)
col1.metric("Letzter Close", f"{latest['close']:.2f}")
col2.metric("Signal", latest["signal"])
col3.metric("RSI (14)", f"{latest['rsi']:.1f}" if pd.notna(latest["rsi"]) else "n/a")
col4.metric("Volatilität (20)", f"{latest['volatility_20']:.2%}" if pd.notna(latest["volatility_20"]) else "n/a")

st.subheader("📊 Kurs & EMAs")
plot_df = analysis.set_index("date")[["close", "ema_fast", "ema_slow"]]
st.line_chart(plot_df)

left, right = st.columns([2, 1])

with left:
    st.subheader("🔎 Neuheiten entdecken (Scanner-Ansatz)")
    newest = analysis.tail(20).copy()
    newest["pattern"] = "-"
    newest.loc[newest["hammer"], "pattern"] = "Hammer"
    newest.loc[newest["bullish_engulfing"], "pattern"] = "Bullish Engulfing"
    newest.loc[newest["bearish_engulfing"], "pattern"] = "Bearish Engulfing"

    st.dataframe(
        newest[["date", "close", "signal", "rsi", "volatility_20", "pattern"]].sort_values("date", ascending=False),
        use_container_width=True,
        hide_index=True,
    )

with right:
    st.subheader("🧠 Strategie-Generator")
    risk_mode = st.selectbox("Risikoprofil", ["Konservativ", "Ausgewogen", "Offensiv"])
    market_type = st.selectbox("Markt", ["Aktien", "ETF", "Krypto"])

    if st.button("Strategie vorschlagen"):
        if risk_mode == "Konservativ":
            sl, tp = "0.8%", "1.5%"
            filter_text = "Handel nur mit Trendrichtung (EMA 21)."
        elif risk_mode == "Ausgewogen":
            sl, tp = "1.2%", "2.4%"
            filter_text = "Trend + RSI-Filter (kein Einstieg zwischen 48-52)."
        else:
            sl, tp = "2.0%", "4.0%"
            filter_text = "Breakout + Retest auf Intraday-Hoch/Tief."

        session_hint = "London/NY Overlap" if market_type in ["Aktien", "ETF"] else "US-Session + hohe Liquidität"
        st.success(
            f"""
**{market_type}-Tagestrading Setup ({risk_mode})**
- Einstieg: LONG bei EMA9 > EMA21 und RSI > 52, SHORT umgekehrt.
- Stop-Loss: {sl}
- Take-Profit: {tp}
- Filter: {filter_text}
- Beste Handelszeit: {session_hint}
"""
        )

st.warning("Hinweis: Kein Finanzrat. Backteste jede Strategie mit deinen eigenen Daten.")
