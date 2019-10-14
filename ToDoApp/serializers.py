from rest_framework import serializers
from .models import Task, ToDoList


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task


class ToDoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoList
