from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from home.router import router_posts

urlpatterns = [
    path('home/', include(router_posts.urls)),
    path('admin/', admin.site.urls),
]
