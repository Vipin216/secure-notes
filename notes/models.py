from django.db import models
from django.contrib.auth.models import User
from .utils import encrypt_note, decrypt_note


class Notes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    Title = models.CharField(max_length=20)
    Note = models.TextField()

    def save(self,*args,**kwargs):

        try:
            decrypt_note(self.Note)
        
        except Exception:
            self.Note = encrypt_note(self.Note)

        super().save(*args,**kwargs)

    @property
    def decrypted_note(self):
        return decrypt_note(self.Note)



class Notelog(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    action = models.CharField(max_length=20)
    note_id = models.IntegerField()
    note_title = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)
