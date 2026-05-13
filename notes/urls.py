from django.urls import path
from django.contrib.auth.views import LoginView
from . import views


urlpatterns = [
    # path('login/',LoginView.as_view(template_name='notes/login.html')),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('view/',views.views_notes,name='view'),
    path('create/',views.create_note,name='create'),
    path('edit/<int:id>/',views.edit_note,name='edit'),
    path('delete/<int:id>/',views.delete_note,name='delete'),
    path('logs/',views.view_logs,name='logs'),


]