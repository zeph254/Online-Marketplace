from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from core.views import index

urlpatterns = [
    path('admin/', admin.site.urls),  # Correct admin path
    path('', index, name='index'),  # Homepage
    path('core/', include('core.urls')),  # Include core app routes correctly
    path('item/', include('item.urls')),  # Ensure item.urls exists
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
