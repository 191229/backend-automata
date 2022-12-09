from django.contrib import admin
from django.urls import re_path
from django.conf.urls import include
from lenguajes.views import GetParticiones, GetConjunto, PostConjunto, PostParticion

urlpatterns = [
    re_path(r'particion$', GetParticiones.as_view()),
    re_path(r'conjunto$', GetConjunto.as_view()),
    re_path(r'addConjunto$', PostConjunto.as_view()),
    re_path(r'addParticion$', PostParticion.as_view()),
    re_path('admin/', admin.site.urls),
]
