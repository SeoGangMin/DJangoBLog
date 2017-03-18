from django.core.paginator import Paginator
from django.shortcuts import render
from django.utils import timezone

import json
from django.http import HttpRequest,HttpResponse
from django.http import JsonResponse
from django.core import serializers

from .models import Post
from . import dbutil

from .queries.post import select_post


# Create your views here.
def post_list(request):
    # posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts=Post.objects.all()
    return render(request, 'blog/index.html', {'post_list':posts})

def posts_json(request):
    posts=Post.objects.all()
    data = serializers.serialize("json", posts)
    return HttpResponse(data, content_type='application/json')
    # return HttpResponse(json.dumps(results), content_type="application/json")

# def query_posts(request):
#     sql= select_post()
#     print(sql)
#     rows = dbutil.select_sql(sql, None)
#
#     return render(request, 'blog/post_list.html', {'post_list':rows})

# def index(request):
#     posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#     return render(request, 'blog/index.html', {post_list:posts})
