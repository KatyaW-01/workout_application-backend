# Workout Tracker API

## Project Description

The Workout Tracker API is a Flask-based backend for a workout tracking application. The application tracks both workouts and exercises and exercises are reusable across workouts, including details such as sets, reps, and duration. This API follows REST conventions and uses SQLAlchemy for ORM and Marshmallow for data serialization and validation.

## Installation Instructions

1. **Clone the Repository**
   ```bash
   git clone <your-repo-url>
   cd <your-project-directory>
   ```

2. **Create and Activate a Virtual Environment**
    ```bash
    virutalenv env
    source env/bin/activate
    ```
3. **Install all Necessary Dependencies**
    ```bash
    pip install -r requirements.txt
    ```
4. **Set Up the Database**
    ```bash
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```
5. Seed the Database
    ```bash
    python seed.py
    ```
## Run Instructions
To start the development server:
```bash
python app.py
```
## API Endpoints
`GET /`
* returns a welcome message
### Workouts
* `GET /workouts` <br>
Returns a list of all workouts with their assoiated exercises
* `GET /workouts/<id>` <br>
Returns a specific workout by id
* `POST /workouts` <br>
Creates a new workout
* `DELETE /workouts/<id>` <br>
Deletes a workout by id
### Exercises
* `GET /exercises` <br>
Returns a list of all exercises
* `GET /exercises/<id>` <br>
Returns a specific exercise by ID
* `POST /exercises` <br>
Creates a new exercise
* `DELETE /exercises/<id>` <br>
Deletes a specific exercise by ID
### Workout Exercises (Associations)
* `POST /workouts/<workout_id>/exercises/<exercise_id>/workout_exercises` <br>
Adds an existing exercise to a workout while also adding information of reps, sets, and duration