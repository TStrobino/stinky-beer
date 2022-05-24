from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from rest_framework.response import Response
from rest_framework import status
import json


class HelloView(View):
    def get(self, request):
        response = {"response": "Welcome to the AstroYiest Internal REST API."}
        return HttpResponse(json.dumps(response, indent=4))