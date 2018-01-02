"""etkinlikmi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

# Django
from django.contrib import admin
from django.conf import settings
from django.views.static import serve
from django.conf.urls import url, include

# Local Django
from core.api_views import LoginView


urlpatterns = [
    # Admin
    url(r'^admin/', admin.site.urls),

    # Api
    url(r'^', include('etkinlikmi.api_urls')),

    # Token
    url(r'^auth/login', LoginView.as_view(), name='login'),
    url(r'^auth/', include('djoser.urls.authtoken')),
]
