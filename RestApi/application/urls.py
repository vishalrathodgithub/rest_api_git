from application import views
from django.urls import path

urlpatterns = [
    path('home/', views.home),
    path('showdata/',views.ShowEmployee),
    path('data',views.Table),
]
