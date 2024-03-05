from django.forms import ValidationError
from rest_framework import fields,serializers
from django.contrib.auth import get_user_model, authenticate
from .models import *



class UserSerializer(serializers.ModelSerializer):
    
    role = serializers.CharField(read_only=True)

    class Meta:
        model = AppUser
        fields = ['id','username','password','id_student' ,'first_name','last_name','role']
        extra_kwargs = {'password': {'write_only': True}}
        

        
    #create user role student
    def create(self, validated_data):
        user = AppUser.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.role = "STD"
        user.save()
        return user


    #แก้ไขข้อมูล User
    '''def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.id_student = validated_data.get('id_student', instance.id_student)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.save()
        return instance '''  

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)


class UserLoginSerializer(serializers.Serializer):
	username = serializers.CharField()
	password = serializers.CharField()
	
	def check_user(self, clean_data):
		user = authenticate(username=clean_data['username'], password=clean_data['password'])
		if not user:
			raise ValidationError('user not found')
		return user

    
#--------------------------------------TasksSerializer-------------------
class TaskSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = Task
        fields = ['id','product_backlog','task_id','task_name','id_student','status','date_to_do','date_done','hour_todo','hour_done']  

#-------------------------------------BacklogsSerializer-----------------------
class BacklogsSerializer(serializers.ModelSerializer):
    task_set = TaskSerializer(many=True, read_only=True)
    class Meta:
        model = ProductBacklog
        fields = ['id','title_product','description','date_to_do','status','important','date_done','hour_todo','hour_done','task_set']

#---------------------------DailyScrumSerializer--------------------------
class DailyScrumSerializer(serializers.ModelSerializer):
    student = UserSerializer( read_only=True)
    class Meta:
        model = StandUpMeeting
        fields = ['id','student','subject','project','date','yesterday','today','problem','note','others']

#-----------------------ProjectSerializer----------------
class ProjectSerializer(serializers.ModelSerializer):
    members = UserSerializer(many=True, read_only=True)
    productbacklog_set = BacklogsSerializer(many=True, read_only=True)
    meeting_set = DailyScrumSerializer(many=True, read_only=True) 

    class Meta:
        model = Project
        fields = ['id','members','meeting_set', 'project_name', 'trello_link', 'figma_link','productbacklog_set','meeting_set',]
        

#-------------------------SubjectSerializer----------------------
class SubjectSerializer(serializers.ModelSerializer):
    #project = ProjectSerializer(many=True, read_only=True)
    teacher = UserSerializer( read_only=True)
    
    class Meta:
        model = Subject
        fields = ['id', 'subject_name','teacher']


class SubjectWithProjectSerializer(serializers.ModelSerializer):
    project_set = ProjectSerializer(many=True, read_only=True)
    teacher = UserSerializer( read_only=True)
    
    class Meta:
        model = Subject
        fields = ['id', 'subject_name','teacher','project_set']



