import streamlit as st
import pandas as pd
from utils.data_manager import DataManager  # --- NEW CODE: import data manager ---
from functions.rechnungen import add, subtract, square, root

st.title("Hier könnt ihr diverse Berechnungen durchführen")
st.write(" Keine scheu, probiert es aus. ;) ")

with st.form("Addieren"):
    st.write("Gib hier deine Zahlen die du addieren willst ein:")
    a = st.number_input("Nummer 1")
    b = st.number_input("Nummer 2")
    submitted = st.form_submit_button("Berechnen")  
    if submitted:
        st.write("Ergebnis:", add(a, b))
        st.session_state['data_df'] = pd.concat([st.session_state['data_df'], pd.DataFrame([add(a, b)])])

with st.form("Subtrahieren"):
    st.write("Gib hier deine Zahlen die du subtrahieren willst ein:")
    a = st.number_input("Nummer 1", key="sub_a")
    b = st.number_input("Nummer 2", key="sub_b")
    submitted = st.form_submit_button("Berechnen", key="sub_submit")  
    if submitted:
        st.write("Ergebnis:", subtract(a, b))
        st.session_state['data_df'] = pd.concat([st.session_state['data_df'], pd.DataFrame([subtract(a, b)])])

with st.form("Quadrieren"):
    st.write("Gib hier deine Zahl die du quadrieren willst ein:")
    a = st.number_input("Nummer", key="square_a")
    submitted = st.form_submit_button("Berechnen", key="square_submit")  
    if submitted:
        st.write("Ergebnis:", square(a))
        st.session_state['data_df'] = pd.concat([st.session_state['data_df'], pd.DataFrame([square(a)])])

with st.form("Wurzel"):
    st.write("Gib hier deine Zahl und die Wurzel welche daraus gezogen werden soll, ein:")
    a = st.number_input("Nummer", key="root_a")
    b = st.number_input("Wurzelgrad", key="root_b")
    submitted = st.form_submit_button("Berechnen", key="root_submit")  
    if submitted:
        st.write("Ergebnis:", root(a, b))
        st.session_state['data_df'] = pd.concat([st.session_state['data_df'], pd.DataFrame([root(a, b)])])

data_manager = DataManager()
data_manager.save_user_data(st.session_state['data_df'], 'data.csv')
st.dataframe(st.session_state['data_df'])
