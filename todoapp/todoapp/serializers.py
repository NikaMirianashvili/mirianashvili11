from django.contrib.auth.models import User
from rest_framework import serializers

class usercreateserializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    def create(self, validated_data):
        user = User(
            email = validated_data['email'],
            username = validated_data['username']
        )

        user.set_password(validated_data['password'])
        user.save()
        return user
    
class userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']