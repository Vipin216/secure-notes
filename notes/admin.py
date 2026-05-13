from django.contrib import admin
from .models import Notes,Notelog

admin.site.register(Notes)

# Register your models here.
@admin.register(Notelog)
class NoteLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'action', 'note_id', 'note_title', 'timestamp')
    list_filter = ('action', 'timestamp')
    search_fields = ('user__username', 'note_id', 'note_title')