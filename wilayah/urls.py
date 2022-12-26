
from django.contrib import admin
from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),

    path("about/", aboutus,name="about"),
    path("presiden/", presiden,name="presiden"),
    path("blog/", blog,name="blog"),
    path("detail/<int:id>", detailBlog,name="detail"),
    path("provinsi/", provinsi ,name="provinsi"),
    path("login/", loginPage, name="login"),
    # apps
    path("dashboard/", include('blog.urls'))
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)