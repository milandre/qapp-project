"""QAPP API views

This file has the all api
question/answer operations.
"""

from rest_framework import generics, status
from rest_framework import viewsets
from rest_framework.authentication import (
    BasicAuthentication
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from qa.models import (
    Question,
    Answer,
    Comment
)
from permissions import IsOwnerOrReadOnly
from serializers import (
    QuestionSerializer,
    AnswerSerializer
)

# Question Viewset


class QuestionViewSet(viewsets.ModelViewSet):
    """QuestionViewSet

    ModelViewSet for Question objects. Include
    create(), update(), list(), destroy()
    operations
    """

    queryset = Question.objects.all().order_by('-pub_date')
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    lookup_url_kwarg = 'question_id'
    serializer_class = QuestionSerializer

    def create(self, request, *args, **kwargs):
        """Create a Question object.

        Returns:
            A 201 HTTP Response indicating
            the Question creation, otherwise
            an exception raise
        """
        # Serialize the information in request.data
        serializer = self.get_serializer(data=request.data)
        # Check if is valid
        serializer.is_valid(raise_exception=True)

        # If serializer is valid, then save the object
        self.custom_perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data,
                        status=status.HTTP_201_CREATED,
                        headers=headers)

    def custom_perform_create(self, serializer):
        """Perform the save operations.

        Returns:
            A Question creation in database
        """
        # Creates the question
        serializer.save(author=self.request.user)


class ListMostLikedQuestionsAPIView(generics.ListAPIView):
    """ListMostLikedQuestionsAPIView

    ListAPIView for displaying a list of
    most liked questions
    """
    # authentication_classes = ()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Question.objects.filter(likes__gt=0).order_by('-likes')
    serializer_class = QuestionSerializer


class ListUnansweredQuestionsAPIView(generics.ListAPIView):
    """ListUnansweredQuestionsAPIView

    ListAPIView for displaying a list of
    unanswered questions
    """
    # authentication_classes = ()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Question.objects.filter(answers__isnull=True)\
                               .order_by('-pub_date')
    serializer_class = QuestionSerializer


# Answer Viewset

class AnswerViewSet(viewsets.ModelViewSet):
    """AnswerViewSet

    ModelViewSet for Answer objects. Include
    create(), update(), list(), destroy()
    operations
    """

    queryset = Answer.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    lookup_url_kwarg = 'answer_id'
    serializer_class = AnswerSerializer

    def create(self, request, *args, **kwargs):
        """Create an Answer object.

        Returns:
            A 201 HTTP Response indicating
            the Answer creation, otherwise
            an exception raise
        """
        # Getting question id for later asociation with
        # object Answer created
        question_id = request.data['question']
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.custom_perform_create(serializer, question_id)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data,
                        status=status.HTTP_201_CREATED,
                        headers=headers)

    def custom_perform_create(self, serializer, question_id):
        """Perform the save operations.

        Returns:
            A Answer creation in database with the asociated
            Question object
        """
        # Creates the answer
        question = Question.objects.get(id=question_id)
        serializer.save(author=self.request.user, question=question)
