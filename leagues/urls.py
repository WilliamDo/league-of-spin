from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('table/<int:division_id>', views.table, name='table'),
]