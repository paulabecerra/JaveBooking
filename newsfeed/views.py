from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class NewsFeedView(TemplateView):
    def get(self, request):
        return render(
            request=request,
            template_name='newsfeed/home.html'
        )
