from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import QuizSession
from .serializers import QuestionsSerializer
from .config import TestConfig

# Create your tests here.


class QuizTest(TestCase):
    """Test class for testing api's"""

    def setUp(self):
        """method for setting up client for all the below tests"""
        self.client = APIClient()
        self.session = QuizSession.objects.create()
        self.test_data = TestConfig.TEST_DATA
        self.question_serializer = QuestionsSerializer(data=self.test_data)

        if self.question_serializer.is_valid():
            self.question = self.question_serializer.save()
        else:
            print(f"Validation Error: {self.question_serializer.errors}")

        self.answer_payload = {
            'session_id':self.session.id,
            'question_id':self.question.id,
            'answer':TestConfig.TEST_ANSWER
        }


    def test_start_quiz_session(self):
        """method to test (POST api/quiz) endpoint"""
        response = self.client.post(reverse("quiz"))
        self.assertEqual(response.status_code, 201)
        self.assertIn("session_id", response.data)


    def test_random_question(self):
        """method to test (GET api/question/random) endpoint"""

        response = self.client.get(
            reverse("random") + f"?session_id={self.session.id}"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.session.id, response.data.get('session_id'))
        self.assertIn("question_id", response.data.get('question'))
        self.assertIn("options", response.data.get('question'))


    def test_submit_answer(self):
        """method to test (POST api/answer) endpoint"""

        response = self.client.post(reverse('answer'), data=self.answer_payload)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.session.id, response.data.get('session_id'))
        self.assertEqual(self.question.id, response.data.get('question_id'))
        self.assertIn('result', response.data)
        self.assertEqual('Correct', response.data.get('result'))
        self.assertIn('score', response.data)

    def test_quiz_report(self):
        """method to test (GET api/quiz) endpoint"""
        self.client.post(reverse('answer'), data=self.answer_payload)

        response = self.client.get(reverse("quiz") + f"?session_id={self.session.id}")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.session.id, response.data.get('session_id'))
        self.assertIn('total_questions', response.data.get('stats'))
        self.assertIn('correct_questions', response.data.get('stats'))
        self.assertIn('incorrect_questions', response.data.get('stats'))
        self.assertEqual(1, response.data['stats'].get('correct_questions'))
        self.assertEqual(1, response.data['stats'].get('total_questions'))
        self.assertEqual(0, response.data['stats'].get('incorrect_questions'))
