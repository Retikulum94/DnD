import streamlit as st
import pandas as pd
from datetime import datetime
import pytz
from utils.data_manager import DataManager  # --- NEW CODE: import data manager ---
from functions.ph1 import ph_from_hydrogen

st.title("pH‑Wert berechnen")
st.write("Gib die H⁺‑Konzentration (mol/L) ein, um den pH‑Wert zu erhalten.")

if 'data_df' not in st.session_state:
    st.session_state['data_df'] = pd.DataFrame(columns=['timestamp', 'Konzentration', 'pH'])

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

            new_data = pd.DataFrame([{
                'timestamp': datetime.now(pytz.timezone('Europe/Zurich')),
                'Konzentration': conc,
                'pH': ph
            }])
            st.session_state['data_df'] = pd.concat([st.session_state['data_df'], new_data], ignore_index=True)
            # st.session_state['data_df'] = pd.concat([st.session_state['data_df'], pd.DataFrame([ph])])

            data_manager = DataManager()
            data_manager.save_user_data(st.session_state['data_df'], 'data.csv')

        except ValueError as e:
            st.error(e)
st.dataframe(st.session_state['data_df'])