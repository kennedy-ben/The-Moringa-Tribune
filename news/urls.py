import statistics
from django.urls import URLPattern, path,re_path
from . import views
from django.conf import settings


urlpattens=[
     path('',views.welcome,name = 'welcome'),
     path('', views.news_of_day, name = 'newsToday')
]

urlpattens=[
      path('article/(\d+)',views.article,name ='article')
]

urlpattens=[
     path('archives/(\d{4}-\d{2}-\d{2})',views.past_days_news,name = 'pastNews')
     
]
urlpattens=[
     path('search/', views.search_results, name='search_results')
]

if settings.DEBUG:
    URLPattern+= statistics(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)  