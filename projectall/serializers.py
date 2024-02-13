from django.forms import ValidationError
from rest_framework import fields,serializers
from django.contrib.auth import get_user_model, authenticate
from .models import AppUser,DailyScrum,ProductBacklog,Subject,Project,Task



class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AppUser
        fields = ['id','username','password','id_student' ,'first_name','last_name']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = AppUser.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.role = "STD"
        user.save()
        return user

    '''def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.id_student = validated_data.get('id_student', instance.id_student)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.save()
        return instance '''   


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
        fields = ['id','product_backlog','task_id','task_name','status']  

#-------------------------------------BacklogsSerializer-----------------------
class BacklogsSerializer(serializers.ModelSerializer):
    task_set = TaskSerializer(many=True, read_only=True)
    class Meta:
        model = ProductBacklog
        fields = ['id','title_product','date_to_do','status','date_done','important','task_set']



#-----------------------ProjectSerializer----------------
class ProjectSerializer(serializers.ModelSerializer):
    members = UserSerializer(many=True, read_only=True)
    productbacklog_set = BacklogsSerializer(many=True, read_only=True) 

    class Meta:
        model = Project
        fields = ['id','members', 'project_name', 'trello_link', 'figma_link','productbacklog_set']

#-------------------------SubjectSerializer----------------------
class SubjectSerializer(serializers.ModelSerializer):
    #project = ProjectSerializer(many=True, read_only=True)
    #teacher = UserSerializer(many=True, read_only=True)
    
    class Meta:
        model = Subject
        fields = ['id', 'subject_name','teacher']


class SubjectWithProjectSerializer(serializers.ModelSerializer):
    project_set = ProjectSerializer(many=True, read_only=True)
    #teacher = UserSerializer(many=True, read_only=True)
    
    class Meta:
        model = Subject
        fields = ['id', 'subject_name','teacher','project_set']



#---------------------------DailyScrumSerializer--------------------------
class DailyScrumSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DailyScrum
        fields = ['student','date','yesterday','today','problem','note','others']