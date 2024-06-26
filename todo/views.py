from django.shortcuts import render
from todo.serializers import TodoSerializer
from .models import Todo
from rest_framework import permissions, viewsets

# Create your views here.
class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Todos to be viewed or edited.
    """
    queryset = Todo.objects.all().order_by('created_at')
    serializer_class = TodoSerializer
    permission_classes = [] #permissions.IsAuthenticated