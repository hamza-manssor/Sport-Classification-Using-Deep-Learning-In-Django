from django.urls import path
from pj_sports import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.home,name="home"),
    path('process/', views.process,name="process")
]
