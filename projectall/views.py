# from django.shortcuts import redirect, render
# from rest_framework.permissions import IsAuthenticated
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

