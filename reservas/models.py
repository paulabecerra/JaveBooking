#Reservas Models

#Django
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class AvailableSchedule(models.Model):
    #Teachers' Available Schedules
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
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.CharField(max_length=50, choices=DAY_CHOICES)
    time = models.DateTimeField(null=False, blank=False)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.teacher.profile.is_teacher:
            super(Model, self).save(*args, **kwargs)
        else:
            raise ValidationError(
                _('El usuario debe ser un profesor para ejecutar esta acción.')
            )


class StudentBooking(models.Model):
    #Students' booked sessions
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    conversation_club = models.ForeignKey(AvailableSchedule, on_delete=models.CASCADE)
    date = models.DateTimeField(null=False, blank=False)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.student.profile.is_teacher:
            super(Model, self).save(*args, **kwargs)
        else:
            raise ValidationError(
                _('El usuario debe ser un estudiante para ejecutar esta acción.')
            )
