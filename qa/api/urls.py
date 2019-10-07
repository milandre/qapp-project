"""QAPP API Urls.

This file has the urls used
for qa api module.
"""
from django.conf.urls import url

from qa.api import views

# Question views

question_list = views.QuestionViewSet.as_view({
    'get': 'list'
})

question_create = views.QuestionViewSet.as_view({
    'post': 'create'
})

question_detail = views.QuestionViewSet.as_view({
    'get': 'retrieve'
})

question_update = views.QuestionViewSet.as_view({
    'put': 'update',
    'patch': 'partial_update'
})

question_destroy = views.QuestionViewSet.as_view({
    'delete': 'destroy'
})

# Answer views

answer_list = views.AnswerViewSet.as_view({
    'get': 'list'
})

answer_create = views.AnswerViewSet.as_view({
    'post': 'create'
})

answer_detail = views.AnswerViewSet.as_view({
    'get': 'retrieve'
})

answer_update = views.AnswerViewSet.as_view({
    'put': 'update',
    'patch': 'partial_update'
})

answer_destroy = views.AnswerViewSet.as_view({
    'delete': 'destroy'
})

urlpatterns = [
    url(
        r'^create-question/$',
        question_create,
        name='create-question-api'
    ),
    url(
        r'^detail-question/(?P<question_id>[0-9]+)/$',
        question_detail,
        name='detail-question-api'
    ),
    url(
        r'^list-questions/$',
        question_list,
        name='list-questions-api'
    ),
    url(
        r'^list-liked-questions/$',
        views.ListMostLikedQuestionsAPIView.as_view(),
        name='list-liked-questions-api'
    ),
    url(
        r'^list-unanswered-questions/$',
        views.ListUnansweredQuestionsAPIView.as_view(),
        name='list-unanswered-questions-api'
    ),
    url(
        r'^update-question/(?P<question_id>[0-9]+)/$',
        question_update,
        name='update-question-api'
    ),
    url(
        r'^delete-question/(?P<question_id>[0-9]+)/$',
        question_destroy,
        name='delete-question-api'
    ),
    url(
        r'^create-answer/$',
        answer_create,
        name='create-answer-api'
    ),
    url(
        r'^detail-answer/(?P<answer_id>[0-9]+)/$',
        answer_detail,
        name='detail-answer-api'
    ),
    url(
        r'^list-answers/$',
        answer_list,
        name='list-answers-api'
    ),
    url(
        r'^update-answer/(?P<answer_id>[0-9]+)/$',
        answer_update,
        name='update-answer-api'
    ),
    url(
        r'^delete-answer/(?P<answer_id>[0-9]+)/$',
        answer_destroy,
        name='delete-question-api'
    ),
]
