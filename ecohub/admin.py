from django.contrib import admin

from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.
from .models import NewsCategory, Message, Article, Blog, Project, Fund

class NewsAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Author", {'fields': ["author"]}),
        ("Category", {"fields": ["news_category"]}),
        ("Title/date", {'fields': ["article_title", "published"]}),
        ("Abstract", {'fields': ["summary"]}),
        ("Content", {"fields": ["text"]})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }

class BlogAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Author", {'fields': ["author"]}),
        ("Category", {"fields": ["category"]}),
        ("Title", {'fields': ["title"]}),
        ("Abstract", {'fields': ["abstract"]}),
        ("Content", {"fields": ["content"]})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(mce_attrs={'width': 800})},
        }

class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Owner", {'fields': ["owner"]}),
        ("Category", {'fields': ["category"]}),
        ("Title", {'fields': ["title"]}),
        ("Attachment", {'fields': ["attachment"]}),
        ("Funds", {'fields': ["target_funds", "current_funds"]}),
        ("Abstract", {'fields': ["abstract"]}),
        ("Description", {'fields': ["description"]})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(mce_attrs={'width': 800})},
    }

admin.site.register(NewsCategory)
admin.site.register(Message)
admin.site.register(Article, NewsAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Fund)