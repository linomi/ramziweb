from django.urls import path
from . import views

app_name = 'scholar_prompt'

urlpatterns = [
    path('', views.scholar_view.as_view(), name='index'),
    path('change-cv/', views.change_cv, name='change_cv'),
    path('<slug:slug>/', views.AuthorView.as_view(), name='author')
]