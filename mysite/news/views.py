from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Articles


def news(request):
    return render(request, 'news/news.html')


class ArticlesDetailView(DetailView):
    model = Articles

