from django.contrib import admin
from .models import allPosts

# Register your models here.
# admin.site.register(allPosts)
# @admin.register(allPosts)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = (r'home/js/injectscript.js',)

admin.site.register(allPosts, PostAdmin)