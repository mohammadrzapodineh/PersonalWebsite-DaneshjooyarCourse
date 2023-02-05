from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from SiteSetting.views import RobotsTxtView
from django.conf.urls.static import static
from Blog.sitemaps import ArticleSitemap

sitemaps = {
    'articles': ArticleSitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Home.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('ContactUs.urls')),
    path('', include('Resume.urls')),
    path('blog/', include('Blog.urls')),
    path('robots.txt', RobotsTxtView.as_view()),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps }, name='django.contrib.sitemaps.views.sitemap')


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
