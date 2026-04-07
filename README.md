
# 🎯 EuroGenius – Dein KI-gestützter Lotto-Assistent

Willkommen bei EuroGenius – der modernen Streamlit-App für Lotto-Spieler in der Schweiz und der EU.
Diese App analysiert EuroMillions-Ziehungen, generiert Tipps, Strategien und speichert alles sicher über Supabase.

## 🔐 Funktionen
- Supabase-Login mit Gast- und Premium-Zugang
- Strategie-Seite mit Tabs, Slidern & Speicherfunktion
- Tippgenerator (für Premium unbegrenzt, für Gast 3 Tipps)
- Benutzerfreundliche Navigation (Zurück / Weiter)
- 📈 Trading Bot Lab für Aktien, ETF & Krypto (OHLCV-Analyse, EMA/RSI-Signale, Candlestick-Scanner)
- Vorbereitet für Abo-Modell & Zahlungssystem (Stripe)

## 🧱 Struktur
```
.
├── .streamlit/
│   └── secrets.toml
├── pages/
│   ├── home.py
│   ├── login.py
│   ├── main_app.py
│   ├── strategie.py
├── custom_style.py
├── supabase_connector.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation
1. Repository klonen:
```
git clone https://github.com/dein-nutzer/eurogenius.git
cd eurogenius
```

2. Virtuelle Umgebung aktivieren & installieren:
```
pip install -r requirements.txt
```

3. Supabase-Zugang in `.streamlit/secrets.toml` hinterlegen

4. App starten:
```
streamlit run pages/home.py
```

## 📦 Deployment
Bereit für Streamlit Cloud. Einfach GitHub verbinden und `pages/home.py` als Hauptseite wählen.

## 📧 Kontakt
Für Support oder Kooperationen: eurogenius@demo.com
