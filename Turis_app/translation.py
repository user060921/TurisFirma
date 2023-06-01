from modeltranslation.translator import register, TranslationOptions
from Turis_app.models import *

@register(about)
class aboutTranslationOptions(TranslationOptions):
    fields = ('title','description','title1','description1',)

@register(aboutcarusel)
class aboutcaruselTranslationOptions(TranslationOptions):
    fields = ('name','description',)

@register(service)
class serviceTranslationOptions(TranslationOptions):
    fields = ('name','description','country',)


@register(packages)
class packagesTranslationOptions(TranslationOptions):
    fields = ('description','country','data','people','money',)

@register(des)
class desTranslationOptions(TranslationOptions):
    fields = ('percentage','country','percentage1','country1','percentage2','country2','percentage3','country3',)

