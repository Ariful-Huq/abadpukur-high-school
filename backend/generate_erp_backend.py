# generate_erp_backend.py
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 1. Create apps
apps = [
    "users",
    "students",
    "teachers",
    "routine",
    "attendance",
    "fees",
    "settings_app"
]

for app in apps:
    app_path = os.path.join(BASE_DIR, app)
    if not os.path.exists(app_path):
        os.system(f"python manage.py startapp {app}")
        print(f"Created app: {app}")
    else:
        print(f"App {app} already exists, skipping creation")

# 2. Generate basic models, serializers, viewsets, urls
# For simplicity, write minimal code to each file

files_content = {
    "users/models.py": '''from django.db import models
from django.contrib.auth.models import AbstractUser

class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.name

class User(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)
''',

    "users/serializers.py": '''from rest_framework import serializers
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

    "users/views.py": '''from rest_framework import viewsets
from .models import User, Role
from .serializers import UserSerializer, RoleSerializer

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
''',

    "users/urls.py": '''from rest_framework.routers import DefaultRouter
from .views import UserViewSet, RoleViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'roles', RoleViewSet, basename='role')

urlpatterns = router.urls
'''
}

for path_suffix, content in files_content.items():
    path = os.path.join(BASE_DIR, path_suffix.replace("/", os.sep))
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Written {path_suffix}")

# 3. Create api/v1 urls.py
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

print("✅ Backend scaffold generated successfully! Run migrations next.")