from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path('user', views.addUser),
    path('user/<id>', views.user_views),
]