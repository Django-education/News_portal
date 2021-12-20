from modeltranslation.translator import register, TranslationOptions
from .models import Post


@register(Post)
class PostTranslationOptions(TranslationOptions):
    """ Класс, группирующий свойства, подлежащие переводу """
    fields = ('title', 'about', 'content', 'author')
