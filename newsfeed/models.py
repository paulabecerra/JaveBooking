from django.db import models

class LearningTip(models.Model):
    title = models.CharField(max_length=200)
    tip = models.TextField(max_length=500)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
