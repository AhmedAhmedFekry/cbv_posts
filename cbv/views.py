from django.shortcuts import render
from django.views.generic.base import TemplateView
from core.models import Post


class Ex2(TemplateView):
    template_name='cbv/temp1.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] =Post.objects.all() 
        return context
    
