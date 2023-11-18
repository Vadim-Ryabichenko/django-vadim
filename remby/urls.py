from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('mainapp.urls')),
    path('topics/', include('topicsapp.urls')),
    path('accounts/', include('accountsapp.urls')),
    path('admin/', admin.site.urls),
]
