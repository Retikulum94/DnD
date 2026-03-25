import streamlit as st
import pandas as pd
from datetime import datetime
import pytz
from utils.data_manager import DataManager
from functions.rechnungen import add, subtract, square, root

st.title("Hier könnt ihr diverse Berechnungen durchführen")
st.write(" Keine scheu, probiert es aus. ;) ")

if 'data_df' not in st.session_state:
    st.session_state['data_df'] = pd.DataFrame(columns=['timestamp', 'Rechnung', 'Resultat'])

with st.form("Addieren"):
    st.write("Gib hier deine Zahlen die du addieren willst ein:")
    a = st.number_input("Nummer 1")
    b = st.number_input("Nummer 2")
    submitted = st.form_submit_button("Berechnen")  
    if submitted:
        st.write("Ergebnis:", add(a, b))
        new_entry = {
            "timestamp": datetime.now(pytz.timezone('Europe/Zurich')),
            "Rechnung": f"{a} + {b}",
            "Resultat": add(a, b)
        }
        st.session_state['data_df'] = pd.concat([st.session_state['data_df'], pd.DataFrame([new_entry])], ignore_index=True)


data_manager = DataManager()
data_manager.save_user_data(st.session_state['data_df'], 'data.csv')
st.dataframe(st.session_state['data_df'])
