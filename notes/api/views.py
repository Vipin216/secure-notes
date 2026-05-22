from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import logout,login,authenticate
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
from ..models import Notes,Notelog
from ..forms import NoteForm
from ..models import Notes
from .serializers import NoteSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


 
@api_view(["GET"])
def api_home(request):
    data={'message':'Hello API'}

    return Response(data)


@api_view(["GET"])
@login_required
def api_notes(request):
    notes=Notes.objects.filter(
        user=request.user
    )
    serializer = NoteSerializer(notes,many=True)

    return Response(serializer.data)


@api_view(["POST"])
@login_required

def create_note_api(request):
    serializer = NoteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data)
    
    return Response(serializer.errors)

@api_view(["PUT"])
@login_required
def edit_note_api(request,id):
    note = get_object_or_404(Notes,id=id,user=request.user)

    serializer = NoteSerializer(note,data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.errors)


@api_view(["DELETE"])
@login_required
def delete_note_api(request,id):
    note = get_object_or_404(Notes,id=id,user=request.user)

    note.delete()

    return Response({
        "message":"Successfully deleted"
    })