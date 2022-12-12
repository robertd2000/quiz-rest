from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import QuizzesSample
from .serializers import QuizSerializer, QuizQuestionsSerializer
from .service import get_quiz_results


class Quiz(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = QuizSerializer
    queryset = QuizzesSample.objects.all()


class QuizQuestions(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = QuizzesSample.objects.all()
    serializer_class = QuizQuestionsSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def send_results(request, pk):
    results = request.data
    result = get_quiz_results(pk, results)

    return Response(result)
