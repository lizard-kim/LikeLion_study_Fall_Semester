from rest_framework import viewsets
from .models import Essay, Album, Files
from .serializers import EssaySerializer, AlbumSerializer, FilesSerializer
from rest_framework.filters import SearchFilter
from rest_framework.parsers import MultiPartParser, FormParser


class PostViewSet(viewsets.ModelViewSet):
    
    queryset = Essay.objects.all()
    serializer_class = EssaySerializer

    filter_backends = [SearchFilter]
    search_fields = ('title', 'body')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        qs = super().get_queryset()

        if self.request.user.is_authenticated:
            qs = qs.filter(author = self.request.user)
        else:
            qs = qs.none()

        return qs

class ImgViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


from rest_framework.response import Response
from rest_framework import status


class FileViewSet(viewsets.ModelViewSet):
    queryset = Files.objects.all()
    serializer_class = FilesSerializer

    parser_classes = (MultiPartParser, FormParser) # 다양한 media파일을 인코딩할 수 있도록 한다.

    # create() -> post()

    def post(self, request, *args, **kwargs): #우리의 입맛대로 post를 새로 정의하자
        serializer = FilesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        else:
            return Response(serializer.error, status=HTTP_400_BAD_REQUEST)