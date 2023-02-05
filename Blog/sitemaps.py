from django.contrib.sitemaps import Sitemap
from .models import Article


class ArticleSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.9

    def items(self):
        return Article.objects.get_active_articles()

    def lastmod(self, obj):
        return obj.updated

    def location(self, item):
        return item.get_absolute_url