from django.contrib import admin
from .models import BlogPost


# Register your models here.


class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'overview',
        'created_at',
        'creator'
    )

    search_fields = (
        'title',
        'text'
    )

    list_filter = (
        'creator',
        'created_at'
    )

    readonly_fields = (
        'created_at',
        'updated_at'
    )


admin.site.register(BlogPost, BlogPostAdmin)
