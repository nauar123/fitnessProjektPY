import streamlit as st
import pandas as pd
import datetime


st.title("Se træninger")


if "workout" not in st.session_state or not st.session_state.workout:
    st.write("Du har ikke registreret nogen øvelser endnu.")
else:
    st.subheader("Dine registrerede øvelser:")
# Her vises de registrerede øvelser i en tabel, hvis der er nogen


# Her vises de registrerede øvelser ved at gennemgå listen
for w in st.session_state.workout:
    st.write(f"{w['exercise']}: {w['weight']} kg, {w['sets']} sæt, {w['reps']} gentagelser")


# Her vises de som tabel med Pandas DataFrame
if st.session_state.workout:
    df = pd.DataFrame(st.session_state.workout)
    st.dataframe(df)
