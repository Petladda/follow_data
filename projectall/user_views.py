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


class Test(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ['id','project_name', 'trello_link', 'figma_link']
        

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_user_project(request):
    print(request.user.id)
    #user = AppUser.objects.get(pk=id)
    a_object = Project.objects.filter(members__in=[request.user])
    #a_object = Project.objects.all()
    serializer = ProjectSerializer(a_object,many=True)
    return Response(serializer.data)
    #return Response(f"{len(a_object)} {len(serializer.data)}")

