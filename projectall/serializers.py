from django.forms import ValidationError
from rest_framework import fields,serializers
from django.contrib.auth import get_user_model, authenticate
from .models import AppUser,DailyScrum,ProductBacklogs,Subject,Project,Tasks



class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AppUser
        fields = ['id','username','password','id_student' ,'first_name','last_name','role']
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
class TasksSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = Tasks
        fields = ['id','product_backlogs','task_id','task_name','status']  

#-------------------------------------BacklogsSerializer-----------------------
class BacklogsSerializer(serializers.ModelSerializer):
    tasks = TasksSerializer(many=True, read_only=True)
    class Meta:
        model = ProductBacklogs
        fields = ['id','title_product','date_to_do','status','date_done','important','tasks']


#-----------------------ProjectSerializer----------------
class ProjectSerializer(serializers.ModelSerializer):
    members = UserSerializer(many=True, read_only=True)
    products = BacklogsSerializer(many=True, read_only=True) 

    class Meta:
        model = Project
        fields = ['id','members', 'project_name', 'trello_link', 'figma_link','products']

#-------------------------SubjectSerializer----------------------
class SubjectSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(many=True, read_only=True)
    #teacher = UserSerializer(many=True, read_only=True)
    
    class Meta:
        model = Subject
        fields = ['id', 'subject_name','teacher','project']



#---------------------------DailyScrumSerializer--------------------------
class DailyScrumSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DailyScrum
        fields = ['student','date','yesterday','today','problem','note','others']