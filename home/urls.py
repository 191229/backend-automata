from django.urls import path
from home.views import homeViews

urlpatterns = [
    path("", homeViews.index, name="home"),
]