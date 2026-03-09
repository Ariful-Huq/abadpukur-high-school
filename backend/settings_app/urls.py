from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SchoolClassViewSet, SubjectViewSet

router = DefaultRouter()
router.register('classes', SchoolClassViewSet, basename='schoolclass')
router.register('subjects', SubjectViewSet, basename='subject')

urlpatterns = router.urls
