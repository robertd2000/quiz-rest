from django.db import models


class QuizzesSample(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_questions(self):
        return self.question_set.all()

    class Meta:
        verbose_name = "Тест"
        verbose_name_plural = "Тесты"
        ordering = ['id']


class Question(models.Model):
    title = models.CharField(max_length=255, verbose_name='Вопрос')
    quiz = models.ForeignKey(QuizzesSample, on_delete=models.CASCADE, verbose_name='Набор тестов')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')

    def __str__(self):
        return self.title

    def get_answers(self):
        return self.answer_set.all()

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"


class Answer(models.Model):
    text = models.CharField(max_length=255, verbose_name='Ответ')
    is_right = models.BooleanField(default=False, verbose_name='Правильный')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Вопрос')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')

    def __str__(self):
        return f'Вопрос - {self.question.title}, ответ - {self.text}, правильный - {"да" if self.is_right else "нет"}'

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"
