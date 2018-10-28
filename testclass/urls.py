from django.urls import path

from . import views

urlpatterns = [
    path('', views.TestIndexView.as_view(), name='index'),
    path(
        'factory_method/',
        views.FactoryMethodSample.as_view(),
        name='factory_method'
    ),
    path(
        'abstract_factory/',
        views.AbstractFactorySample.as_view(),
        name='abstract_factory'
    ),
]
