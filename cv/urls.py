from django.conf.urls import handler404, handler500
from django.contrib import admin
from django.urls import path, include

from pages import views as pages_views
#from django.conf.urls import handler404, handler500

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
]

#handler404 = 'pages.views.error_404'
handler404 = 'pages.views.error_404'
#handler500 = pages_views.error_500


# if settings.DEBUG: # new
#      urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# if settings.DEBUG:
#     urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
              static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



admin.site.site_header = "Techno Brain Group"
admin.site.site_title = "Admin"
admin.site.index_title = "Techno Brain Group"