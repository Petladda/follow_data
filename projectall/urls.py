from django.urls import path
from . import views
from rest_framework.authtoken import views as auth_views

urlpatterns = [
	path('register', views.UserRegister.as_view(), name='register'),
	path('login', auth_views.obtain_auth_token, name='login'),
    path('logout', views.UserLogout.as_view(), name='logout'),
    path('user', views.UserView.as_view(), name='user'),


    path('subject/<int:id>/create', views.hello_world,name="create_project"),
]