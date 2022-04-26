from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Comment


# def index(request):
#     html = 'List o comments:\n\n'
#     for comment in Comment.objects.all():
#         html += comment.title + ' - ' + comment.content + '\n'
#     return HttpResponse(html, content_type='text/plain; charset=utf-8')

# def index(request):
#     template = loader.get_template('index.html')
#     comments = Comment.objects.all()
#     context = {'comments': comments}
#     return HttpResponse(template.render(context, request))

def index(request):
    comments = Comment.objects.all()
    return render(
        request=request,
        template_name='index.html',
        context={'comments': comments}
    )


# Teachers
# Groups
