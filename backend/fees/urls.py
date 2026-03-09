from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FeeViewSet

router = DefaultRouter()
router.register('fees', FeeViewSet, basename='fee')

urlpatterns = router.urls
