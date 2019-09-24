from django.urls import path, include 
from . import views
  
    
urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.Add_Wish.as_view(), name='add'),
    path('<int:pk>/delete', views.Delete_Wish.as_view(), name='delete')
]