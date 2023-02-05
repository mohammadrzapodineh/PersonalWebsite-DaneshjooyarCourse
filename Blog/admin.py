from django.contrib import admin
from .models import Article
from django.utils.html import format_html


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'get_created_to_jalali', 'active', 'get_updated_to_jalali',  'show_tags', 'show_image')
    date_hierarchy = 'created'
    search_fields = ('title', 'description', 'tags__name')
    list_filter = ('active', 'author')
    empty_value_display = 'خالی'
    list_display_links = ('title',)
    list_editable = ['author', 'active']
    raw_id_fields = ('author',)
    actions = ['de_active_articles', 'active_articles']
    fieldsets = (
        ('اطلاعات اولیه مقاله', {
            'fields': ('title', 'author')
        }),
        ('اطلاعات مهم مقاله', {
            'fields': ('active', 'image', 'tags', 'description'),
        }),
    )

    @admin.display(empty_value='???', description='تگ ها')
    def show_tags(self, obj):
        return format_html(
            '<p></p>'.join([tag.name for tag in obj.tags.all()])
        )

    @admin.display(empty_value='تصویری موجود نیست', description='تصویر مقاله')
    def show_image(self, obj):
        return format_html(
            '<img src={0} width="100" height="100"/>'.format(obj.image.url)
        )


    @admin.action(description='غیرفعال کردن مقالات انتخاب شده')
    def de_active_articles(self, request, queryset):
        queryset.update(active=False)
        self.message_user(request, 'مقالات انتخاب شده با موفقیت غیر فعال شدند')

    @admin.action(description='فعال سازی مقالات انتخاب شده')
    def active_articles(self, request, queryset):
        queryset.update(active=True)
        self.message_user(request, 'مقالات انتخاب شده با موفقیت  فعال شدند')


# admin.site.register(Article, ArticleAdmin)