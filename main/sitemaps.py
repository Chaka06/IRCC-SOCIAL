from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    """Sitemap pour les pages statiques du site."""

    def items(self):
        return [
            ('home', 1.0, 'daily'),
            ('procedure', 0.9, 'weekly'),
            ('services', 0.9, 'weekly'),
            ('application_form', 0.9, 'weekly'),
            ('contact', 0.8, 'monthly'),
            ('about', 0.7, 'monthly'),
            ('passport_checker', 0.8, 'weekly'),
            ('visa_checker', 0.8, 'weekly'),
        ]

    def location(self, item):
        return reverse(item[0])

    def priority(self, item):
        return item[1]

    def changefreq(self, item):
        return item[2]
