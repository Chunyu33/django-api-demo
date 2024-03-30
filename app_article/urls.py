from django.urls import path

from app_article.views import add_article, modify_article

app_name = 'article'

urlpatterns = [
    path('article/', add_article),
    path('article/<int:art_id>', modify_article)
]
