from fastapi import FastAPI, Depends, HTTPException
from models import pyWorkout ,pyWorkout_create
from database import get_db
from database_models import Workout as dbworkout
from sqlalchemy.orm import Session
import __init__

app=FastAPI()


@app.get("/")
def greet():
    return "Hello World"


@app.get("/workouts",response_model=list[pyWorkout])
def get_all_workouts(db: Session=Depends(get_db)):
    workouts=db.query(dbworkout).all()
    return workouts

@app.get("/workouts/{workout_id}",response_model=pyWorkout)
def get_workout_by_id(workout_id: int, db: Session=Depends(get_db)):
    workout= db.query(dbworkout).filter(dbworkout.id==workout_id).first()
    if workout is None:
        raise HTTPException(status_code=404,detail="No workouts found by that id.")
    return workout

@app.post("/workouts",response_model=pyWorkout)
def add_workout(workout: pyWorkout_create, db: Session=Depends(get_db)):
    db_workout=dbworkout(**workout.model_dump())
    db.add(db_workout)
    db.commit()
    db.refresh(db_workout)
    return db_workout

# @app.put("/workouts")
# def update_workout(workout_id:int, workout:Workout):
#     for i in range(len(workouts)):
#         if workouts[i].id==workout_id:
#             workouts[i]=workout
#             return "Workout edited successfully"
#     return "Workout not found"

@app.delete("/workouts/{workout_id}")
def delete_workout(workout_id: int, db: Session=Depends(get_db)):
    workout= db.query(dbworkout).filter(dbworkout.id==workout_id).first()
    if workout is None:
        raise HTTPException(status_code=404,detail="No workouts found by that id.")
    db.delete(workout)
    db.commit()
    return "Workout deleted successfully"