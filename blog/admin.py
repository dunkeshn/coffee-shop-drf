from django.contrib import admin
from django.db.models import Count
from django.urls import reverse
from django.utils.html import format_html
from blog.models.post import Post
from blog.models.comment import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name_link', 'likes', 'create_datetime', 'is_changed', )
    list_display_links = ('id', 'full_name_link')
    list_filter = ('is_changed',)
    search_fields = ('text', 'commentator__first_name', 'commentator__last_name', 'commentator__username', )
    #autocomplete_fields = ('commentator', )

    def full_name_link(self, obj):
        link = reverse('admin:auth_user_change', args=[obj.commentator.id])
        return format_html('<a href="{}">{}</a>', link, f'{obj.commentator.first_name} {obj.commentator.last_name}')
    full_name_link.short_description = 'Имя пользователя'

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name_link', 'title', 'likes', 'comments_count', 'create_datetime', )
    list_display_links = ('id', 'full_name_link', 'title', )
    readonly_fields = ('comments', )
    search_fields = ('text', 'title', 'author__first_name', 'author__last_name', 'author__username', )
    #autocomplete_fields = ('author', )

    def full_name_link(self, obj):
        link = reverse('admin:auth_user_change', args=[obj.author.id])
        return format_html('<a href="{}">{}</a>', link, f'{obj.author.first_name} {obj.author.last_name}')
    full_name_link.short_description = 'Имя пользователя'

    def comments_count(self, obj):
        return obj.comments_count
    comments_count.short_description = 'Количество комментариев'

    def get_queryset(self, request):
        queryset = Post.objects.annotate(
            comments_count=Count('comments__id')
        )
        return queryset
