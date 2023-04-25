from django.urls import path, include
from . import views

urlpatterns = [
    path ('', views.index, name = 'index'),
    path ('homework/', views.homework, name = 'homework'),
    path('<int:pk>/delete', views.DeleteCity.as_view(), name='delete'),

]