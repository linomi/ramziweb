from django.urls import path
from . import views
urlpatterns = [
path("",views.landing,name='landing_page'),
path("posts",views.index,name = 'index_page'),
path("posts/<slug:slug>",views.post_detail,name = 'post_detail_page')
]
