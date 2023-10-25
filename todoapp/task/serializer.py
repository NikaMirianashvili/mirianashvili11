from rest_framework import serializers
from .models import Task, Category

class taskserializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class categoryserializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


        