from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, ClassViewSet, SectionViewSet, AcademicSessionViewSet

router = DefaultRouter()
router.register('students', StudentViewSet, basename='student')
router.register('classes', ClassViewSet, basename='class')
router.register('sections', SectionViewSet, basename='section')
router.register('sessions', AcademicSessionViewSet, basename='session')
urlpatterns = router.urls
