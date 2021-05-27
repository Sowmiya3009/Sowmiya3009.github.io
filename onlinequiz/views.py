from django.shortcuts import render,redirect

# Create your views here.
from django.shortcuts import render
from . import forms,models
# Create your views here.
from .models import *

def home(request):

	return render(request,'home.html')
def index(request):
	exam=Exam.objects.all()
	return render(request,'index.html',{'Exam': exam})

'''if request.method == 'POST':
		question=request.POST.get('question')
		option1=request.POST.get('option1')
		option2=request.POST.get('option2')
		option3=request.POST.get('option3')
		option4=request.POST.get('option4')
		exam=Exam.objects.create(question=question,option1=option1,option2=option2,option3=option3,option4=option4)
		exam.save()'''

  