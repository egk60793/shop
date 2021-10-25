from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from mianapp.models import CartProduct


class Test(View):
    def get(self, request):

        return JsonResponse("asd", {"":""})