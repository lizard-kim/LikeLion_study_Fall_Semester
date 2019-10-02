from django.shortcuts import render
from django.utils import timezone

from django.urls import reverse_lazy # redirection function
from django.views.generic.list import ListView # show data
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView # add data
from .models import ClassBlog

def home(request):
    return render(request, 'home.html')

class BlogView(ListView): # ListView 클래스를 상속, 객체들의 목록을 가져온다 /  html 템플릿 필요 : 블로그 리스트를 담은 html : (소문자모델)_list.html
    #template_name = 'classcrud/exampleName.html' //템플릿의 html파일 이름을 원하는 것으로 하고 싶을 때 직접 지정하기
    #context_object_name = 'blog_list' //이제 object_list라고 html 에서 불러오는 것이 아닌, blog_list로 불러온다.
    model = ClassBlog # 객체는 모델에서 정의한대로 입력된다.

class BlogCreate(CreateView):    # html : form(입력공간)을 갖고 있는 html : (소문자모델)_form.html
    model = ClassBlog
    fields = ['title', 'body'] # 우리가 수정할 부분
    success_url = reverse_lazy('list') # redirection. list = our url

class BlogDetail(DetailView):   # html : 상세 페이지를 담은 html : (소문자모델)_detail.html
    model = ClassBlog

class BlogUpdate(UpdateView):   # html : form(입력공간)을 갖고 있는 html 필요 : (소문자모델)_form.html
    model = ClassBlog
    fields = ['title', 'body']
    success_url = reverse_lazy('list')

class BlogDelete(DeleteView):   # html : 이거 진짜 지울거야??? 확인메시지 날리는 html : (소문자모델)_confirm_delete.html
    model = ClassBlog
    success_url = reverse_lazy('list')

# html 이름이 정해져 있다. 다르게하려면 추가적인 작업 필요.
# next step : making templates