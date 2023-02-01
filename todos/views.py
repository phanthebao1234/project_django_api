from rest_framework import generics
from django.shortcuts import render
from .models import Todos
from .serializers import TodosSerializer

# Create your views here.
class ListTodo(generics.ListAPIView):
    queryset = Todos.objects.all()
    serializer_class = TodosSerializer
    
class DetailTodo(generics.RetrieveAPIView):
    queryset = Todos.objects.all()
    serializer_class = TodosSerializer
