from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

class StaticViewSitemap(Sitemap):
    def items(self):
        return ['home']  # Añade el nombre de tus vistas (ej: 'home', 'contact')

    def location(self, item):
        return reverse(item)
