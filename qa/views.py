"""QAPP Views.

This file has the views used
for operations in home and
in detail question.
"""

from django.views import generic
from django.views.generic import edit

from models import Question
from forms import QuestionForm, AnswerForm


# Create your views here.


class HomeView(generic.FormView):
    """HomeView

    FormView for question creation
    in home.
    """
    template_name = "home.html"
    form_class = QuestionForm


class DetailQuestionView(generic.DetailView,
                         edit.FormMixin):
    """DetailQuestionView

    DetailView with FormMixin for a question
    deatil with a form for answers creations.
    """
    template_name = "question_detail.html"
    pk_url_kwarg = 'question_id'
    model = Question
    form_class = AnswerForm
    queryset = Question.objects.all()
