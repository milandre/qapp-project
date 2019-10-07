"""QAPP Urls.

This file has the urls used
for qa module.
"""
from django.conf.urls import include, url
from api import urls as api_url
import views


urlpatterns = [
    url(r'^api/', include(api_url, namespace='api')),
    url(r'^detail-question/(?P<question_id>[0-9]+)/$',
        views.DetailQuestionView.as_view(), name='detail-question'),
]
