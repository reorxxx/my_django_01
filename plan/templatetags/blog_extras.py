from django import template
from ..models import Task, Category, Plan

register = template.Library()

@register.inclusion_tag('web/inclusions/_recent_posts.html', takes_context=True)
def show_recent_posts(context, num=5):
    return {
        'recent_post_list': Task.objects.all().order_by('-create_time')[:num],
    }

@register.inclusion_tag('web/inclusions/_archives.html', takes_context=True)
def show_archives(context):
    return {
        'date_list': Task.objects.dates('create_time', 'month', order='DESC'),
    }

@register.inclusion_tag('web/inclusions/_categories.html', takes_context=True)
def show_categories(context):
    return {
        'category_list': Category.objects.all(),
    }

# @register.inclusion_tag('plan/inclusions/_tags.html', takes_context=True)
# def show_tags(context):
#     return {
#         'tag_list': Tag.objects.all(),
#     }