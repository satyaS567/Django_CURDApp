from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('create',views.create,name='create'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('search',views.search,name='search')
]