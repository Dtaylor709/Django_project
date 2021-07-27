from django.contrib import admin
from .models import NewsStory
# Register your models here.

class NewsStoryAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'title', 'content', 'author', 'image_url']

admin.site.register(NewsStory, NewsStoryAdmin)
