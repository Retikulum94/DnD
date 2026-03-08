import streamlit as st
from functions.zufall import ZufallszahlenGenerator

st.title("Zufallszahlgenerator")

st.write("Diese Seite generiert Zufallszahlen.")

zahltyp = st.radio("Wähle den Typ der Zufallszahl:", 
                   ["Ganze Zahl", "Rationale Zahl", "Bruch"])

gen = ZufallszahlenGenerator()

if zahltyp == "Ganze Zahl":
    col1, col2 = st.columns(2)
    with col1:
        von = st.number_input("Von:", value=0, step=1)
    with col2:
        bis = st.number_input("Bis:", value=100, step=1)
    
    if st.button("Generiere ganze Zahl"):
        zahl = gen.ganze_zahl(int(von), int(bis))
        st.success(f"Zufallszahl: **{zahl}**")

elif zahltyp == "Rationale Zahl":
    col1, col2 = st.columns(2)
    with col1:
        von = st.number_input("Von:", value=0.0, step=0.1)
    with col2:
        bis = st.number_input("Bis:", value=1.0, step=0.1)
    
    if st.button("Generiere rationale Zahl"):
        zahl = gen.rationale_zahl(von, bis)
        st.success(f"Zufallszahl: **{zahl:.4f}**")

elif zahltyp == "Bruch":
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Zähler-Bereich")
        von_z = st.number_input("Von (Zähler):", value=0, step=1)
        bis_z = st.number_input("Bis (Zähler):", value=10, step=1)
    with col2:
        st.subheader("Nenner-Bereich")
        von_n = st.number_input("Von (Nenner):", value=1, step=1, min_value=1)
        bis_n = st.number_input("Bis (Nenner):", value=10, step=1, min_value=1)
    
    if st.button("Generiere Bruch"):
        bruch = gen.bruch(int(von_z), int(bis_z), int(von_n), int(bis_n))
        st.success(f"Zufallsbruch: **{bruch}**")