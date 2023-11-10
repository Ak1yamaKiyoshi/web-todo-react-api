from rest_framework import serializers
from .data.user import User
from .data.task import Task
from .data.category import Category
from .data.restore_codes import Password_Restoration_Codes


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class Password_Restoration_CodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Password_Restoration_Codes
        fields = '__all__'