from datetime import datetime 
from django.utils import timezone
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from .serializers import TaskSerializer
from .models import Task
from .permission import TaskAccessPermission

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import permissions

@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def apiOverview(request):
	api_urls = {
		'List':'/task-list/',
		'Detail View':'/task-detail/<str:pk>/',
		'Create':'/task-create/',
		'Update':'/task-update/<str:pk>/',
		'Delete':'/task-delete/<str:pk>/',
		}
	return Response(api_urls)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def taskList(request):
	user = request.user
	status = request.query_params.get("status", None)
	owner_list = Task.objects.filter(author=user).order_by('-id')

	if status:
		result_list = [task for task in owner_list if task.status == status]
		serializer = TaskSerializer(result_list, many=True)
		return Response(serializer.data)

	serializer = TaskSerializer(owner_list, many=True)
	return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def taskDetail(request, pk):
	tasks = Task.objects.get(id=pk)
	if tasks.author.id == request.user.id:
		serializer = TaskSerializer(tasks, many=False)
		return Response(serializer.data)
	else:
		return Response("You have no rights to view details of this task!")


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def taskCreate(request):
	if request.user.id:
		serializer = TaskSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors)


@api_view(['PUT'])
@permission_classes([TaskAccessPermission])
def taskUpdate(request, pk):
	task = Task.objects.get(id=pk)
	if task.author.id == request.user.id:
		serializer = TaskSerializer(instance=task, data=request.data)
		if serializer.is_valid():
			serializer.save()
		return Response(serializer.data)
	else:
		return Response("You have no rights to update this task!")



@api_view(['DELETE'])
@permission_classes([TaskAccessPermission])
def taskDelete(request, pk):
	task = Task.objects.get(id=pk)
	if task.author.id == request.user.id:
		task.delete()
		return Response('Item succsesfully deleted!')
	else:
		return Response("You have no rights to detele this task!")



