from django.urls import path
from . import views

urlpatterns = [
    path('', views.animal_items, name='home'),
    path('modules', views.modules, name='modules'),
    path('animal/<int:id>/', views.animal_delete, name='delete-item')
]
