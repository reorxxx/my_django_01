from django.contrib import admin
from .models import Task,Plan,Category


# Register your models here.


admin.site.register(Task)
admin.site.register(Plan)
admin.site.register(Category)