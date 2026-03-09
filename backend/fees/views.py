from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Fee
from .serializers import FeeSerializer

class FeeViewSet(viewsets.ModelViewSet):
    queryset = Fee.objects.all().order_by('-paid_at')
    serializer_class = FeeSerializer
    permission_classes = [IsAuthenticated]
