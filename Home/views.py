from django.shortcuts import render
from Sliders.models import Slider
from Resume.models import Skill, Biography, Experience
from Blog.models import Article


def home_page(request):
    sliders = Slider.objects.filter(is_show=True)
    articles = Article.objects.get_active_articles()[:3] # 0 1 2 3 / 0 1 2
    skills = Skill.objects.all()
    bio = Biography.objects.filter(is_active=True).first()
    experience = Experience.objects.first()
    context = {'sliders': sliders, 'skills': skills, 'bio': bio, 'experience': experience, 'articles': articles}
    return render(request, 'Home/index.html', context)
