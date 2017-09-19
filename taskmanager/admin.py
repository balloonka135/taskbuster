# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Profile, Project, Tag


class ProjectInline(admin.TabularInline):
    model = Project
    extra = 0


class TagsInline(admin.TabularInline):
    model = Tag
    extra = 0


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = ("username", "interaction", "_projects", "_tags")
    search_fields = ["user__username"]

    inlines = [
        ProjectInline, TagsInline
    ]

    def _projects(self, obj):
        return obj.projects.all().count()


    def _tags(self, obj):
        return obj.tags.all().count()
