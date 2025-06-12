from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Round

class IndexView(generic.ListView):
    template_name = 'scorecard/index.html'
    context_object_name = 'round_list'

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Round.objects.filter(user=user).order_by('-date')
        else:
            return Round.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
