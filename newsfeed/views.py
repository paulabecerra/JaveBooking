from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

#utilities
from django.utils.decorators import method_decorator 

@method_decorator(login_required, name='dispatch')
class NewsFeedView(TemplateView):
    def get(self, request):
        return render(
            request=request,
            template_name='newsfeed/home.html'
        )
