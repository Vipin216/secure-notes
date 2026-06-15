from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import logout,login,authenticate
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
from .models import Notes,Notelog
from .forms import NoteForm
from .models import Notes
from .api.serializers import NoteSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


 
@login_required
def views_notes(request):
    search_query = request.GET.get('search')
    notes = Notes.objects.filter(user=request.user)
    if search_query:
        notes = notes.filter(Q(Title__icontains=search_query))
    
    notes.order_by('-id')
    paginator = Paginator(notes,2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'notes/view.html',{'page_obj':page_obj,'search_query':search_query})


@login_required
def logout_view(request):
    if request.method=="POST":
        logout(request)
        return redirect('login')
    
    return render(request,'notes/logout.html')
    
    

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username = username,password=password)

        if user is not None:
            login(request,user)
            return redirect('view')
        else:
            return render(request,'notes/login.html',{'error':'Invalid credential'})
        
    return render(request,'notes/login.html')


@login_required
def create_note(request):
    if request.method == "POST":
        form = NoteForm(request.POST)

        if form.is_valid():
            

            note = form.save(commit=False)

            note.user = request.user

            note.save()



            Notelog.objects.create(
                user = note.user,
                action="CREATED",
                note_id = note.id,
                note_title = note.Title,

            )
            

            return redirect('view')
    else:
        form = NoteForm()

    
    return render(request,'notes/create.html',{'form':form})


@login_required

def edit_note(request,id):
    # note = Notes.objects.get(id=id)
    # if note.user != request.user:
    #     return redirect('/notes/view')


    # note = Notes.objects.filter(id=id,user=request.user).first()
    # if note == None:
    #     return redirect('/note/view')


    note = get_object_or_404(Notes,id=id,user=request.user)
    

    if request.method == "POST":
        form = NoteForm(request.POST,instance=note)

        if form.is_valid():
            form.save()

            Notelog.objects.create(
                user = note.user,
                note_id = note.id,
                note_title = note.Title,
                action = "EDITED",
            )
            return redirect('view')        


    else:
        note.Note = note.decrypted_note
        form = NoteForm(instance=note)
    
    return render(request,'notes/edit.html',{'form':form})


@login_required

def delete_note(request,id):
    # note = Notes.objects.get(id=id)
    # if note.user != request.user:
    #     return redirect('/notes/view')


    # note = Notes.objects.filter(id=id,user=request.user).first()
    # if note == None:
    #     return redirect('/note/view')

    
    note = get_object_or_404(Notes,id=id,user=request.user)



    if request.method == "POST":
        Notelog.objects.create(
            user = note.user,
            action = "DELETED",
            note_id = note.id,
            note_title = note.Title,

        )
        note.delete()
        return redirect('view')
    
    
    return render(request,'notes/delete.html',{'note':note})



@login_required
def view_logs(request):
    logs = Notelog.objects.filter(user=request.user).order_by('-timestamp')
    return render(request,'notes/logs.html',{'logs':logs})



    


