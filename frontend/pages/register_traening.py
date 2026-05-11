import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import requests #bruges til at sende HTTP anmodninger til backend API'et



# Der oprettes en liste i session_state for at gemme de registrerede øvelser,
# så de kan vises senere.
#if "workout" not in st.session_state:
   # st.session_state.workout = []
    # st.session_state er en måde at gemme data på tværs af forskellige
    # interaktioner i Streamlit-appen, uden at data går tabt når siden opdateres.


#inputfelter
exercise = st.text_input("Hvilken øvelse har du lavet?")
weight = st.number_input("Hvilken vægt har du brugt?", min_value=0)
sets = st.number_input("Hvor mange sæt har du lavet?", min_value=0)
reps = st.number_input("Hvor mange gentagelser har du lavet?", min_value=0)


if st.button("Gem øvelse"):

    # Her oprettes en dictionary, der indeholder oplysningerne om den registrerede øvelse, samme struktur som basemodelen i backend/main.py
    workout = {
        "exercise": exercise, 
        "weight": weight,
        "sets": sets,
        "reps": reps,
        
        #"date": datetime.datetime.now()  # Her tilføjes dato og tid for registreringen,
        # BACKENDEN TILFØJER DATO, SÅ DET ER IKKE NØDVENDIGT HER, DET BLEV BRUGT UNDER TESTNING
    }

    # Her tilføjes øvelsen til listen i session_state
    #st.session_state.workout.append(workout)

   ## st.success(f"Du har registreret {exercise} med {weight} kg, {sets} sæt og {reps} gentagelser.")

# Her sendes data til backend API'et ved hjælp af en POST-anmodning
    response = requests.post("http://localhost:8000/workout", 
                             json=workout)
    
    if response.status_code == 200:
        st.success("Øvelse gemt og sendt til backend!")
    else:
        st.error("Der opstod en fejl ved at sende data til backend.")
