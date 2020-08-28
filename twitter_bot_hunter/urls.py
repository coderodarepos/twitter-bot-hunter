from django.contrib import admin
from django.urls import include
from django.urls import path

from rest_framework import routers
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.urlpatterns import format_suffix_patterns

from trends.views import ListTrends

urlpatterns = [
    path('trends/', ListTrends.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
