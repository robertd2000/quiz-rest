from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet, ModelForm

from .models import Question, Answer, QuizzesSample


class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 4


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = '__all__'


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    form = QuestionForm


admin.site.register(Question, QuestionAdmin)
admin.site.register(QuizzesSample)
