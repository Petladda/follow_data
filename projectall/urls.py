from django.urls import path
from . import views,user_views
from rest_framework.authtoken import views as auth_views

urlpatterns = [
	path('register', views.UserRegister.as_view(), name='register'),
	path('login', auth_views.obtain_auth_token, name='login'),
    path('logout', views.UserLogout.as_view(), name='logout'),
    path('user', views.UserView.as_view(), name='user'),

#--------------------------------user with project---------------------------------
    path('user/project', user_views.get_user_project, name='user_projects'),
    path('user/subject', user_views.get_user_subject, name='user_subjects'),
    path('subject/<int:id>/project/<int:pid>/remove',user_views.student_remove,name='student_remove'),
    path('user/stand-up-meeting', user_views.get_user_stand_up_meeting, name='get_user_stand_up_meeting'),

#--------------------------------subject---------------------------------
    path('subject/', views.SubjectView.as_view({'get': 'list'}), name='subject'),
    path('subject-create/', views.create_subject, name='create_subject'),
    path('subject-delete/<int:id>/', views.delete_subject, name='delete_subject'),
    path('subject-update/<int:id>/', views.subject_update, name='subject_update'),
    path('subject/<int:id>/', views.get_subject_with_project, name='get_subject_with_project'),

    path('subject/<int:id>/create', views.create_project,name="create_project"),

#--------------------------------Project---------------------------------
    path('subject/<int:id>/project/<int:pid>/',views.get_proejct_by_id,name='get_project_by_id'),
    path('subject/<int:id>/project/<int:pid>/join',views.student_join,name='student_join'),

    path('subject/<int:id>/project-update/<int:pid>/',views.project_update,name='project-update'),
    path('subject/<int:id>/project-delete/<int:pid>',views.project_delete,name='project_delete'),

#--------------------------------Productbacklog---------------------------------
    path('subject/<int:id>/project/<int:pid>/productbacklog/<int:bid>',views.get_productbacklog_by_bid,name='get_productbacklog_with_task'),
    path('subject/<int:id>/project/<int:pid>/productbacklog-create/',views.backlog_create,name='backlog_create'),

    path('subject/<int:id>/project/<int:pid>/productbacklog-delete/<int:bid>',views.backlog_delete,name='backlog_delete'),
    path('subject/<int:id>/project/<int:pid>/productbacklog-update/<int:bid>',views.backlog_update,name='backlog_update'),
#----------------------------------task-----------------------------------------
    path('subject/<int:id>/project/<int:pid>/productbacklog/<int:bid>/task/<int:tid>',views.get_task,name='get_task'),
    path('subject/<int:id>/project/<int:pid>/productbacklog/<int:bid>/task-create',views.task_create,name='task_create'),

    path('subject/<int:id>/project/<int:pid>/productbacklog/<int:bid>/task-update/<int:tid>',views.task_update,name='task_update'),
    path('subject/<int:id>/project/<int:pid>/productbacklog/<int:bid>/task-delete/<int:tid>',views.task_delete,name='task_delete'),
    

#--------------------------------stand up meeting---------------------------------

    path('stand_up_meeting', views.MeetingView.as_view({'get': 'list'}), name='stand_up_meeting_list'),
    path('subject/<int:id>/project/<int:pid>/stand_up_meeting-create', views.create_stand_up_meeting, name='stand_up_meeting-create'),
    path('stand_up_meeting/<int:did>', views.get_stand_up_meeting, name='get_stand_up_meeting_by_id'),
    path('stand_up_meeting-delete/<int:did>', views.delete_stand_up_meeting, name='delete_stand_up_meeting_by_id'),

]