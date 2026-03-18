import streamlit as st
import pandas as pd
from utils.data_manager import DataManager  # --- NEW CODE: import data manager ---
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
        
 # --- CODE UPDATE: save data to data manager ---
    data_manager = DataManager()
    data_manager.save_user_data(st.session_state['data_df'], 'data.csv')
    # --- END OF CODE UPDATE ---
        
# display the data frame in a table
st.dataframe(st.session_state['data_df'])