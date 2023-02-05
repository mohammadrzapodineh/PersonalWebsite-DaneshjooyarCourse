from django.urls import path
from .views import portfolio_list, portfolio_by_category_list

app_name = 'Resume'
urlpatterns = [
    path('portfolio/', portfolio_list, name='portfolio_list'),
    path('portfolio/category/<int:category_id>/', portfolio_by_category_list, name='portfolio_category_list'),
]