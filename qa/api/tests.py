"""QAPP Test.

This file has the unit test
for qa api modules operations.
"""

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from qa.models import Question, Answer
from serializers import QuestionSerializer


"""
Question Tests.

Unit tests for create,
list and update a Question
object
"""


class CreateQuestionTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user('pablo')
        self.client.force_authenticate(user=self.user)
        self.data = {'title': 'What is your Name?',
                     'question_text': 'I want to know'
                     }

    def test_can_create_question(self):
        response = self.client.post(reverse('qapp:api:create-question-api'),
                                    self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadQuestionTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user('pablo')
        self.question = Question.objects\
                                .create(author=self.user,
                                        title="Who was first?",
                                        question_text="The chicken or the egg?")
        self.client.force_authenticate(user=self.user)

    def test_can_read_question_list(self):
        response = self.client.get(reverse('qapp:api:list-questions-api'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_question_unans_list(self):
        response = self.client.get(reverse('qapp:api:list-unanswered-questions-api'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_question_liked_list(self):
        response = self.client.get(reverse('qapp:api:list-liked-questions-api'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_question_detail(self):
        response = self.client\
                       .get(reverse('qapp:api:detail-question-api',
                            args=[self.user.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateQuestionTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user('Emma')
        self.client.force_authenticate(user=self.user)
        self.question = Question.objects\
                                .create(author=self.user,
                                        title="Who was first?",
                                        question_text="The chicken or the egg?")
        self.data = QuestionSerializer(self.question).data
        self.data.update({'likes': 1, 'closed': 'true'})

    def test_can_update_question(self):
        response = self.client\
                       .put(reverse('qapp:api:update-question-api',
                            args=[self.question.id]), self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


"""
Answer Tests.

Unit tests for create,
list and update an Answer
object
"""


class CreateAnswerTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user('pablo')
        self.question = Question.objects\
                                .create(author=self.user,
                                        title="Who are you?",
                                        question_text="I want to know")
        self.client.force_authenticate(user=self.user)
        self.data = {'question': self.question.id,
                     'answer_text': 'Im your father'}

    def test_can_create_answer(self):
        response = self.client.post(reverse('qapp:api:create-answer-api'),
                                    self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadAnswerTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user('pablo')
        self.question = Question.objects\
                                .create(author=self.user,
                                        title="Who was first?",
                                        question_text="The chicken or the egg?")
        self.answer = Answer.objects\
                            .create(author=self.user,
                                    question=self.question,
                                    answer_text="Chicken first")
        self.client.force_authenticate(user=self.user)

    def test_can_read_answer_list(self):
        response = self.client.get(reverse('qapp:api:list-answers-api'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_answer_detail(self):
        response = self.client\
                       .get(reverse('qapp:api:detail-answer-api',
                            args=[self.user.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateAnswerTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user('Emma')
        self.client.force_authenticate(user=self.user)
        self.question = Question.objects\
                                .create(author=self.user,
                                        title="Who was first?",
                                        question_text="The chicken or the egg?")
        self.data = QuestionSerializer(self.question).data
        self.data.update({'likes': 1, 'closed': 'true'})

    def test_can_update_question(self):
        response = self.client\
                       .put(reverse('qapp:api:update-question-api',
                            args=[self.question.id]), self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
