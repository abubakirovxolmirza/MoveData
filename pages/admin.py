from django.contrib import admin
from .models import Page, Tutorial, Video


class TutorialInline(admin.StackedInline):
    model = Tutorial


class VideoInline(admin.StackedInline):
    model = Video


class PageAdmin(admin.ModelAdmin):
    search_fields = ['title']
    inlines = [
        TutorialInline,
        VideoInline,
    ]


admin.site.register(Page, PageAdmin)
