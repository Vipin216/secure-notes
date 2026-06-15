from rest_framework import serializers
from ..models import Notes
from django.contrib.auth.models import User


class NoteSerializer(serializers.ModelSerializer):

    Note = serializers.SerializerMethodField()

    class Meta:
        model = Notes
        fields = '__all__'
        read_only_fields = ['user']
    
    def get_Note(self,obj):
        return obj.decrypted_note


class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(
        write_only = True
    )

    class Meta:
        model = User

        fields = [
            "username",
            "password"
        ]

    def create(self,validated_data):
        user = User.objects.create_user(
            username = validated_data["username"],
            password = validated_data["password"]
        )

        return user




