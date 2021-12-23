from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^hello/', views.hello),
    url(r'^article/(\d+)/', views.viewArticle),
    url(r'^articles/(\d{2})/(\d{4})', views.viewArticles),
]