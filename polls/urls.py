from django.urls import path

from . import views

# polls URLs

urlpatterns = [
    path('', views.index, name='index'),
    path('test', views.test),
]