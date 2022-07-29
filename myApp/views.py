
from re import template

from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from .models import TodoModel
from django.contrib.auth.models import User
# Create your views here.

class TodoView(View):
    def get(self, request):
        todos = TodoModel.objects.all()
        serialized_todo = [model.json() for model in todos]
        return JsonResponse(serialized_todo, safe=False)

    def post(self, request):
        task = request.POST

        user_id = task['userid']
        user = User.objects.get(id = user_id)
        task = task.objects.create(user=user, title=task['title'])

        

