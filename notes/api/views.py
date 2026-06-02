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
from rest_framework.decorators import api_view,throttle_classes
from rest_framework.response import Response
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny
)
from rest_framework.decorators import permission_classes
from django.db.models import Q
from .paginator import NotePagination
from .throttles import NoteThrottle
 
@api_view(["GET"])
def api_home(request):
    data={'message':'Hello API'}

    return Response(data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
@throttle_classes([NoteThrottle])
def api_notes(request):
    search = request.query_params.get("search","")
    ordering = request.query_params.get("ordering")
    notes=Notes.objects.filter(
        user=request.user
    )
    if search:
        notes=notes.filter( Q(Title__icontains=search)|Q(Note__icontains=search))
    if ordering:
        notes=notes.order_by(ordering)
    
    paginator = NotePagination()
    result_page=paginator.paginate_queryset(notes,request)

    serializer = NoteSerializer(result_page,many=True)

    return paginator.get_paginated_response(serializer.data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])

def create_note_api(request):
    serializer = NoteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data)
    
    return Response(serializer.errors)

@api_view(["PUT"])
@permission_classes([IsAuthenticated])
@throttle_classes([NoteThrottle])
def edit_note_api(request,id):
    note = get_object_or_404(Notes,id=id,user=request.user)

    serializer = NoteSerializer(note,data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.errors)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_note_api(request,id):
    note = get_object_or_404(Notes,id=id,user=request.user)

    note.delete()

    return Response({
        "message":"Successfully deleted"
    })