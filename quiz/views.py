from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import get_session_or_error, create_quiz_session, prepare_session_stats, get_random_question_or_error, prepare_random_question_data, get_question_or_error, update_session_progress, prepare_submit_answer_data

# Create your views here.
class StartQuizView(APIView):
    """View class for /quiz endpoint"""

    def post(self, request):
        """method to handle post quiz-session request"""
        try:
            session = create_quiz_session()
        except Exception as e:
            return Response({'error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({"session_id": session.id}, status=status.HTTP_201_CREATED)


    def get(self, request):
        """method to handle get quiz-session request"""
        session_id = request.GET.get('session_id')

        session_result = get_session_or_error(session_id=session_id)
        if not isinstance(session_result, tuple):
            session = session_result
        else:
            return Response(session_result[0], status=session_result[1])

        data = prepare_session_stats(session=session)

        return Response(data=data, status=status.HTTP_200_OK)

class RandomQuestionView(APIView):
    """View class for /question/random endpoint"""

    def get(self, request):
        """method to handle get question request"""
        session_id = request.GET.get("session_id")

        session_result = get_session_or_error(session_id=session_id)
        if not isinstance(session_result, tuple):
            session = session_result
        else:
            return Response(session_result[0], status=session_result[1])

        question_result = get_random_question_or_error()
        if not isinstance(question_result, tuple):
            question = question_result
        else:
            return Response(question_result[0], question_result[1])

        data = prepare_random_question_data(session=session, question=question)

        return Response(data=data, status=status.HTTP_200_OK)

class SubmitAnswerView(APIView):
    """view class for /answer endpoint"""

    def post(self, request):
        """method to handle post submit answer request"""
        request_data = request.POST
        session_id = request_data.get('session_id')
        question_id = request_data.get('question_id')
        answer = request_data.get('answer')

        question_result = get_question_or_error(question_id=question_id)
        if not isinstance(question_result, tuple):
            question = question_result
        else:
            return Response(question_result[0], status=question_result[1])

        session_result = get_session_or_error(session_id=session_id)
        if not isinstance(session_result, tuple):
            session = session_result
        else:
            return Response(session_result[0], status=question_result[1])

        if answer in question.options:
            is_correct = True if answer == question.correct_option else False

            update_session_result = update_session_progress(session=session, is_correct=is_correct)
            if isinstance(update_session_progress, tuple):
                return Response(update_session_result[0], status=update_session_result[1])
            else:
                print(update_session_result)

            data = prepare_submit_answer_data(session=session, question=question, is_correct=is_correct)
            return Response(data=data, status=status.HTTP_200_OK)

        return Response({'error':"Answer must match option key: 'A', 'B', 'C', etc."}, status=status.HTTP_400_BAD_REQUEST)