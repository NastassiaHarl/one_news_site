from django.urls import path
from . import views
from django.views.generic import ListView, DetailView
from news.models import Articles
from .views import ArticlesDetailView

urlpatterns = [
    path('', ListView.as_view(queryset=Articles.objects.all().order_by("-date")[:20],
    template_name='news/news.html')),
    path('news/<id>', ArticlesDetailView.as_view(model=Articles, template_name='news/new.html')),
    ]


