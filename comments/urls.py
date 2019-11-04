from django.urls import path

from . import views

app_name = 'comments'
urlpatterns = [
    path('comment/<int:task_pk>/', views.comment, name='comment'),
]