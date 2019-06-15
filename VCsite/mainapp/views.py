from django.shortcuts import render, reverse
from django.utils import timezone
from django.http import HttpResponseRedirect
from .models import Comment
# Create your views here.


def index(request):
    return render(request, 'mainapp/index.html')


def video(request):
    return render(request, 'mainapp/video.html')


def detail(request):

    return render(request, "mainapp/detail.html")

def redirect(request):

    data = request.POST.get('comment')
    comment = Comment()

    comment.comment_text = data
    comment.pub_date = timezone.now()
    comment.save()

    comment_list = Comment.objects.all().order_by('-pub_date')[:5]

    return render(request, 'mainapp/detail.html', {'comment_list':comment_list})

