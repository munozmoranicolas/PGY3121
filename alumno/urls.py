from django.urls import path
from . import views

urlpatterns = [
    path('crud',views.crud,name='crud'),
]