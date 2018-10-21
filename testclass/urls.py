from django.urls import path

from . import views

urlpatterns = [
    path('', views.TestIndexView.as_view(), name='index')
]
