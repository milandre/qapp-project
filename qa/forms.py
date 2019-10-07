"""QAPP forms.

This file has the  forms used
for qa module.
"""
from django import forms

from models import Question, Answer

# User Register


class QuestionForm(forms.ModelForm):
    """QuestionForm

    A ModelForm for question creation
    """

    class Meta:
        model = Question
        exclude = ('author',
                   'closed',
                   'pub_date',
                   'likes',
                   'last_update')


class AnswerForm(forms.ModelForm):
    """AnswerForm

    A ModelForm for answer creation
    """

    class Meta:
        model = Answer
        exclude = ('author',
                   'question',
                   'checked',
                   'pub_date',
                   'likes',
                   'last_update')
        labels = {
            'answer_text': ''
        }
