from django import template

from comments.forms import CommentForm

register = template.Library()


@register.inclusion_tag('comments/_form.html', takes_context=True)
def show_comment_form(context, task, form=None):
    if form is None:
        form = CommentForm()
    return {
        'form': form,
        'task': task,
    }


@register.inclusion_tag('comments/_list.html', takes_context=True)
def show_comments(context, task):
    comment_list = task.comment_set.all().order_by('-created_time')
    comment_count = comment_list.count()
    return {
        'comment_count': comment_count,
        'comment_list': comment_list,
    }