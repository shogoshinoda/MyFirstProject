from cgitb import handler
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from error_handle import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('boards/', include('boards.urls')),
    path('users/', include('users.urls')),
    path('questions/', include('questions.urls')),
    path('error_handle', include('error_handle.urls')),
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = views.page_not_found
# handler500 = views.server_error