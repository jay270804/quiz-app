from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import QuizSession, Questions


# Create your views here.
class StartQuizView(APIView):
    """View class for /quiz endpoint"""

    def post(self, request):
        """function to handle post quiz-session request"""
        try:
            session = QuizSession.objects.create()
        except Exception as e:
            return Response({'error':e},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({"session_id": session.id}, status=status.HTTP_201_CREATED)


class RandomQuestionView(APIView):
    """View class for /question/random endpoint"""

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

class SubmitAnswerView(APIView):
    """view class for /answer endpoint"""

    def post(self, request):
        """method to handle post submit answer request"""
        request_data = request.POST
        session_id = request_data.get('session_id')
        question_id = request_data.get('question_id')
        answer = request_data.get('answer')

        try:
            question = Questions.objects.get(pk=question_id)
            if question is None:
                return Response({'error':'Cannot find question to check answer'}, status=status.HTTP_400_BAD_REQUEST)
        except Questions.DoesNotExist:
            return Response({'error':'Questions does not exists.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            session = QuizSession.objects.get(pk=session_id)
            if session is None:
                return Response({'error':'Cannot find session to update progress'}, status=status.HTTP_400_BAD_REQUEST)
        except Questions.DoesNotExist:
            return Response({'error':'QuizSession does not exists.'}, status=status.HTTP_400_BAD_REQUEST)

        if answer in question.options:
            # session_data = {"total_questions":session.total_questions + 1}
            session.total_questions += 1
            data = {
                'session_id':session.id,
                'question_id':question.id,
            }

            if answer == question.correct_option:
                session.correct_questions += 1

                try:
                    session.save()
                    data['result'] = 'Correct'
                    data['score'] = 1
                except Exception as e:
                    return Response({'error':f'Cannot update user progress in quiz session: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                return Response(data=data, status=status.HTTP_200_OK)
            else:
                session.incorrect_questions += 1
                try:
                    session.save()
                    data['result'] = 'Incorrect'
                    data['score'] = 0
                except Exception:
                    return Response({'error':'Cannot update user progress in quiz session'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                return Response(data=data, status=status.HTTP_200_OK)

        return Response({'error':"Answer must match option key: 'A', 'B', 'C', etc."}, status=status.HTTP_400_BAD_REQUEST)