from django.shortcuts import render,redirect
from block.models import Block
from article.models import Article
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from comment.models import Comment
from .models import Message
from django.http import HttpResponse
import json

@login_required
def message_list(request):
