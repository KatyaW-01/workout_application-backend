from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy import CheckConstraint
from marshmallow import Schema, fields

db = SQLAlchemy()

# Define Models here
class Exercise(db.Model):
  __tablename__ = 'exercises'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String)
  category = db.Column(db.String)
  equipment_needed = db.Column(db.Boolean)

  workout_exercises = db.relationship('WorkoutExercise', back_populates='exercise')

  @validates('name')
  def validate_name(self, key, name):
    if not name:
      raise ValueError("Name cannot be Empty")
    if not isinstance(name,str):
      raise TypeError("Name must be a string")
    return name

  def __repr__(self):
    return f'<Exercese {self.id}, {self.name}, {self.category}, {self.equipment_needed}>'
  
class ExerciseSchema(Schema):
  id = fields.Int(dump_only=True)
  name = fields.String()
  category = fields.String()
  equipment_needed = fields.Boolean()

  workout_exercises = fields.Nested(lambda: WorkoutExerciseSchema(exclude=("exercise",)), many=True)


class Workout(db.Model):
  __tablename__ = 'workouts'

  id = db.Column(db.Integer, primary_key=True)
  date = db.Column(db.Date)
  duration_minutes = db.Column(db.Integer)
  notes = db.Column(db.Text)

  workout_exercises = db.relationship('WorkoutExercise', back_populates='workout')
  exercises = association_proxy('workout_exercises', 'exercise')

  __table_args__ = (
    CheckConstraint("date <= CURRENT_DATE", name="check_date_not_future"),
  )

  def __repr__(self):
    return f'<Exercese {self.id}, {self.date}, {self.duration_minutes}, {self.notes}>'
  
class WorkoutSchema(Schema):
  id = fields.Int(dump_only=True)
  date = fields.Date()
  duration_minutes = fields.Int()
  notes = fields.String()

  workout_exercises = fields.Nested(lambda: WorkoutExerciseSchema(exclude=("workout",)),many=True)

class WorkoutExercise(db.Model):
  __tablename__ = 'workout_exercises'

  id = db.Column(db.Integer, primary_key=True)
  reps = db.Column(db.Integer, db.CheckConstraint('reps < 50'))
  sets = db.Column(db.Integer)
  duration_seconds = db.Column(db.Integer)

  workout_id = db.Column(db.Integer, db.ForeignKey('workouts.id'))
  exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'))

  workout = db.relationship('Workout', back_populates='workout_exercises')
  exercise = db.relationship('Exercise', back_populates='workout_exercises')

  @validates('duration_seconds')
  def validate_duration_seconds(self,key,seconds):
    if not seconds:
      raise ValueError("Duration seconds cannot be blank")
    if not isinstance(seconds,int):
      raise TypeError("Duration seconds must be an integer")
    return seconds

  def __repr__(self):
    return f'<Exercese {self.id}, Date: {self.workout.date}, Exercise: {self.exercise.name}, Reps: {self.reps}, Sets: {self.sets}, Duration: {self.duration_seconds}>'
  
class WorkoutExerciseSchema(Schema):
  id = fields.Int(dump_only=True)
  reps = fields.Int()
  sets = fields.Int()
  duration_seconds = fields.Int()

  workout = fields.Nested(lambda: WorkoutSchema(exclude=("workout_exercises",)), many=True)
  exercise = fields.Nested(lambda: ExerciseSchema(exclude=("workout_exercises",)), many=True)


