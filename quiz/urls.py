from django.urls import path
from .views import StartQuizView, RandomQuestionView, SubmitAnswerView

urlpatterns=[
    path('quiz/', StartQuizView.as_view(), name='quiz'),
    path('question/random/', RandomQuestionView.as_view(), name='random'),
    path('answer/', SubmitAnswerView.as_view(), name='answer'),
]
