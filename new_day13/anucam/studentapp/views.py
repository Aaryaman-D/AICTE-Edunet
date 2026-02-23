from django.shortcuts import render
from .models import Student
from django.http import HttpResponse

# Create your views here.
def index(request):
    students=Student.objects.all()
    page_title="Student Info Page :"
    return render(request,"index.html",
                  {"students":students,
                    "title":page_title}
                  )