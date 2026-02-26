from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'course', 'email')
    list_editable = ('age', 'course')
    search_fields = ('first_name', 'last_name', 'email', 'course')
    list_filter = ('course', 'age')
    ordering = ('first_name', 'last_name')
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'age')
        }),
        ('Academic Information', {
            'fields': ('course', 'email')
        }),
    )

admin.site.register(Student, StudentAdmin)

# Customize admin site header
admin.site.site_header = "School Management Admin"
admin.site.site_title = "School Admin"
admin.site.index_title = "Welcome to School Management System"
