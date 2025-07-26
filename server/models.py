from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

# Define Models here
class Exercise(db.Model):
  __tablename__ = 'exercises'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String)
  category = db.Column(db.String)
  equipment_needed = db.Column(db.Boolean)

  def __repr__(self):
    return f'<Exercese {self.id}, {self.name}, {self.category}, {self.equipment_needed}>'

class Workout(db.Model):
  __tablename__ = 'workouts'

  id = db.Column(db.Integer, primary_key=True)
  date = db.Column(db.Date)
  duration_minutes = db.Column(db.Integer)
  notes = db.Column(db.Text)

class WorkoutExercises(db.Model):
  __tablename__ = 'workout exercises'

  id = db.Column(db.Integer, primary_key=True)
  reps = db.Column(db.Integer)
  sets = db.Column(db.Integer)
  duration_seconds = db.Column(db.Integer)

  workout_id = db.Column(db.Integer, db.ForeignKey('workouts.id'))
  exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'))


