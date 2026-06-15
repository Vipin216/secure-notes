from cryptography.fernet import Fernet
from django.conf import settings

fernet = Fernet(settings.ENCRYPTION_KEY)

def encrypt_note(text):
    return fernet.encrypt(text.encode()).decode()

def decrypt_note(text):
    return fernet.decrypt(text.encode()).decode()