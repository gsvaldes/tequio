from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

# Create your views here.


class HomeView(View):
    """
    holding view 
    """
    def get(self, request, *args, **kwargs):
        context = {"message": "hello tequio"}
        return render(request, 'core/home.html', context=context)
