# generate_full_erp_backend.py
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Apps to create
apps = [
    "users",
    "students",
    "teachers",
    "routine",
    "attendance",
    "fees",
    "settings_app"
]

# 1️⃣ Create apps
for app in apps:
    app_path = os.path.join(BASE_DIR, app)
    if not os.path.exists(app_path):
        os.system(f"python manage.py startapp {app}")
        print(f"Created app: {app}")
    else:
        print(f"App {app} already exists, skipping creation")

# 2️⃣ Define app templates (models, serializers, views, urls)
app_templates = {
    "users": {
        "models.py": '''from django.db import models
from django.contrib.auth.models import AbstractUser

class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.name

class User(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)
''',
        "serializers.py": '''from rest_framework import serializers
from .models import User, Role

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    role_name = serializers.CharField(source='role.name', read_only=True)
    class Meta:
        model = User
        fields = "__all__"
''',
        "views.py": '''from rest_framework import viewsets
from .models import User, Role
from .serializers import UserSerializer, RoleSerializer

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
''',
        "urls.py": '''from rest_framework.routers import DefaultRouter
from .views import UserViewSet, RoleViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'roles', RoleViewSet, basename='role')
urlpatterns = router.urls
'''
    },

    "students": {
        "models.py": '''from django.db import models
from datetime import datetime
from apps.users.models import User

class AcademicSession(models.Model):
    name = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()
    def __str__(self):
        return self.name

class Class(models.Model):
    name = models.CharField(max_length=50)
    school_code = models.CharField(max_length=3, default="ABC")
    def __str__(self):
        return self.name

class Section(models.Model):
    name = models.CharField(max_length=10)
    class_fk = models.ForeignKey(Class, on_delete=models.CASCADE, related_name="sections")
    def __str__(self):
        return f"{self.class_fk.name}-{self.name}"

class Student(models.Model):
    id = models.BigAutoField(primary_key=True)
    student_id = models.CharField(max_length=20, unique=True, db_index=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[("M","Male"),("F","Female")])
    guardian_name = models.CharField(max_length=100, blank=True)
    guardian_contact = models.CharField(max_length=20, blank=True)
    class_fk = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True)
    section_fk = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True)
    session = models.ForeignKey(AcademicSession, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.student_id:
            self.student_id = self.generate_student_id()
        super().save(*args, **kwargs)

    def generate_student_id(self):
        school_code = self.class_fk.school_code if self.class_fk else "ABC"
        year = self.session.start_date.strftime("%y") if self.session else datetime.now().strftime("%y")
        last_student = Student.objects.filter(student_id__startswith=f"{school_code}{year}").order_by("-student_id").first()
        number = int(last_student.student_id[-3:]) + 1 if last_student else 1
        return f"{school_code}{year}{number:03d}"

    def __str__(self):
        return f"{self.student_id} - {self.first_name} {self.last_name}"
''',
        "serializers.py": '''from rest_framework import serializers
from .models import Student, Class, Section, AcademicSession

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = "__all__"

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = "__all__"

class AcademicSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicSession
        fields = "__all__"
''',
        "views.py": '''from rest_framework import viewsets
from .models import Student, Class, Section, AcademicSession
from .serializers import StudentSerializer, ClassSerializer, SectionSerializer, AcademicSessionSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer

class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

class AcademicSessionViewSet(viewsets.ModelViewSet):
    queryset = AcademicSession.objects.all()
    serializer_class = AcademicSessionSerializer
''',
        "urls.py": '''from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, ClassViewSet, SectionViewSet, AcademicSessionViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet, basename='student')
router.register(r'classes', ClassViewSet, basename='class')
router.register(r'sections', SectionViewSet, basename='section')
router.register(r'sessions', AcademicSessionViewSet, basename='session')
urlpatterns = router.urls
'''
    },

    "teachers": {
        "models.py": '''from django.db import models
from apps.users.models import User
from students.models import Class, Section

class Subject(models.Model):
    name = models.CharField(max_length=100)
    class_fk = models.ForeignKey(Class, on_delete=models.CASCADE, related_name="subjects")
    def __str__(self):
        return f"{self.name} ({self.class_fk.name})"

class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    teacher_id = models.CharField(max_length=20, unique=True, db_index=True)
    designation = models.CharField(max_length=100, blank=True)
    contact_number = models.CharField(max_length=20, blank=True)
    subjects = models.ManyToManyField(Subject, blank=True)

    def save(self, *args, **kwargs):
        if not self.teacher_id:
            self.teacher_id = self.generate_teacher_id()
        super().save(*args, **kwargs)

    def generate_teacher_id(self):
        school_code = "ABC"
        last_teacher = TeacherProfile.objects.order_by("-teacher_id").first()
        number = int(last_teacher.teacher_id[-3:]) + 1 if last_teacher else 1
        return f"{school_code}T{number:03d}"

    def __str__(self):
        return f"{self.teacher_id} - {self.user.get_full_name()}"
''',
        "serializers.py": '''from rest_framework import serializers
from .models import TeacherProfile, Subject

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"

class TeacherSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username', read_only=True)
    subjects = SubjectSerializer(many=True, read_only=True)
    class Meta:
        model = TeacherProfile
        fields = "__all__"
''',
        "views.py": '''from rest_framework import viewsets
from .models import TeacherProfile, Subject
from .serializers import TeacherSerializer, SubjectSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = TeacherProfile.objects.all()
    serializer_class = TeacherSerializer

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
''',
        "urls.py": '''from rest_framework.routers import DefaultRouter
from .views import TeacherViewSet, SubjectViewSet

router = DefaultRouter()
router.register(r'teachers', TeacherViewSet, basename='teacher')
router.register(r'subjects', SubjectViewSet, basename='subject')
urlpatterns = router.urls
'''
    }
}

# 3️⃣ Write templates to files
for app, files in app_templates.items():
    for filename, content in files.items():
        path = os.path.join(BASE_DIR, app, filename)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Written {app}/{filename}")

# 4️⃣ Create api/v1 urls.py
api_dir = os.path.join(BASE_DIR, "api", "v1")
os.makedirs(api_dir, exist_ok=True)
api_urls_path = os.path.join(api_dir, "urls.py")
api_urls_content = '''from django.urls import path, include

urlpatterns = [
    path('', include('users.urls')),
    path('', include('students.urls')),
    path('', include('teachers.urls')),
    path('routine/', include('routine.urls')),
    path('attendance/', include('attendance.urls')),
    path('fees/', include('fees.urls')),
    path('settings/', include('settings_app.urls')),
]
'''
with open(api_urls_path, "w", encoding="utf-8") as f:
    f.write(api_urls_content)
print("Created api/v1/urls.py")

print("✅ Full backend scaffold generated! Next, run migrations and create superuser.")