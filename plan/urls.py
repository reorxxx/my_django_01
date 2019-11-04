from django.urls import path

from . import views


app_name = 'plan'

urlpatterns = [
    path('', views.index, name='index'),
    path('plan/<int:pk>/', views.detail, name='detail'),
    path('archives/<int:year>/<int:month>/', views.archive, name='archive'),
    path('category/<int:pk>/', views.category, name='category'),

]