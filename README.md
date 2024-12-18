
# Quiz App Backend

The backend is built using Django and provides the API for the quiz application.

## Setup Instructions

### 1. Clone the Repository
Clone the backend repository using the following command:

```bash
git clone https://github.com/jay270804/quiz-app.git
```

### 2. Navigate to the Project Directory
Change into the project directory:

```bash
cd quiz-app
```

### 3. Create a Python Virtual Environment

#### For Windows:
Run the following command to create a virtual environment:

```bash
python -m venv venv
```

#### For Linux/Mac:
Run the following command to create a virtual environment:

```bash
python3 -m venv venv
```

### 4. Activate the Virtual Environment

#### For Windows:
Activate the virtual environment with:

```bash
venv\Scripts\activate
```

#### For Linux/Mac:
Activate the virtual environment with:

```bash
source venv/bin/activate
```

### 5. Install Dependencies
Install the required dependencies by running the following command:

```bash
pip install -r requirements.txt
```

### 6. Run the Django Development Server
To check if Django is working correctly, run:

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser. You should see the Django welcome page if everything is set up correctly.

### 7. Apply Migrations
Run the following command to apply database migrations:

```bash
python manage.py migrate
```

This will set up the necessary database tables for the application.

### 8. Seed the Questions
To populate the database with quiz questions, run:

```bash
python manage.py seed_questions
```

This will add sample quiz questions to the database.

### 9. Start the Server
Once all the steps above are completed, your backend should be set up and ready. Run the server again to start your backend:

```bash
python manage.py runserver
```

Your backend is now running, and the API endpoints should be available at `http://127.0.0.1:8000/`.

---

## Notes

- Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).
- Use a Python version compatible with Django as specified in the `requirements.txt` file.
- If you encounter any issues during setup, check the error messages carefully or refer to Django's official documentation for troubleshooting.
