
import streamlit as st

st.set_page_config(page_title="👋 Willkommen bei EuroGenius", layout="centered")

st.title("🎉 Willkommen bei EuroGenius – Deiner Lotto-Analyseplattform")

st.markdown("""
EuroGenius kombiniert **Künstliche Intelligenz**, **statistische Analyse** und **universelle Zahlensysteme**, um dir bei der Auswahl deiner EuroMillion-Tipps zu helfen.

### 📥 Schritt 1: Daten hochladen
Lade in der **Seitenleiste links** deine EuroMillion-Ziehungen im CSV-Format hoch.

Beispielstruktur:
```
Datum, Zahl1, Zahl2, Zahl3, Zahl4, Zahl5
2024-05-10, 5, 13, 22, 31, 42
```

### 🎯 Schritt 2: Strategie auswählen
Wähle oben eine der folgenden Seiten:
- 🧠 **KI-Strategie**
- 🌀 **Cluster-Strategie**
- 📈 **Gewinnmuster & Trends**
- ♾️ **Universelle Muster**
- ✅ **Meta-Strategie** (empfohlen für kombinierte Tipps)

### 🆘 Hilfe
Bei Fragen oder Problemen klicke auf den [Support-Link](https://example.com/hilfe) oder lade eine Beispiel-Datei zum Testen.

---

Viel Erfolg bei deiner nächsten Ziehung! 🍀
""")

st.success("🚀 Los geht's – lade deine CSV in der Sidebar hoch!")
