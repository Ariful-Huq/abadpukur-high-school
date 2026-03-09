from rest_framework.routers import DefaultRouter
from .views import TeacherViewSet, SubjectViewSet

router = DefaultRouter()
router.register('teachers', TeacherViewSet, basename='teacher')
router.register('subjects', SubjectViewSet, basename='subject')
urlpatterns = router.urls
