from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import QuizSession, Questions
from .serializers import QuestionsSerializer

# Create your tests here.


class QuizTest(TestCase):
    """Test class for testing api's"""

    def setUp(self):
        """method for setting up client for all the below tests"""
        self.client = APIClient()

    def test_start_quiz_session(self):
        """method to test (POST api/start-quiz) endpoint"""
        response = self.client.post(reverse("start-quiz"))
        self.assertEqual(response.status_code, 201)
        self.assertIn("session_id", response.data)

    def test_get_random_question(self):
        """method to test (GET api/get-question) endpoint"""
        session = QuizSession.objects.create()
        data = {
            "question_text":"What is the name of the programming language developed by James Gosling at Sun Microsystems and named after the type of coffee from Indonesia",
            "options":{"A": "Java", "B": "Python", "C": "C++", "D": "Ruby"},
            # "options":["A","B","C","D"],
            # "correct_option":"A",
            "correct_option":"A",
        }

        serializer = QuestionsSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
        else:
            print(f"Validation Error: {serializer.errors}")

        response = self.client.get(
            reverse("get-question") + f"?session_id={session.id}"
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("question_id", response.data.get('question'))
        self.assertIn("options", response.data.get('question'))
