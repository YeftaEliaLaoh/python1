from django.conf.urls import include, url

from myapp.views import hello

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/', hello, name = 'hello'),

    # ... your url patterns
]