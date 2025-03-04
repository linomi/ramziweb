from django.contrib import admin
from .models import Post, Author, Tag, Category, Comment

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'slug']
    search_fields = ['name']

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'slug', 'date']
    list_filter = ['category', 'date', 'author']
    search_fields = ['title', 'content']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['author_name', 'post', 'created_at', 'is_active']
    list_filter = ['created_at', 'is_active']
    search_fields = ['author_name', 'author_email', 'content']
    list_editable = ['is_active']

# Register existing models
admin.site.register(Author)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)

# Register new models
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)

