from django.contrib import admin
from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^motiongraphics/', include('motiongraphics.urls')),
    url(r'^illustrator/', include('illustrator.urls')),
	url(r'^$', views.index),
]
