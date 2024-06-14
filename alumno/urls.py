from django.urls import path
from . import views

urlpatterns = [
    path('crud',views.crud,name='crud'),
    path('generos_list',views.genero_list,name='genero_list'),
    path('generos_add',views.genero_add,name='genero_add'),
    path('generos_edit',views.genero_edit,name='genero_edit'),
    path('generos_del',views.genero_del,name='genero_del'),
#print(path),
]