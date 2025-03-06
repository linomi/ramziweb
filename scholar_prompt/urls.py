from django.urls import path
from . import views

app_name = 'scholar_prompt'

urlpatterns = [
    path('', views.scholar_view.as_view(), name='index'),
]