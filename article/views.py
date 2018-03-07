from django.shortcuts import render,redirect
from block.models import Block
from .models import Article
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from comment.models import Comment
from .paginate_queryset import paginate_queryset

def article_list(request,block_id):
    page_no = int(request.GET.get("page_no","1"))
    ARTICLE_CNT_1PAGE = 3
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)
    all_articles = Article.objects.filter(block=block,status=0).order_by("-id")
    p = Paginator(all_articles,ARTICLE_CNT_1PAGE)
    page = p.page(page_no)
    
    page_cnt = p.num_pages
    page_links = [i for i in range(page_no-5,page_no+6) if i>0 and i<=page_cnt]
    pre_links = [i for i in range(page_no-5,page_no) if i>0 and i<=page_cnt]
    post_links = [i for i in range(page_no+1,page_no+6) if i>0 and i<=page_cnt]
    current_no = page_no
    previous_link = page_links[0]-1
    previous_page = current_no-1
    next_link = page_links[-1]+1
    next_page = current_no+1
    has_previous = (previous_link>0)
    has_next = (next_link <= page_cnt)
    
    article_objs = page.object_list

    if has_previous > 0 and has_next >0:
        return render(request,"article_list.html",{"articles":article_objs,"b":block,"has_previous":has_previous,"has_next":has_next,"previous_page":previous_page,"next_page":next_page,"page_cnt":page_cnt,"pre_links":pre_links,"post_links":post_links,"current_no":current_no})
    elif has_previous > 0:
        return render(request,"article_list.html",{"articles":article_objs,"b":block,"has_previous":has_previous,"previous_page":previous_page,"pre_links":pre_links,"post_links":post_links,"current_no":current_no})
    elif has_next >0:
        return render(request,"article_list.html",{"articles":article_objs,"b":block,"has_next":has_next,"next_page":next_link,"page_cnt":page_cnt,"pre_links":pre_links,"post_links":post_links,"current_no":current_no})
    else:
        return render(request,"article_list.html",{"articles":article_objs,"b":block,"pre_links":pre_links,"post_links":post_links,"current_no":current_no})

@login_required
def article_create(request,block_id):
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)
    if request.method == "GET":
        create_objs = Article.objects.filter(block=block,status=0).order_by("-id")
        return render(request,"article_create.html",{"article_creater":create_objs,"b":block})
    else:
        title = request.POST["title"].strip()
        content = request.POST["content"].strip()
        if not title or not content:
            return render(request,"article_create.html",{"b":block, "error":"标题和内容都不能为空", "title":title, "content":content})
        if len(title) > 10 or len(content) > 50:
            return render(request,"article_create.html",{"b":block, "error":"标题或内容太长", "title":title, "content":content})
        article = Article(block=block, title=title, content=content, status=0)
        article.save()
        return redirect("/article/list/%s" % block_id)


def article_detail(request,detail_id):
    detail_id = int(detail_id)
    article = Article.objects.get(id=detail_id)
    block_id = article.block
    page_no = int(request.GET.get("page_no","1"))
    all_comment = Comment.objects.filter(article=detail_id,status=0).order_by("-id")
    page_comment,pagination_data = paginate_queryset(all_comment,page_no)
    return render(request,"article_detail.html",{"details":article,"b":block_id,"comments":page_comment,"pagination_data":pagination_data})
