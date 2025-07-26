from flask import Flask, make_response
from flask_migrate import Migrate

from models import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)

#Define Routes here

@app.route('/workouts', method=["GET"])
def get_workouts():
  #list all workouts
  pass

@app.route('/workouts/<id>', method=["GET"])
def get_workout(id):
  #show a single workout with its associated exercises
  #include reps/sets/duration from WorkoutExercises if you can
  pass

@app.route('/workouts', methods=["POST"])
def create_workouts():
  #create a workout
  pass

@app.route('/workouts/<id>', methods=["DELETE"])
def delete_workout(id):
  #delte a workout
  #delete associated WorkoutExercises if you can 
  pass


if __name__ == '__main__':
  app.run(port=5555, debug=True)