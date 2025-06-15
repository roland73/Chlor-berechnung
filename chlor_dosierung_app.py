import streamlit as st

# Titel
st.title("Chlor-Dosierungsrechner für Pools")

# Eingaben
pool_volume = st.number_input("Poolvolumen (in m³)", min_value=1.0, value=14.0, step=0.1)
chlor_current = st.number_input("Aktueller Chlorgehalt (in mg/l)", min_value=0.0, value=0.0, step=0.1)
chlor_target = st.number_input("Zielwert freies Chlor (in mg/l)", min_value=0.1, value=1.0, step=0.1)
chlor_concentration = st.selectbox("Konzentration des Chlorprodukts", options=[12, 13, 14, 15])

# Berechnung
chlor_difference = max(chlor_target - chlor_current, 0)
chlor_needed = round((chlor_difference * pool_volume * 1000) / (chlor_concentration * 10 * 1000), 2)

# Ausgabe
st.markdown(f"### Benötigte Menge: {chlor_needed} Liter bei {chlor_concentration}% Aktivchlor")

if chlor_difference <= 0:
    st.warning("Der aktuelle Chlorwert liegt bereits auf oder über dem Zielwert. Keine Zugabe erforderlich.")

st.info("Tipp: Flüssigchlor immer abends oder bei bedecktem Himmel zugeben und Filter mindestens 6 Stunden laufen lassen.")
