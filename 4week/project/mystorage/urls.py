from rest_framework.routers import DefaultRouter #router를 기반으로 작성할겁니다.
from django.urls import path, include
from mystorage import views

router = DefaultRouter()
router.register('essay', views.PostViewSet)  #127.0.0.1:8000/essay/ 를 views.py의 PostViewSet함수와 연결
router.register('album', views.ImgViewSet)
router.register('files', views.FileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
