
from django.urls import path
from . import views

urlpattens=[
     path('',views.welcome,name = 'welcome'),
     path('today/', views.news_of_day, name = 'newsToday')
]

urlpattens=[
     path('archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_news,name = 'pastNews')
]
   
