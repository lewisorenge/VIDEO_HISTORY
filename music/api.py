from .models import music
from rest_framework import viewsets
from .serializers import musicSerializer

#music viewset
class musicViewSet(viewsets.ModelViewSet):
    queryset = music.objects.all()
    serializer_class = musicSerializer
