from django.conf.urls import include, url
from django.views.generic import ListView
from . import views

urlpatterns = [
    url(r'^hello/', views.hello),
    url(r'^article/(\d+)/', views.viewArticle),
    url(r'^articles/(\d{2})/(\d{4})', views.viewArticles),
    url(r'^redirect/', views.redirectTest),
    url(r'^dreamreals/', ListView.as_view(model = Dreamreal, 
      template_name = "dreamreal_list.html")),
]