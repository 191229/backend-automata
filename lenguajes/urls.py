from django.contrib import admin
from django.urls import re_path
from django.conf.urls import include
from lenguajes.views import GetParticiones

urlpatterns = [
    re_path(r'particion$', GetParticiones.as_view()),
    re_path('admin/', admin.site.urls),
]
