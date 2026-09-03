from django.contrib import admin
from .models import Post

admin.site.site_header = "🛡 SGnG Mission Control"
admin.site.site_title = "SGnG Admin Portal"
admin.site.index_title = "Strubell Goods & Gear — Admin Dashboard"

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'created_at')
    list_filter = ('status', 'author')
    search_fields = ('title', 'body')
