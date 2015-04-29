from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^helloworld/', include('helloworld.urls')),
    url(r'^blog-posts/', include('qa-blog.urls'))
]
