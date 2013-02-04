from blog.models import Post, Image
from django.contrib import admin

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    list_filter = ['published','pub_date']
    search_fields = ['title', 'description', 'content']
    date_hierarchy = 'pub_date'
    save_on_top = True
    prepopulated_fields = {"slug": ("title",)}

class ImageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Post, PostAdmin)
admin.site.register(Image, ImageAdmin)
