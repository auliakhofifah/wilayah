from django.contrib import admin
from .models import  *
# Register your models here.

class AdminArtikel(admin.ModelAdmin):
    list_display = ["penulis","judul", "konten", "date", "picture"]

admin.site.register(Artikels, AdminArtikel)