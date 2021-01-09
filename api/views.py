from django.http.response import JsonResponse
from django.shortcuts import render,redirect
from rest_framework import serializers

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import TaskSerializer
from .models import Task
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    '''overview of api'''
    api_urls={
        'List':'/task-list/',
        'Create':'/task-create/',
    }
    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return redirect(taskList)