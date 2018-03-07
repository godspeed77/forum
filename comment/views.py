from django.shortcuts import render,redirect
from block.models import Block
from article.models import Article
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import Comment
from django.http import HttpResponse
import json

@login_required
def create_comment(request):
    if request.method == "POST":
        article_id = request.POST["article_id"].strip()
        article_id = int(article_id)
        to_comment_id = int(request.POST["to_comment_id"].strip())
        article = Article.objects.get(id=article_id)
        user = request.user
        content = request.POST["content"].strip()
        if to_comment_id != 0:
            to_comment = Comment.objects.get(id=to_comment_id)
        else:
            to_comment = None
        comment = Comment(owner=user, article=article, content=content, to_comment=to_comment, status=0)
        comment.save()
        status = request.POST.get('status')
        msg = request.POST.get('msg')
       
        return HttpResponse(json.dumps({
            "status": status,
            "msg": msg
        }))
