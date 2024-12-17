from django.urls import path
from .views import StartQuizView, GetQuestionView

urlpatterns=[
    path('start-quiz/', StartQuizView.as_view(), name='start-quiz'),
    path('get-question/', GetQuestionView.as_view(), name='get-question'),
]