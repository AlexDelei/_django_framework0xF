from django.contrib import admin
from .models import Post
from .models import Blog
 # Registering the models we have created in this current app
 # for this case in blog app we have models.py file where we have two models
 # Post and Blog
 # So by doing so we  make it visible on our admins page

class MemberAdmin(admin.ModelAdmin):
    """
    displaying a nice list view
    """
    list_display = ['title', 'author']

admin.site.register(Post, MemberAdmin) # have added it for posts only
admin.site.register(Blog)

