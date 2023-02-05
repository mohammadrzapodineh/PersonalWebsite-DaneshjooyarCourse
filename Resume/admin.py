from django.contrib import admin
from .models import Skill, Biography, Experience, Portfolio, CategoryPortfolio

admin.site.register(Skill)
admin.site.register(CategoryPortfolio)
admin.site.register(Portfolio)
admin.site.register(Biography)
admin.site.register(Experience)
