from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .forms import studentForm
from .models import Student
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def index(request):
    students = Student.objects.all()
    return render(request, 'user/index.html', {'students': students})

# c-create-add a record into db
def create_student(request):
    if request.method == 'POST':
        form = studentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student added successfully!')
            return redirect('index')
    else:
        form = studentForm()
    return render(request, 'admin/studentform.html', {'form': form, 'title': 'button: Add Student   '})

# r-read-retrieve a record from db (view-only)
def view_student(request, id):
    student = get_object_or_404(Student, id=id)
    return render(request, 'user/student_detail.html', {'student': student})

# Admin Dashboard - displays all students with management options
def dashboard(request):
    students = Student.objects.all()
    search_query = request.GET.get('search', '')
    
    if search_query:
        students = students.filter(
            Q(id__icontains=search_query) |
            Q(first_name__icontains=search_query) |
            Q(last_name__icontains=search_query)
        )
    
    total_students = Student.objects.count()
    return render(request, 'admin/dashboard.html', {
        'students': students,
        'total_students': total_students,
        'search_query': search_query
    })

# Search Engine
def search(request):
    students = Student.objects.all()
    search_query = request.GET.get('q', '')
    search_filter = request.GET.get('filter', 'all')
    
    if search_query:
        if search_filter == 'id':
            students = students.filter(id__icontains=search_query)
        elif search_filter == 'name':
            students = students.filter(
                Q(first_name__icontains=search_query) |
                Q(last_name__icontains=search_query)
            )
        elif search_filter == 'email':
            students = students.filter(email__icontains=search_query)
        elif search_filter == 'course':
            students = students.filter(course__icontains=search_query)
        else:  # all
            students = students.filter(
                Q(id__icontains=search_query) |
                Q(first_name__icontains=search_query) |
                Q(last_name__icontains=search_query) |
                Q(email__icontains=search_query) |
                Q(course__icontains=search_query)
            )
    
    results_count = students.count()
    
    return render(request, 'user/search.html', {
        'students': students,
        'search_query': search_query,
        'search_filter': search_filter,
        'results_count': results_count
    })

# Error handlers
def page_not_found(request, exception):
    return render(request, '404.html', status=404)

def server_error(request):
    return render(request, '500.html', status=500)
def update_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        form = studentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student updated successfully!')
            return redirect('dashboard')
    else:
        form = studentForm(instance=student)
    return render(request, 'admin/studentform.html', {'form': form, 'title': 'Edit Student'})
def register_user(request):
    form = UserCreationForm()

    return render(request, 'user/register.html', {'form': form})