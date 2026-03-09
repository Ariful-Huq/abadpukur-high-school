from rest_framework.routers import DefaultRouter
from .views import ClassRoutineViewSet, PeriodViewSet

router = DefaultRouter()
router.register('routines', ClassRoutineViewSet, basename='routine')
router.register('periods', PeriodViewSet, basename='period')

urlpatterns = router.urls
