from django.urls import path
from website import views

app_name="website" 

urlpatterns = [
  
  path('home/',views.home,name='home'),
  # path('login/', views.login_user,name='login'),
   path('logout/', views.logout_user,name='logout'),
   path('register/', views.register_user,name='register'),
  
    
   
]