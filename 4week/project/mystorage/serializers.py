from .models import Essay, Album, Files
from rest_framework import serializers
from rest_framework.parsers import MultiPartParser, FormParser

class EssaySerializer(serializers.ModelSerializer):

    author_name = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Essay
        fields = ('pk', 'title', 'body', 'author_name')


class AlbumSerializer(serializers.ModelSerializer):

    author_name = serializers.ReadOnlyField(source='author.username')
    image = serializers.ImageField(use_url=True)

from rest_framework.response import Response
from rest_framework import status


class FilesSerializer(serializers.ModelSerializer):

    author_name = serializers.ReadOnlyField(source='author.username')
    myfiles = serializers.FileField(use_url=True)

    parser_classes = (MultiPartParser, FormParser)

    #create() 오버라이딩
    
    def post(self, request, *args, **kwargs):
        serializer = FilesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        else:
            return Response(serializer.error, status=HTTP_400_BAD_REQUEST)