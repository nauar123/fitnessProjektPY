from fastapi import FastAPI
from pydantic import BaseModel  # det er en slags skabelon for data
import datetime
from typing import List

app = FastAPI()

# Midlertidig database
workouts = []

# Det her model strukturen laves for daten
class Workout(BaseModel):
    exercise: str
    weight: int
    sets: int
    reps: int

# POST GEM træning
@app.post("/workout")
def add_workout(workout: Workout):
    data = workout.dict()  # Nødvendig for at gemme data
    data["date"] = datetime.datetime.now()

    workouts.append(data)
    return {"message": "Workout added", "data": data}

# GET - hent alle træninger
@app.get("/workouts")
def get_workouts():
    return workouts