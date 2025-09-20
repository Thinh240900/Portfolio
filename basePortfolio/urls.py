from django.urls import path

from basePortfolio import views

app_name = "basePortfolio"

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('health', views.health)
]