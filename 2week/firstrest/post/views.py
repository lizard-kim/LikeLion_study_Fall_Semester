from rest_framework import viewsets # what is viewsets?
from .models import Post
from .serializer import PostSerializer

#CBV

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all() # Post model의 모든 것을 가져다 queryset으로 쓰겠다.
    serializer_class = PostSerializer # PostSerializer를 사용하겠다.