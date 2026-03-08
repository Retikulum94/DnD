import streamlit as st
from functions.ph1 import ph_from_hydrogen

st.title("pH‑Wert berechnen")
st.write("Gib die H⁺‑Konzentration (mol/L) ein, um den pH‑Wert zu erhalten.")

with st.form("pH‑Formular"):
    conc = st.number_input(
        "H⁺‑Konzentration (mol/L)",
        min_value=0.0,
        format="%f",
        help="z. B. 1e-7 für reines Wasser"
    )
    submitted = st.form_submit_button("Berechnen")
    if submitted:
        try:
            ph = ph_from_hydrogen(conc)
            st.write("pH:", ph)
        except ValueError as e:
            st.error(e)