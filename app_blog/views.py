# app_blog/views.py
from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        # Відображає шаблон index.html
        return render(request, 'index.html', context=None)