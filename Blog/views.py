from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from random import choices
from django.core.paginator import Paginator
from Comments.models import Comment
from Comments.forms import CommentForm
from django.contrib import messages


def blog_list(request):
    object_list = Article.objects.get_active_articles()
    q = request.GET.get('q')
    if q is not None:
        # object_list = Article.objects.filter(title__icontains=q, description__icontains=q)
        object_list = Article.objects.search(q)
    paginator = Paginator(object_list, 1)
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    context = {
        'articles': articles,
        'q': q,
    }

    return render(request, 'Blog/blog_list.html', context)


def blog_detail(request, blog_id):
    comment_form = CommentForm()
    article = get_object_or_404(Article, id=blog_id, active=True)
    comments = Article.objects.get_active_comments_article(article)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            name = comment_form.cleaned_data.get('name')
            email = comment_form.cleaned_data.get('email')
            text = comment_form.cleaned_data.get('text')
            Comment.objects.create(
                name=name,
                email=email,
                text=text,
                article=article
            )
            messages.add_message(request, messages.SUCCESS, 'کامنت شما با موفقیت ثبت شد دوست عزیز')
            return redirect('Blog:blog_detail', article.id)
        messages.add_message(request, messages.ERROR, 'کامنت شما با موفقیت ثبت نشد دوست عزیز')
    articles = Article.objects.get_active_articles().exclude(id=article.id).distinct()
    if len(articles) > 1:
        random_articles = choices(articles, k=2)
    random_articles = articles
    context = {
        'article': article,
        'random_articles': set(random_articles),
        'comment_form': comment_form,
        'comments': comments

    }

    return render(request, 'Blog/blog_detail.html', context)

# class BlogList(ListView):
#     # model = Article # Article.objects.all()  #object_list
#     queryset = Article.objects.filter(active=True)
#     template_name = 'Blog/blog_list.html'
#     paginate_by = 1 #- >3
#     context_object_name = 'articles'
#


def blog_tag(request, tag_title):
    object_list = Article.objects.get_articles_by_Tag(tag_title)
    paginator = Paginator(object_list, 1)
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    context = {
        'articles': articles,
        'tag_title': tag_title
    }

    return render(request, 'Blog/blog_list.html', context)