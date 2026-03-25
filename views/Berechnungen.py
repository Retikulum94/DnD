import streamlit as st
import pandas as pd
from datetime import datetime
import pytz
import plotly.graph_objects as go
import plotly.express as px
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

with st.form("Subtrahieren"):
    st.write("Gib hier deine Zahlen die du subtrahieren willst ein:")
    a = st.number_input("Nummer 1")
    b = st.number_input("Nummer 2")
    submitted = st.form_submit_button("Berechnen")  
    if submitted:
        st.write("Ergebnis:", subtract(a, b))
        new_entry = {
            "timestamp": datetime.now(pytz.timezone('Europe/Zurich')),
            "Rechnung": f"{a} - {b}",
            "Resultat": subtract(a, b)
        }
        st.session_state['data_df'] = pd.concat([st.session_state['data_df'], pd.DataFrame([new_entry])], ignore_index=True)

with st.form("Quadrieren"):
    st.write("Gib hier deine Zahl die du quadrieren willst ein:")
    a = st.number_input("Nummer")
    submitted = st.form_submit_button("Berechnen")  
    if submitted:
        st.write("Ergebnis:", square(a))
        new_entry = {
            "timestamp": datetime.now(pytz.timezone('Europe/Zurich')),
            "Rechnung": f"{a}^2",
            "Resultat": square(a)
        }
        st.session_state['data_df'] = pd.concat([st.session_state['data_df'], pd.DataFrame([new_entry])], ignore_index=True)

with st.form("Wurzelziehen"):
    st.write("Gib hier deine Zahl und den Wurzelexponenten ein:")
    a = st.number_input("Zahl")
    b = st.number_input("Wurzelexponent")
    submitted = st.form_submit_button("Berechnen")  
    if submitted:
        st.write("Ergebnis:", root(a, b))
        new_entry = {
            "timestamp": datetime.now(pytz.timezone('Europe/Zurich')),
            "Rechnung": f"√{b}({a})",
            "Resultat": root(a, b)
        }
        st.session_state['data_df'] = pd.concat([st.session_state['data_df'], pd.DataFrame([new_entry])], ignore_index=True)

data_manager = DataManager()
data_manager.save_user_data(st.session_state['data_df'], 'data.csv')
st.dataframe(st.session_state['data_df'])

# Visualisierung der Berechnungsresultate
if len(st.session_state['data_df']) > 0:
    st.subheader("📊 Visualisierung der Resultate")
    
    col1 = st.columns(2)
    
    with col1:
        # Balkendiagramm: Resultate pro Rechnung
        fig1 = px.bar(
            st.session_state['data_df'],
            x='Rechnung',
            y='Resultat',
            title='Resultate nach Rechenoperation',
            color='Resultat',
            color_continuous_scale='Viridis'
        )
        fig1.update_layout(height=400)
        st.plotly_chart(fig1, use_container_width=True)
    