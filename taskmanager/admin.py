# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = ("username", "interaction")
    search_fields = ["user__username"]
