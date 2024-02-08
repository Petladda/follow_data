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


from .models import AppUser,DailyScrum,ProductBacklogs,Subject
from .serializers import UserSerializer ,DailyScrumSerializer,BacklogsSerializer,UserLoginSerializer,SubjectSerializer,ProjectSerializer
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
        serializer = UserSerializer()
        if serializer.is_valid(raise_exception=True):
            user = serializer.create()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

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



class DailyViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = DailyScrumSerializer
    queryset = DailyScrum.objects.all()






from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes,authentication_classes

from .models import Subject,Project    





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
    else:
        return Response({"message": "You are not authorized to create projects"})



@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def student_join(request,id,pid):
    project = Project.objects.get(pk=pid)
    project.members.add(
            request.user
        )
    return Response({"message" : "OK"})
    #project_id = request.data.get('project_id')
    #if project_id == project :
    #    project.members.add(
    #        request.user
    #    )
    #else:
    #    return Response({"message": "project ID is not match"})
    

class SubjectView(ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = SubjectSerializer

    def get_queryset(self):
        subject = Subject.objects.all() 
        return subject

    

class ProjectView(ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class  = ProjectSerializer

    def get_queryset(self):
        project = Project.objects.all() 
        return project
    


class product_backlogs(ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class  = BacklogsSerializer
    def get_queryset(self):
        backlogs = ProductBacklogs.objects.all() 
        return backlogs
    

class DailyView(ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class  = DailyScrumSerializer
    def get_queryset(self):
        scrum = Project.objects.all() 
        return scrum
    
    def post(self,request):
        serializer = DailyScrumSerializer()
        if serializer.is_valid():
            serializer.save()
        return Response(status=status.HTTP_200_OK)