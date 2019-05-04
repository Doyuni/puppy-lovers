from django.contrib import admin
from community.models import Post, Review, Comment
# Register your models here.

# admin.site.register(Comment)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'author_name', 'created_at', 'hits')
    
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('reviewable_type', 'reviewable_name', 'title', 'description', 'score')
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('commentable_type', 'commentable_id', 'text', 'author_name')