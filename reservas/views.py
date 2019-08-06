#Django
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

#Utilities
from django.utils.decorators import method_decorator
from django.core.exceptions import ValidationError

#Forms
from reservas.forms import AvailableSchedule

@method_decorator(login_required, name='dispatch')
class TeacherSchedule(TemplateView):
    template_name = 'schedules.html'
    def post(self, request):
        form = AvailableSchedule(request.POST)
        if form.is_valid():
            form.save()
            return redirect('newsfeed:home')
        else:
            raise ValidationError('El formato no es válido')

    def get(self, request):
        form = AvailableSchedule()
        return render(
            request=request,
            template_name='reservas/schedules.html'
        )
