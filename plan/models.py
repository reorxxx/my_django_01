import markdown
from django.db import models
from django.urls import reverse

# Create your models here.

# 迁移数据库 需要运行 python manage.py makemigrations  和  python manage.py migrate

# 任务
from django.utils import timezone
from django.utils.html import strip_tags


# 标签
class Category(models.Model):
    index = models.IntegerField()
    name = models.CharField(max_length=100)


# 任务
class Task(models.Model):
    # 序号
    index = models.IntegerField()

    # 标题
    title = models.CharField(max_length=100)

    # 分类
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default= 1)

    # 具体内容
    body = models.TextField(blank=True)

    # 摘要
    excerpt = models.CharField(blank=True,max_length=100)

    # 创建时间、更新时间
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()

    #是否重复任务
    is_repeat = models.IntegerField()
    # #重复任务间隔时间
    # repeat_time = models.TimeField(blank=True)

    def __str__(self):
        return self.title

    # 自定义 get_absolute_url 方法
    # 记得从 django.urls 中导入 reverse 函数
    def get_absolute_url(self):
        return reverse('plan:detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        self.modified_time = timezone.now()

        # 首先实例化一个 Markdown 类，用于渲染 body 的文本。
        # 由于摘要并不需要生成文章目录，所以去掉了目录拓展。
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
        ])

        # 先将 Markdown 文本渲染成 HTML 文本
        # strip_tags 去掉 HTML 文本的全部 HTML 标签
        # 从文本摘取前 54 个字符赋给 excerpt
        self.excerpt = strip_tags(md.convert(self.body))[:54]

        super().save(*args, **kwargs)


# # 待办事项
class Plan(models.Model):
    index = models.IntegerField()
    # task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
    # category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    # start_time = models.DateTimeField()
    # end_time = models.DateTimeField()
    # create_time = models.DateTimeField()
    # update_time = models.DateTimeField()
#


