
from django.contrib import admin
from django.urls import path
from .views import TaskListCreateView, TaskDetailView, UserListCreateView, UserDetailView, CategoryListCreateView, CategoryDetailView, Password_Restoration_CodesListCreateView, Password_Restoration_CodesDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', TaskListCreateView.as_view(), name='todo-list-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='todo-detail'),
    path('users/', UserListCreateView.as_view(), name='todo-list-create'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='todo-detail'),
    path('categories/', CategoryListCreateView.as_view(), name='todo-list-create'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='todo-detail'),
    path('restoration_codes/', Password_Restoration_CodesListCreateView.as_view(), name='todo-list-create'),
    path('restoration_codes/<int:pk>/', Password_Restoration_CodesDetailView.as_view(), name='todo-detail'),
]
