from flask import Flask, make_response
from flask_migrate import Migrate

from models import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)

@app.route('/')
def index():
  return '<h1>Welcome to the Workout App</h1>'

@app.route('/workouts', methods=["GET"])
def get_workouts():
  workouts = Workout.query.all()
  result = WorkoutSchema(many=True).dump(workouts)
  return make_response(result, 200)

@app.route('/workouts/<id>', methods=["GET"])
def get_workout(id):
  workout = Workout.query.filter_by(id=id).first()
  response_body = WorkoutSchema().dump(workout)
  return make_response(response_body, 200)

@app.route('/workouts', methods=["POST"])
def create_workouts():
  #create a workout
  pass

@app.route('/workouts/<id>', methods=["DELETE"])
def delete_workout(id):
  #delte a workout
  #delete associated WorkoutExercises if you can 
  pass

@app.route('/exercises', methods=["GET"])
def get_exercises():
  exercises = Exercise.query.all()
  result = ExerciseSchema(many=True).dump(exercises)
  return make_response(result,200)

@app.route('/exercises/<id>', methods=["GET"])
def get_exercise(id):
  exercise  = Exercise.query.filter_by(id=id).first()
  response_body = ExerciseSchema().dump(exercise)
  return make_response(response_body, 200)

@app.route('/exercises', methods=["POST"])
def create_exercises():
  #create an exercise
  pass

@app.route('/exercises/<id>', methods=["DELETE"])
def delete_exercise(id):
  #delete an exercse
  #delete associated WorkoutExercises if you can
  pass

@app.route('/workouts/<workout_id>/exercises/<exercise_id>/workout_exercises', methods=["POST"])
def add_exercise_to_workout(workout_id,exercise_id):
  #add an exercise to a workout, including reps/sets/duration
  pass


if __name__ == '__main__':
  app.run(port=5555, debug=True)