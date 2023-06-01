from django.contrib import admin
from . models import *
from modeltranslation.admin import TranslationAdmin

@admin.register(ContactUs)
class ContactUs(admin.ModelAdmin):
    list_display = ['fullname','email','phone','subject',]

@admin.register(Map)
class Map(admin.ModelAdmin):
    list_display = ['map',]

@admin.register(about)
class aboutAdmin(TranslationAdmin):
    list_display = ['title', 'description',]

@admin.register(aboutcarusel)
class aboutcaruselAdmin(TranslationAdmin):
    list_display = ['name', 'description',]

@admin.register(service)
class serviceAdmin(TranslationAdmin):
    list_display = ['name', 'description',]


@admin.register(packages)
class packagesAdmin(TranslationAdmin):
    list_display = ['country', 'data','people','money','description',]

@admin.register(des)
class desAdmin(TranslationAdmin):
    list_display = ['percentage','country',]





