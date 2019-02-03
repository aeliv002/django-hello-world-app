from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home-page'),
    path('city/create',views.CreateCity.as_view(), name='city-create'),
    ]
