#Django
from django.db import models
from django.contrib.auth.models import User

#User models

class Profile(models.Model):
    #This is the user model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    biography = models.TextField(max_length=500, blank=True)
    picture = models.ImageField(
        upload_to='media/',
        default='media/default',
        blank=True,
        null=True)
    is_teacher = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
