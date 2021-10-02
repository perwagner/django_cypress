from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('watchman/', include('watchman.urls')),
    path('', include('apps.frontend.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('apps.users.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('silk/', include('silk.urls', namespace='silk')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
