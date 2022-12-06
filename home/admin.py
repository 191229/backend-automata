from django.contrib import admin
from home.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['first','second', 'three', 'fourth']
# Register your models here.
