from django.urls import re_path as url
from django.contrib import admin
from polls import views
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    url(r'', include('blog.urls')),
    path('admin/', admin.site.urls),
    #path('', views.IndexView.as_view(), name='index'),
]