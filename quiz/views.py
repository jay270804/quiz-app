from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import QuizSession, Questions


# Create your views here.
class StartQuizView(APIView):
    """View class for start-quiz endpoint"""

    def post(self, request):
        """function to handle post quiz-session request"""
        session = QuizSession.objects.create()

        return Response({"session_id": session.id}, status=status.HTTP_201_CREATED)


class GetQuestionView(APIView):
    """View class for get_question endpoint"""

    def get(self, request):
        """function to handle get question request"""
        session_id = request.GET.get("session_id")

        if not session_id:
            return Response(
                {"error": "session_id is required in query parameter"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            session = QuizSession.objects.get(id=session_id)
        except QuizSession.DoesNotExist:
            return Response(
                {"error": "quiz-session does not exist"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            question = Questions.objects.order_by("?").first()
            if question is None:
                return Response(
                    {"error": "random-question is none"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        except Questions.DoesNotExist:
            return Response(
                {"error": "Questions does not exist."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        data = {
            "session_id": session.id,
            "question": {
                "question_id": question.id,
                "question_text": question.question_text,
                "options": question.options,
            },
        }

        return Response(data=data, status=status.HTTP_200_OK)
