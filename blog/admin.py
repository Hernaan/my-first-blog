from django.contrib import admin

from .models import Post

admin.site.register(Post)
#class AdminPost(admin.ModelAdmin):
#		list_display = ["title", "text", "author"]
# 	