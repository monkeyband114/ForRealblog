from django.contrib import admin
from .models import Tags, Blogpost, Images, CommentChat


admin.site.register(Tags)
admin.site.register(Blogpost)
admin.site.register(Images)
admin.site.register(CommentChat)