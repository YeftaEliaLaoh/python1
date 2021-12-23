from django.conf.urls import include, url

#from myapp.urls import myapp

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^myapp/', include('myapp.urls')),

    # ... your url patterns
]