
from django.urls import path
from django.views.generic import TemplateView
from .views import Ex2
urlpatterns = [
    path('template/', TemplateView.as_view(template_name='cbv/temp.html',
                                           extra_context={'title': 'custom template test'})),
    path('template1/', Ex2.as_view()),

]
