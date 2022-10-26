from django.contrib import admin
from .models import SocialPost, Comment


class CommentInline(admin.TabularInline):
    model = Comment

class SocialPostAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]


admin.site.register(SocialPost, SocialPostAdmin)
admin.site.register(Comment)