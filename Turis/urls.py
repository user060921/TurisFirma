from django.urls import path
from django.contrib import admin
from Turis_app.views import *
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings 
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Turis_app.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]+ i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),
    path('', include('Turis_app.urls')),        
    prefix_default_language=False,
)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
