from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('mapapp/', include('mapapp.urls')),
    path('admin/', admin.site.urls),
]
