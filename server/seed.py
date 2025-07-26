#!/usr/bin/env python3

from app import app
from models import *

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
