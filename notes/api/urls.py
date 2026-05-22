from django.urls import path
from django.contrib.auth.views import LoginView
from . import views


urlpatterns = [
    path('',views.api_home,name='api_home'),
    path('view/',views.api_notes,name='api_view'),
    path('create/',views.create_note_api,name='api_create'),
    path('delete_api/<int:id>/',views.delete_note_api,name='api_delete'),
    path('edit/<int:id>/',views.edit_note_api,name='api_edit'),
    
    



]