from django.shortcuts import render

from student.forms import StudentRegistrationForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            #return redirect('success')  # ลิงก์ไปยังหน้าที่ต้องการหลังจากการลงทะเบียน
    else:
        form = StudentRegistrationForm()