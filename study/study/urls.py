"""study URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.urls import path, include, re_path
from django.conf.urls import include as url_include
from django.views.generic import TemplateView
from rest_framework.authtoken.views import obtain_auth_token
# from . import settings
from .settings import pro as settings
from bookshelf.urls import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bookshelf/', include('bookshelf.urls')),
    # url(r'^api/token/', obtain_auth_token, name='api-token'),
    re_path(r'^api/', url_include(router.urls)),
    re_path(r'^$', TemplateView.as_view(template_name='bookshelf/index.html'))
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
