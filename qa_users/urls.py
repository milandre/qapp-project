"""User urls.

This file has the urls used
for user module.
"""
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth import forms

from views import RegisterView

urlpatterns = [
    url(
        r'^login/$', auth_views.login,
        {
            'template_name': 'login.html'
        },
        name='login'
    ),
    url(
        r'^logout/$', auth_views.logout_then_login,
        name='logout'
    ),
    url(r'^register/', RegisterView.as_view(), name='register')
]
