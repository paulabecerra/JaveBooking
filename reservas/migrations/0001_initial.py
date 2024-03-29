# Generated by Django 2.2.3 on 2019-07-30 01:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AvailableSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday')], max_length=50)),
                ('time', models.DateTimeField()),
                ('level', models.CharField(choices=[('Level 1', 'Level 1'), ('Level 1-2', 'Level 1-2'), ('Level 3', 'Level 3'), ('Level 2-3', 'Level 2-3'), ('Level 4', 'Level 4'), ('Level 3-4', 'Level 3-4'), ('Level 5', 'Level 5'), ('Level 4-5', 'Level 4-5'), ('Level 6', 'Level 6'), ('Level 5-6', 'Level 5-6'), ('Level 7', 'Level 7'), ('Level 7-8', 'Level 7-8'), ('Level 8', 'Level 8')], max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StudentBooking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('conversation_club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservas.AvailableSchedule')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
