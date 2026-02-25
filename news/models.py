from django.db import models
from tools.models import Tool

class NewsArticle(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    source_url = models.URLField()
    published_date = models.DateField()
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE, related_name='news_articles')

    def __str__(self):
        return self.title