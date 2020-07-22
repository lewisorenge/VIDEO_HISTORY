from .models import history
from rest_framework import viewsets
from .serializers import historySerializer

#music viewset
class historyViewSet(viewsets.ModelViewSet):
    queryset = history.objects.all()
    serializer_class = historySerializer
