from re import DEBUG
from django.contrib import admin
from django.urls import path, include
import notifications.urls

urlpatterns = [
    path("admin/", admin.site.urls),
    
    path("", include("apps.authentication.urls")),
    path("", include("apps.data.urls")),
    
    path("", include("apps.home.urls")),
    
    path('notifications/', include(notifications.urls, namespace='notifications')),
]

# if DEBUG:
#     urlpatterns += path("__debug__/", include("debug_toolbar.urls")),
