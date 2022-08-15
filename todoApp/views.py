
from rest_framework import viewsets
from .models import Todo
from .serializer import TodoSerializer
# Create your views here.


class TodoView(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
