from django.urls import path

from webapp.views import articles_list_view, article_create_view

urlpatterns = [
    path('', articles_list_view),
    path('cat_status/', article_create_view),
]