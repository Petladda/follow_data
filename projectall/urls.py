from django.urls import path
from . import views
from rest_framework.authtoken import views as auth_views

urlpatterns = [
	path('register', views.UserRegister.as_view(), name='register'),
	path('login', auth_views.obtain_auth_token, name='login'),
    path('logout', views.UserLogout.as_view(), name='logout'),
    path('user', views.UserView.as_view(), name='user'),
    path('subject', views.SubjectView.as_view({'get': 'list'}), name='subject'),
    #path('subject/<int:id>', views.SubjectView.as_view(), name='subject/<int:id>'),
    path('project', views.ProjectView.as_view({'get': 'list'}), name='project'),
    path('dailyscrum', views.DailyView.as_view({'get': 'list'}), name='dailyscrum'),
    path('productbacklogs', views.product_backlogs.as_view({'get': 'list'}), name='productbacklogs'),

    path('subject/<int:id>/create', views.create_project,name="create_project"),
    path('subject/<int:id>/project/<int:pid>/join',views.student_join,name='student_join'),
]