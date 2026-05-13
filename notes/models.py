from django.db import models
from django.contrib.auth.models import User


class Notes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    Title = models.CharField(max_length=20)
    Note = models.TextField()


class Notelog(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    action = models.CharField(max_length=20)
    note_id = models.IntegerField()
    note_title = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)
