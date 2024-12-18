# Quiz App Backend

This is the backend for the Quiz App, built using Django.

## Features
- Start a quiz session.
- Fetch random questions.
- Submit answers and get feedback.
- View session statistics.

## API Endpoints

### Quiz Endpoints
- `POST /quiz/` - Starts a new quiz session and returns a session ID.
- `GET /quiz/` - Fetches session statistics for a given session ID.

### Question Endpoints
- `GET /question/random/` - Fetches a random question for the given session ID.

### Answer Endpoints
- `POST /answer/` - Submits an answer for a question and returns whether it was correct, along with the current score.

These API endpoints are tested using Django's test framework. To run the tests, use:
```bash
python manage.py test quiz
```

## Setup Instructions

### Step 1: Clone the Repository
```bash
https://github.com/jay270804/quiz-app.git
cd quiz-app
```

### Step 2: Create a Python Virtual Environment

#### On Windows
```bash
python -m venv env
```

#### On macOS/Linux
```bash
python3 -m venv env
```

### Step 3: Activate the Virtual Environment

#### On Windows
```bash
env\Scripts\activate
```

#### On macOS/Linux
```bash
source env/bin/activate
```

### Step 4: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 5: Verify Django Installation
Run the following command to ensure Django is properly installed:
```bash
python manage.py runserver
```

### Step 6: Apply Migrations
```bash
python manage.py migrate
```

### Step 7: Seed Questions
Seed the database with sample questions:
```bash
python manage.py seed_questions
```

### Step 8: Start the Server
Start the Django development server:
```bash
python manage.py runserver
```

Your backend is now set up and running at `http://127.0.0.1:8000`.

## Project Structure
- `quiz/` - Contains the core app handling quiz logic.
- `manage.py` - Django management script.
- `db.sqlite3` - SQLite database file (auto-generated).

## Additional Information

### How to Test Endpoints
You can use tools like Postman or cURL to test the API endpoints. For example:

#### Start a New Quiz Session
```bash
POST http://127.0.0.1:8000/quiz/
```

#### Fetch a Random Question
```bash
GET http://127.0.0.1:8000/question/random/?session_id=<your_session_id>
```

#### Submit an Answer
```bash
POST http://127.0.0.1:8000/answer/
Body: {
    "session_id": "<your_session_id>",
    "question_id": "<your_question_id>",
    "answer": "<your_answer>"
}
```

#### Fetch Session Stats
```bash
GET http://127.0.0.1:8000/quiz/?session_id=<your_session_id>
```
