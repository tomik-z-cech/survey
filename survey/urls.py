# surveysite/urls.py
from django.contrib import admin
from django.urls import path, include
from survey.views import SurveyView

urlpatterns = [
    path('', SurveyView.as_view(), name='survey'),
]