from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication
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


        
#----------------------get project by user-------------
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_user_project(request):
    
    a_object = Project.objects.filter(members__in=[request.user])
    serializer = ProjectSerializer(a_object,many=True)
    return Response(serializer.data,status=status.HTTP_201_CREATED)

#----------------------get subject by user-------------
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_user_subject(request):
    
    a_object = Subject.objects.filter(teacher__in=[request.user])
    serializer = SubjectSerializer(a_object,many=True)
    return Response(serializer.data,status=status.HTTP_201_CREATED)
   
#---------------------remove user----------------
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def student_remove(request,id,pid):
    
    project = Project.objects.get(pk=pid)
    project.members.remove(
            request.user
        )
    return Response(status=status.HTTP_201_CREATED)