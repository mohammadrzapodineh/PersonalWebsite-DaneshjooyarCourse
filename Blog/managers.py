from django.db.models import Manager
from django.db.models import Q
from django.db.models import Count


class ArticleManager(Manager):
    def get_active_articles(self):
        return self.get_queryset().filter(active=True)

    def search(self, q):
        return self.get_active_articles().filter(
            Q(title__icontains=q) |
            Q(description__icontains=q)
        )

    def get_active_comments_article(self, article):
        return article.comments.filter(active=True)

    def get_articles_by_Tag(self, tag_title):
        return self.get_active_articles().filter(tags__name__exact=tag_title)

    def get_hot_articles(self):
        return self.get_active_articles().annotate(comment_count=Count('comments')).exclude(comment_count=0).order_by('-comment_count')

    # def get_active_articles(self):
    #     return self.filter(active=True)