# crete urls.py in forms_app

from django.urls import path
from .import views

urlpatterns = [
    path('', views.form_name_view, name='form_name'),

]