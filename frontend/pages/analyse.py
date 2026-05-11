import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import numpy as np
import requests  # ✅ bruges til at hente data fra backend


# GRAF
st.title("Analayse af træning")


# GAMMEL LØSNING (session_state) TESTNING
# if "workout" not in st.session_state:
#     st.write("Ingen træninger registreret endnu.")

# else:
#     df = pd.DataFrame(st.session_state.workout)


#  NY LØSNING (BACKEND)
# Henter data fra backend via GET request
response = requests.get("http://127.0.0.1:8000/workouts")

# Tjekker om backend virker
if response.status_code != 200:
    st.error("Kunne ikke hente data fra backend")

else:
    # Konverterer JSON data til Python liste
    data = response.json()

    # Hvis der ikke er data
    if len(data) == 0:
        st.write("Ingen træninger registreret endnu.")

    else:
        # Konverterer data til Pandas DataFrame
        df = pd.DataFrame(data)

        # Her vises de registrerede øvelser ved at gennemgå listen
        df["date"] = pd.to_datetime(df["date"])
        
        df = df.sort_values(by="date")  # Sorter efter dato

        st.subheader("Udvikling over tid")

        # Her vises udviklingen over tid for den valgte øvelse
        selected_exercise = st.selectbox("Vælg en øvelse at analysere", 
            df["exercise"].unique())
        
        # Her filtreres data for den valgte øvelse
        filtered_df = df[df["exercise"] == selected_exercise]

        # Grafen 

        # fiq og ax er variabler, der bruges til at oprette en figur og et sæt akser i Matplotlib.
        # plt er en forkortelse for Matplotlibs pyplot modul, som bruges til at oprette og manipulere grafer og figurer.
        # subplot() funktionen bruges til at oprette en figur og et sæt akser, hvor figuren er det overordnede område, der indeholder grafen,
        # og ax er det specifikke område, hvor grafen vil blive tegnet.
        fiq, ax = plt.subplots()

        ax.plot(filtered_df["date"], filtered_df["weight"], marker="o")

        ax.set_title(f"Udvikling i vægt for {selected_exercise}")
        ax.set_xlabel("Dato")
        ax.set_ylabel("Vægt (kg)")

        st.pyplot(fiq)


        # FINDER ANTAL DAGE MAN HAR TRÆNET 
        st.subheader("Træningsfrekvens")

        # kun dato tages uden tiden
        df["date_only"] = df["date"].dt.date

        # dette er antal unikke træningsdage
        unique_days = df["date_only"].nunique()

        st.write(f"antal træningsdage i alt: {unique_days}")


        # GENNEMSNIT AF ANTAL DAGE MAN TRÆNER PÅ 1 UGE

        # Den finder uge nummer 
        df["week"] = df["date"].dt.isocalendar().week


        # Den viser hvor mange dage per uge man træner
        ugetraining_days_per_week = df.groupby("week")["date_only"].nunique()

        # Gennemsnit af træningsdage pr uge 
        avg_days_per_week = np.mean(ugetraining_days_per_week)
        st.write(f"Gennemsnit træningsdage pr uge: {avg_days_per_week:.2f}")
``