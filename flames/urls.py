from django.urls import path
from .views import home,love,data


urlpatterns = [
    path('<str:pk>',home),
    path('',home,name="home"),
    path('letter/',love),
    path('s/<str:pl>',data),
]
