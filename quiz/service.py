from quiz.models import QuizzesSample


def get_quiz_results(pk: int, results: list[str]) -> dict[str, float | int]:
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

    result = {'right_answers': score, 'wrong_answers': total_answers - score, 'total_answers': total_answers,
              'percent_right': score / total_answers * 100,
              'percent_wrong': (total_answers - score) / total_answers * 100}
    return result
