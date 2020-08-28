from django.contrib.auth.models import User
from django.shortcuts import render

import tweepy
from decouple import config
from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework.views import APIView


class ListTrends(APIView):

    def get(self, request, format=None):
                
        auth = tweepy.OAuthHandler(config('API_KEY'), config('API_SECRET_KEY'))
        auth.set_access_token(config('ACCESS_TOKEN'),
                              config('ACCESS_TOKEN_SECRET'))

        api = tweepy.API(auth)
        trends = api.trends_place(id=23424768)[0]['trends']


        return Response(trends)