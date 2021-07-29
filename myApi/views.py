from .models import Family
from rest_framework import viewsets
from .serializers import FamilySerializer
# Create your views here.

class FamilyViewSet(viewsets.ModelViewSet):
    queryset = Family.objects.all().order_by('first_name')
    serializer_class = FamilySerializer
