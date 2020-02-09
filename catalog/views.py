from django.shortcuts import render
from .models import Course

# Create your views here.
def show_courses(request):
    all_courses = Course.object.fliter()
    return render(request, 'catalog/courses.template.html', {
        'all_courses':all_courses
    })