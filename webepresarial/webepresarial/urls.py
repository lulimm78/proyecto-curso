"""
URL configuration for webepresarial project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from core.sitemaps import StaticViewSitemap
from django.views.generic import TemplateView

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    #path del core
    path('',include('core.urls')),
    #path de services
    path('services/',include('services.urls')),
    #path de rectificados
    path('rectificados/',include('rectificados.urls')),
    #path de blog
    path('blog/',include('blog.urls')),
     # Paths de pages
    path('page/', include('pages.urls')),
     # Paths de coontact
    path('contact/', include('contact.urls')),
    #path del admin
    path('admin/', admin.site.urls),
    #path sitemap para google search
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    #para bing search
    path("BingSiteAuth.xml", TemplateView.as_view(
        template_name="BingSiteAuth.xml", content_type="text/xml"
    )),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)