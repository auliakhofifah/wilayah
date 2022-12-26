from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("artikel/", artikel, name="artikel"),
    path("addartikel/", addArtikel, name="addartikel"),
    path("editartikel/<int:id>", editArtikel, name="editartikel"),
    path("deleteartikel/<int:id>", deleteArtikel, name="deleteartikel"),
    path("logout/", logoutPage, name="logout"),
    path("register/", register, name="register"),
    path("edituser/<int:id>", editUser, name="edituser"),
    path("deleteuser/<int:id>", hapusUsers, name="hapususer"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)