from taggit.models import Tag
from Blog.models import Article
from Resume.models import CategoryPortfolio
from .models import Setting, SocialMedia


def setting_processor(request):
    setting = Setting.objects.first()
    social_media = SocialMedia.objects.all()
    tags = Tag.objects.all()
    popular_articles = Article.objects.get_hot_articles()
    categories = CategoryPortfolio.objects.all()
    context = {
        'setting': setting,
        'social_media': social_media,
        'tags': tags,
        'popular_articles': popular_articles,
        'categories': categories
    }
    return context