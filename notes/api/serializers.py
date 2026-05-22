from rest_framework import serializers
from ..models import Notes

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = '__all__'
        read_only_fields = ['user']