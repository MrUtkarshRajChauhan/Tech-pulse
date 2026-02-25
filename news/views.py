from django.views.generic import ListView
from .models import NewsArticle

class NewsListView(ListView):
    model = NewsArticle
    template_name = 'news/news_list.html'
    context_object_name = 'articles'