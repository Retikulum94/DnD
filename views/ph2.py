import streamlit as st
import pandas as pd
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
    
            # --- NEW CODE to update history in session state and display it ---
        st.session_state['data_df'] = pd.concat([st.session_state['data_df'], pd.DataFrame([ph])])
        
# --- NEW CODE to display the history table ---
st.dataframe(st.session_state['data_df'])