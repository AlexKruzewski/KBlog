from blog.models import Post
from django.contrib import admin

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    list_filter = ['published','pub_date']
    search_fields = ['title', 'description', 'content']
    date_hierarchy = 'pub_date'
    save_on_top = True
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Post, PostAdmin)
