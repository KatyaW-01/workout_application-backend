from flask import Flask, make_response, request
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
  workout_schema = WorkoutSchema()
  data = request.get_json()
  workout_data = workout_schema.load(data)
  workout = Workout(date=workout_data["date"], duration_minutes=workout_data["duration_minutes"], notes=workout_data["notes"])
  db.session.add(workout)
  db.session.commit()
  result = workout_schema.dump(workout)
  return make_response(result,201)

@app.route('/workouts/<id>', methods=["DELETE"])
def delete_workout(id):
  workout = Workout.query.filter_by(id=id).first()
  if workout:
    db.session.delete(workout)
    db.session.commit()
    body = {'message': f'Workout {id} deleted successfully.'}
    status = 200
  else:
    body = {'message': f'Workout {id} not found.'}
    status = 404
  return make_response(body,status)

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
  exercise_schema = ExerciseSchema()
  data = request.get_json()
  exercise_data = exercise_schema.load(data)
  exercise = Exercise(name = exercise_data["name"], category = exercise_data["category"])
  db.session.add(exercise)
  db.session.commit()
  result = exercise_schema.dump(exercise)
  return make_response(result,201)

@app.route('/exercises/<id>', methods=["DELETE"])
def delete_exercise(id):
  exercise  = Exercise.query.filter_by(id=id).first()
  if exercise:
    db.session.delete(exercise)
    db.session.commit()
    body = {'message': f'Exercise {id} deleted successfully.'}
    status = 200
  else:
    body = {'message': f'Exercise {id} not found.'}
    status = 404
  return make_response(body,status)

@app.route('/workouts/<workout_id>/exercises/<exercise_id>/workout_exercises', methods=["POST"])
def add_exercise_to_workout(workout_id,exercise_id):
  workout = Workout.query.filter_by(id=workout_id).first()
  exercise  = Exercise.query.filter_by(id=exercise_id).first()
  if not workout or not exercise:
    body = {"error": "Workout or Exercise not found"}
    status = 404
    return make_response(body,status)
  data = request.get_json()
  workout_exercise_schema = WorkoutExerciseSchema()
  workout_exercise_data = workout_exercise_schema.load(data)
  workout_exercise = WorkoutExercise(workout = workout, exercise = exercise, reps = workout_exercise_data["reps"], sets = workout_exercise_data["sets"], duration_seconds = workout_exercise_data["duration_seconds"])
  db.session.add(workout_exercise)
  db.session.commit()
  result = workout_exercise_schema.dump(workout_exercise)
  return make_response(result, 201)

if __name__ == '__main__':
  app.run(port=5555, debug=True)