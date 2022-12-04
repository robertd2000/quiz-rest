from rest_framework.serializers import ModelSerializer
from .models import QuizzesSample, Question, Answer


class QuizSerializer(ModelSerializer):
    class Meta:
        model = QuizzesSample
        fields = ['id', 'title', 'created_at']


class AnswerSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = ['text', 'created_at', 'question']


class QuestionSerializer(ModelSerializer):
    answer_set = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = ['title', 'created_at', 'quiz', 'answer_set']


class QuizQuestionsSerializer(ModelSerializer):
    question_set = QuestionSerializer(many=True)

    class Meta:
        model = QuizzesSample
        fields = ['id', 'title', 'created_at', 'question_set']


# class ResultSerializer(ModelSerializer):
#     class Meta:
#