#Django
from django import forms

#Models
from django.contrib.auth.models import User
from reservas.models import AvailableSchedule

class AvailableSchedule(forms.ModelForm):
    #Available schedules
    DAY_CHOICES = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday')
    )
    LEVEL_CHOICES = (
        ('Level 1', 'Level 1'),
        ('Level 1-2', 'Level 1-2'),
        ('Level 3', 'Level 3'),
        ('Level 2-3', 'Level 2-3'),
        ('Level 4', 'Level 4'),
        ('Level 3-4', 'Level 3-4'),
        ('Level 5', 'Level 5'),
        ('Level 4-5', 'Level 4-5'),
        ('Level 6', 'Level 6'),
        ('Level 5-6', 'Level 5-6'),
        ('Level 7', 'Level 7'),
        ('Level 7-8', 'Level 7-8'),
        ('Level 8', 'Level 8'),
    )
    day = forms.ChoiceField(choices=DAY_CHOICES)
    time = forms.DateTimeField()
    level = forms.ChoiceField(choices=LEVEL_CHOICES)

    class Meta():
        model = AvailableSchedule
        fields = "__all__"
