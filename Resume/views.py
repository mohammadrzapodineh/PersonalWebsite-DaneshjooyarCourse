from django.shortcuts import render, get_object_or_404
from .models import Portfolio, CategoryPortfolio


def portfolio_list(request):
    portfolios = Portfolio.objects.all()
    context = {
        'portfolios': portfolios,
    }
    return render(request, 'Resume/portfolio_list.html', context)


def portfolio_by_category_list(request, category_id):
    category = get_object_or_404(CategoryPortfolio, id=category_id)
    # category = CategoryPortfolio.objects.get(id=category_id)
    portfolios = category.portfolio_set.all()
    context = {
        'portfolios': portfolios,
        'current_category': category
    }
    return render(request, 'Resume/portfolio_list.html', context)