from django.contrib import admin
from django.urls import path, include, re_path
from products.views import index
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('products/', include('products.urls', namespace='products')),
    path('users/', include('users.urls', namespace='users')),
    path('api/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/auth', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



