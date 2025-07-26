#!/usr/bin/env python3

from app import app
from models import *
from datetime import date

with app.app_context():
  #reset data and add new example data, committing to db
  Exercise.query.delete()
  Workout.query.delete()
  WorkoutExercise.query.delete()

  #add exercises
  e1 = Exercise(name ="Jumping Jacks", category ="Cardio", equipment_needed = False)
  e2 = Exercise(name="Bench Press", category="Strength", equipment_needed=True)
  e3 = Exercise(name="Kettlebell Swing", category="Strength", equipment_needed=True)
  e4 = Exercise(name="Running", category="Cardio", equipment_needed=False)
  e5 = Exercise(name="Pull-Up", category="Strength", equipment_needed=True)
  db.session.add_all([e1,e2,e3,e4,e5])
  db.session.commit()

  #add workouts
  w1 = Workout(date=date(2025, 7, 20), duration_minutes=45, notes="Full body strength training with focus on legs.")
  w2 = Workout(date=date(2025, 7, 21), duration_minutes=30, notes="Cardio session: running and jump rope.")
  w3 = Workout(date=date(2025, 7, 22), duration_minutes=60, notes="HIIT workout with burpees, kettlebell swings, and planks.")
  w4 = Workout(date=date(2025, 7, 25), duration_minutes=35, notes="Light cardio and stretching.")
  db.session.add_all([w1,w2,w3,w4])
  db.session.commit()

  #add workout exercise
  we1 = WorkoutExercise(workout=w2, exercise=e1, reps=12, sets=3, duration_seconds=60)
  we2 = WorkoutExercise(workout=w2, exercise=e3, reps=10, sets=4, duration_seconds=45)
  we3 = WorkoutExercise(workout=w3, exercise=e3, reps=15, sets=2, duration_seconds=90)
  we4 = WorkoutExercise(workout=w4, exercise=e4, reps=20, sets=3, duration_seconds=120)
  we5 = WorkoutExercise(workout=w4, exercise=e5, reps=18, sets=4, duration_seconds=75)
  db.session.add_all([we1,we2,we3,we4,we5])
  db.session.commit()




