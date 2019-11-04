import re

import markdown
from django.shortcuts import render, get_object_or_404
from markdown.extensions.toc import TocExtension
from django.utils.text import slugify


from .models import Task, Category
from .models import Plan


# Create your views here.

def index(request):
    task_list = Task.objects.all().order_by('-create_time')

    return render(request, 'web/index.html', context={'task_list': task_list})


def detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    md = markdown.Markdown(
        extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            TocExtension(slugify=slugify),
                                  ])
    task.body = md.convert(task.body)

    m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
    task.toc = m.group(1) if m is not None else ''

    return render(request, 'web/single.html', context={'task': task})


def archive(request, year, month):
    task_list = Task.objects.filter(create_time__year=year,
                                    create_time__month=month
                                    ).order_by('-create_time')
    return render(request, 'web/index.html', context={'task_list': task_list})


def category(request, pk):
    # 记得在开始部分导入 Category 类
    cate = get_object_or_404(Category, pk=pk)
    task_list = Task.objects.filter(category=cate).order_by('-create_time')
    return render(request, 'web/index.html', context={'task_list': task_list})
