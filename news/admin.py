from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Post


@admin.register(Post)
class PostAdmin(TranslationAdmin):
    """ Класс регистрации модели постов в админке """
    list_display = ('title', 'about', 'content', 'author', 'publish', 'source')
    list_display_links = ('title',)

