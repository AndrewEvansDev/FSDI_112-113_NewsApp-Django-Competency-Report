from django.contrib import admin
from .models import Article, Comment

class CommentInLine(admin.TabularInline):#or StackedInLine
    model = Comment
    extra = 0

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInLine,
    ]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)

# this registers new app on admin panel