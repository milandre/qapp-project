"""QAPP API Serializers

This file has the objects serializations
for later use in api views.
"""

from django.contrib.auth.models import User
from rest_framework import serializers

from qa.models import (
    Tag,
    Question,
    Answer,
    Comment
)


class UserSerializer(serializers.ModelSerializer):
    """UserSerializer

    ModelSerializer for serialize a User object
    """

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class TagSerializer(serializers.ModelSerializer):
    """TagSerializer

    ModelSerializer for serialize a Tag object
    """

    class Meta:
        model = Tag
        exclude = ('id',)


class QuestionSerializer(serializers.ModelSerializer):
    """QuestionSerializer

    ModelSerializer for serialize a Question object
    """
    author = UserSerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    tags_set = serializers.PrimaryKeyRelatedField(
        source='tags',
        many=True, write_only=True,
        queryset=Tag.objects.all(),
        required=False
    )
    number_answers = serializers.SerializerMethodField()

    class Meta:
        model = Question
        exclude = ('tags_set',)

    def get_number_answers(self, obj):
        """Number of answers in a specific question

        Args:
            obj: Question obj

        Returns:
            Integer with number of answers
        """
        answers = Answer.objects.filter(question=obj)
        return len(answers)


class AnswerSerializer(serializers.ModelSerializer):
    """AnswerSerializer

    ModelSerializer for serialize an Answer object
    """
    author = UserSerializer(read_only=True)
    question = QuestionSerializer(read_only=True)

    class Meta:
        model = Answer
