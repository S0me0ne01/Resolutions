from django.contrib import admin
from django.urls import path, include

#Для обработки выгруженных файлов
from django.conf import settings
from django.conf.urls.static import static

app_name = 'resolutions'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
