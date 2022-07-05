from django.urls import path
from users.views import Update_user, User_info, login_view, logout_view, register_view

urlpatterns = [
  path('login/', login_view, name ='login'),
  path('logout/', logout_view, name ='logout'),
  path('signup/', register_view, name ='register'),
  path('profile/<int:pk>/', User_info.as_view(), name="user"),
  path('update-user/<int:pk>/', Update_user.as_view(), name="update_user"),
]