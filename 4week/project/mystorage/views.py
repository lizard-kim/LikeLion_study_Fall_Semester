from rest_framework import viewsets
from .models import Essay
from .serializers import EssaySerializer


class PostViewSet(viewsets.ModelViewSet):
    
    queryset = Essay.objects.all()
    serializer_class = EssaySerializer
