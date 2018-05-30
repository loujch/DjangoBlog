from django.shortcuts import render
from blog.models import BlogsPost


# Create your views here.
def blog_index(request):
    blog_list = BlogsPost.objects.all()  # 获取所有数据
    return render(request,'index.html', {'blog_list':blog_list})   # 返回index.html页面

def blog_about(request):
    blog_list = BlogsPost.objects.all()  # 获取所有数据
    return render(request, 'about.html', {'blog_list':blog_list})   # 返回about.html页面

def blog_contact(request):
    blog_list = BlogsPost.objects.all()  # 获取所有数据
    return render(request, 'contact.html', {'blog_list':blog_list})   # 返回contact.html页面