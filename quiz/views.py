from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import QuizzesSample
from .serializers import QuizSerializer, QuizQuestionsSerializer


class Quiz(generics.ListAPIView):
    serializer_class = QuizSerializer
    queryset = QuizzesSample.objects.all()


class QuizQuestions(generics.RetrieveAPIView):
    queryset = QuizzesSample.objects.all()
    serializer_class = QuizQuestionsSerializer


@api_view(['POST'])
def send_results(request, pk):
    results = request.data
    score = 0

    questions = QuizzesSample.objects.get(pk=pk)
    correct_answers = []

    for question in questions.get_questions():
        answers = []
        for answer in question.get_answers():
            answers.append({"text": answer.text, "is_right": answer.is_right})
        correct_answers.append(answers)

    total_answers = len(correct_answers)
    for i in range(total_answers):
        answer = next(item for item in correct_answers[i] if item["text"] == results[i])
        if answer.get('is_right'):
            score += 1

    # ["1914", "1453"]
    return Response(
        {'right_answers': score, 'wrong_answers': total_answers - score, 'total_answers': total_answers,
         'percent_right': score / total_answers * 100,
         'percent_wrong': (total_answers - score) / total_answers * 100})

# [
#     [
#         {
#             "text": "1911",
#             "is_right": false
#         },
#         {
#             "text": "1914",
#             "is_right": true
#         },
#         {
#             "text": "1916",
#             "is_right": false
#         },
#         {
#             "text": "1918",
#             "is_right": false
#         }
#     ],
#     [
#         {
#             "text": "1453",
#             "is_right": true
#         },
#         {
#             "text": "1463",
#             "is_right": false
#         },
#         {
#             "text": "1550",
#             "is_right": false
#         },
#         {
#             "text": "1600",
#             "is_right": false
#         }
#     ]
# ]
