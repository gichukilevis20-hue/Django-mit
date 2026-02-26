from django.core.management.base import BaseCommand
from schoolapp.models import Student

class Command(BaseCommand):
    help = 'Add sample student data to the database'

    def handle(self, *args, **options):
        students_data = [
            {'first_name': 'John', 'last_name': 'Doe', 'age': 20, 'course': 'Computer Science', 'email': 'john.doe@example.com'},
            {'first_name': 'Jane', 'last_name': 'Smith', 'age': 19, 'course': 'Information Technology', 'email': 'jane.smith@example.com'},
            {'first_name': 'Michael', 'last_name': 'Johnson', 'age': 21, 'course': 'Computer Science', 'email': 'michael.johnson@example.com'},
            {'first_name': 'Emily', 'last_name': 'Williams', 'age': 20, 'course': 'Data Science', 'email': 'emily.williams@example.com'},
            {'first_name': 'David', 'last_name': 'Brown', 'age': 22, 'course': 'Software Engineering', 'email': 'david.brown@example.com'},
            {'first_name': 'Sarah', 'last_name': 'Davis', 'age': 19, 'course': 'Information Technology', 'email': 'sarah.davis@example.com'},
        ]
        
        for student_data in students_data:
            student, created = Student.objects.get_or_create(**student_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added student: {student.first_name} {student.last_name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Student already exists: {student.first_name} {student.last_name}'))
        
        self.stdout.write(self.style.SUCCESS('Sample data loading complete!'))
