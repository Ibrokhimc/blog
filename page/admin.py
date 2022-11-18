from django.contrib import admin

from .models import Articles ,Catelog

@admin.register(Catelog)
class CatelogAmdin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug':['name']}


@admin.register(Articles)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {'slug':['title']}

# Register your models here.
