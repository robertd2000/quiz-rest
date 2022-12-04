from django.urls import path
from .views import Quiz, QuizQuestions, send_results
from django.conf import settings
from django.conf.urls.static import static

app_name = 'quiz'

urlpatterns = [
    path('<int:pk>/results/', send_results, name='send_results'),
    path('<int:pk>/', QuizQuestions.as_view(), name='quiz_questions'),
    path('', Quiz.as_view(), name='quiz'),
]
