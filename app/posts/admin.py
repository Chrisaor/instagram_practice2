from django.contrib import admin

from posts.models import Post, PostComment

admin.site.register(Post)
admin.site.register(PostComment)