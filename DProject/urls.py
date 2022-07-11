from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name = 'home'),
    path('home/predict/', views.predict, name = 'predict'),
    path('home/predict/result', views.result, name = 'result'),

]
