from django.contrib import admin

# Register your models here.
from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "slug", "created_on")
    list_filter = ("status",)
    search_fields = ["title", "content"]
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, PostAdmin)
