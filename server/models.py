from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
db = SQLAlchemy()

# Define Models here
class Exercise(db.Model):
  __tablename__ = 'exercises'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String)
  category = db.Column(db.String)
  equipment_needed = db.Column(db.Boolean)

  workout_exercises = db.relationship('WorkoutExercise', back_populates='exercise')

  def __repr__(self):
    return f'<Exercese {self.id}, {self.name}, {self.category}, {self.equipment_needed}>'

class Workout(db.Model):
  __tablename__ = 'workouts'

  id = db.Column(db.Integer, primary_key=True)
  date = db.Column(db.Date)
  duration_minutes = db.Column(db.Integer)
  notes = db.Column(db.Text)

  workout_exercises = db.relationship('WorkoutExercise', back_populates='workout')
  exercises = association_proxy('workout_exercises', 'exercise')

  def __repr__(self):
    return f'<Exercese {self.id}, {self.date}, {self.duration_minutes}, {self.notes}>'

class WorkoutExercise(db.Model):
  __tablename__ = 'workout_exercises'

  id = db.Column(db.Integer, primary_key=True)
  reps = db.Column(db.Integer)
  sets = db.Column(db.Integer)
  duration_seconds = db.Column(db.Integer)

  workout_id = db.Column(db.Integer, db.ForeignKey('workouts.id'))
  exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'))

  workout = db.relationship('Workout', back_populates='workout_exercises')
  exercise = db.relationship('Exercise', back_populates='workout_exercises')

  def __repr__(self):
    return f'<Exercese {self.id}, Date: {self.workout.date}, Exercise: {self.exercise.name}, Reps: {self.reps}, Sets: {self.sets}, Duration: {self.duration_seconds}>'


