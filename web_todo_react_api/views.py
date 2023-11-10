from rest_framework import generics
from .data.user import User
from .data.task import Task
from .data.category import Category
from .data.restore_codes import Password_Restoration_Codes
from .serializers import TaskSerializer, UserSerializer, CategorySerializer, Password_Restoration_CodesSerializer


class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer



class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class Password_Restoration_CodesListCreateView(generics.ListCreateAPIView):
    queryset = Password_Restoration_Codes.objects.all()
    serializer_class = Password_Restoration_CodesSerializer

class Password_Restoration_CodesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Password_Restoration_Codes.objects.all()
    serializer_class = Password_Restoration_CodesSerializer

