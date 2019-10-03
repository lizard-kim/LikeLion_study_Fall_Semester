from .models import Post
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__' # make all field serializer
        # fields = ['title', 'body'] make title and body fields serializer 
        read_only_fields = ('title', ) # tuple recommended