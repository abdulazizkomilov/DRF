from rest_framework import serializers
from .models import Note
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']



class NoteSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    class Meta:
        model = Note
        fields = ['id', 'author', 'name', 'body', 'created', 'created_format',]
