from django.contrib import admin
from django.urls import path, include
from flames import urls


urlpatterns = [
    path('',include(urls)),
    path('admin/', admin.site.urls),
]
