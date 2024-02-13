# from django.shortcuts import redirect, render
# from rest_framework import viewsets
# from django.contrib.auth import get_user_model

# from projectall.forms import ProjectGroupForm
# from projectall.models import ProjectGroup
# from .srializers import UserSerializer



# class UserViewSet(viewsets.ModelViewSet):
#     permission_classes = (IsAuthenticated,)
#     serializer_class = UserSerializer
#     queryset = get_user_model().objects.all()


# def create_project_group(request):
#     if request.method == 'POST':
#         form = ProjectGroupForm(request.POST)
#         if form.is_valid():
#             subject = form.cleaned_data['subject']
#             project_count = form.cleaned_data['project_count']

#             # Auto create 
#             for i in range(project_count):
#                 group = ProjectGroup(subject=subject, project_count=i+1)
#                 group.save()

#             #return redirect('success_page')  
#     else:
#         form = ProjectGroupForm()


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes,authentication_classes
from .models import Subject,Project   
from django.shortcuts import get_object_or_404
from .models import AppUser,DailyScrum,ProductBacklog,Subject
from .serializers import *
from rest_framework.permissions import IsAuthenticated ,AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from django.contrib.auth import get_user_model, login, logout
from rest_framework.authtoken.models import Token

#register
class UserRegister(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    

#login	
class UserLogin(APIView):
	permission_classes = (permissions.AllowAny,)

	def post(self, request):
		data = request.data
		serializer = UserLoginSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			user = serializer.check_user(data)
			token = Token.objects.create(user=user)
			return Response(serializer.data, status=status.HTTP_200_OK)

#logout
class UserLogout(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()
    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)
    
#userview
class UserView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response({'user': serializer.data}, status=status.HTTP_200_OK)


class UserViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = AppUser.objects.all()




#------------------------------task------------------------
@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_task(request,id,pid,bid,tid):
    tasks = Task.objects.get(pk=tid)
    serializer = TaskSerializer(tasks)
    return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def task_create(request,id,pid,bid):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
@authentication_classes([])
@permission_classes([])
def task_update(request,id,pid,bid,tid):
    tasks = Task.objects.get(pk=tid)
    serializer = TaskSerializer(instance=tasks,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)


@api_view(['DELETE'])
@authentication_classes([])
@permission_classes([])
def task_delete(request,id,pid,bid,tid):
    tasks = Task.objects.get(pk=tid)
    tasks.delete()
    return Response("delete succsesfully!!!!")


#------------------------------backlog----------------------
@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_productbacklog_by_bid(request,id,pid,bid):
    a_object = ProductBacklog.objects.get(pk=bid)
    serializer = BacklogsSerializer(a_object)
    return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def backlog_create(request,id,pid):
    count = request.data.get('count')
    project = Project.objects.get(pk=pid)
    #serializer = BacklogsSerializer(data=request.data)
    for i in range(count) :
            backlog = ProductBacklog.objects.create(
                project=project,
                title_product="product backlog",
                status=False
            )
            backlog.save()


@api_view(['PUT'])
@authentication_classes([])
@permission_classes([])
def backlog_update(request,id,pid,bid):
    backlogs = ProductBacklog.objects.get(pk=bid)
    serializer = BacklogsSerializer(instance=backlogs,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)


@api_view(['DELETE'])
@authentication_classes([])
@permission_classes([])
def backlog_delete(request,id,pid,bid):
    backlogs = ProductBacklog.objects.get(pk=bid)
    backlogs.delete()
    return Response("delete succsesfully!!!!")

#---------------------------------project------------------------
@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_proejct_by_id(request,id,pid):
    
    a_object = Project.objects.get(pk=pid)
    serializer = ProjectSerializer(a_object)
    return Response(serializer.data)


#----------------------------------------subject---------------------
class SubjectView(ModelViewSet):
    serializer_class = SubjectSerializer
    def get_queryset(self):
        subject = Subject.objects.all() 
        return subject
    
@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_subject_with_project(request,id):
    
    subject = Subject.objects.get(pk=id)
    serializer = SubjectWithProjectSerializer(subject)
    return Response(serializer.data)

#สร้างวิชา by user ? --------
@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def create_subject(request):
    subject_data = request.data
    subject_data['teacher'] = request.user.id

    serializer = SubjectSerializer(data=subject_data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@authentication_classes([])
@permission_classes([])
def subject_update(request,id):
    subject = Subject.objects.get(pk=id)
    serializer = SubjectSerializer(instance=subject,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)


@api_view(['DELETE'])
@authentication_classes([])
@permission_classes([])
def delete_subject(request,id):
    subject = Subject.objects.get(pk=id)
    subject.delete()
    return Response("delete succsesfully!!!!")



#-------------------------create Project------------------------
@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def create_project(request,id):
    count = request.data.get('count')
    subject = Subject.objects.get(pk=id)
    user = AppUser.objects.get(role='TCH')
    if user.role == 'TCH':
        for i in range(count) :
            project = Project.objects.create(
                subject=subject,
                project_name="group" 
            )
            project.save()
            return Response(status=status.HTTP_201_CREATED)
    else:
        return Response({"message": "You are not authorized to create projects"})


#-----------------------------join user ------------------------------------------------------
@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def student_join(request,pid):
    project = Project.objects.get(pk=pid)
    project.members.add(
            request.user
        )
    return Response({"message" : "OK"})
    
    


#---------------------------------------Daily Scrum--------------------------------
@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_dailyscrum(request,id):
    
    daily = DailyScrum.objects.get(pk=id)
    serializer = DailyScrumSerializer(daily)
    return Response(serializer.data)
