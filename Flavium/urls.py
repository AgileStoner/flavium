"""Flavium URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header  =  "Flavium administration"
admin.site.site_title  =  "Flavium admin site"
admin.site.index_title  =  "Welcome to Flavium admin site"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/search/', include('search.urls')),
    path('api/bookings/', include('bookings.urls')),
    path('api/accounts/', include('accounts.urls')),
    path('api/venues/', include('venues.urls'), name='venues'),
    path('api/reviews/', include('reviews.urls'), name='reviews'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
