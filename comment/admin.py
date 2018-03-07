from django.contrib import admin
from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ("owner", "article", "content", "to_comment")

admin.site.register(Comment,CommentAdmin)
