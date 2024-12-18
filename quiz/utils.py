from .models import QuizSession, Questions
from rest_framework import status


def get_session_or_error(session_id):
    """utility method to get session using session id"""
    if not session_id:
        return (
            {"error": "session_id must be passed in query parameters"},
            status.HTTP_400_BAD_REQUEST,
        )

    try:
        session = QuizSession.objects.get(pk=session_id)
    except QuizSession.DoesNotExist:
        return ({"error": "Quiz session does not exist"}, status.HTTP_400_BAD_REQUEST)
    return session


def get_question_or_error(question_id):
    """utility method to get question using question id"""
    if not question_id:
        return (
            {"error": "question_id must be present in request body"},
            status.HTTP_400_BAD_REQUEST,
        )

    try:
        question = Questions.objects.get(pk=question_id)
    except Questions.DoesNotExist:
        return ({"error": "Questions does not exist"}, status.HTTP_400_BAD_REQUEST)

    return question


def create_quiz_session():
    """utility method to create quiz session"""

    return QuizSession.objects.create()


def prepare_session_stats(session):
    """utility method to prepare quiz session stats"""

    return {
        "session_id": session.id,
        "stats": {
            "total_questions": session.total_questions,
            "correct_questions": session.correct_questions,
            "incorrect_questions": session.incorrect_questions,
        },
    }


def get_random_question_or_error():
    """utility method to fetch random question"""
    try:
        question = Questions.objects.order_by("?").first()
    except Questions.DoesNotExist:
        return ({"error": "Question does not exist"}, status.HTTP_400_BAD_REQUEST)

    if not question:
        return ({"error": "Random question not found"}, status.HTTP_400_BAD_REQUEST)
    return question


def prepare_random_question_data(session, question):
    """utility method to prepare random question data"""

    return {
        "session_id": session.id,
        "question": {
            "question_id": question.id,
            "question_text": question.question_text,
            "options": question.options,
        },
    }

def update_session_progress(session, is_correct):
    """utility method to update session progress using session and is_correct flag"""

    try:
        session.total_questions += 1
        if is_correct:
            session.correct_questions += 1
        else:
            session.incorrect_questions += 1
        session.save()
    except Exception:
        return ({'error':'Cannot update user progress in quiz session'}, status.HTTP_500_INTERNAL_SERVER_ERROR)
    return {"message":"Session successfully Updated."}

def prepare_submit_answer_data(session, question, is_correct):
    """utility method to prepare data for submiting answer"""

    return{
        'session_id':session.id,
        'question_id':question.id,
        'result': 'Correct' if is_correct else 'Incorrect',
        'score': 1 if is_correct else 0
    }