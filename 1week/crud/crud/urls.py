from django.contrib import admin
from django.urls import path, include
import classcrud.urls
import classcrud.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', classcrud.views.home, name="home"),
    path('classcrud/', include(classcrud.urls)),
]
