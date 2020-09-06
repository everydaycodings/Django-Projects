from django.contrib import admin
from .models import Suscribe, ContactUs, Addpost
from import_export.admin import ImportExportModelAdmin
# Register your models here.

@admin.register(Addpost)
class AddpostAdmin(ImportExportModelAdmin):
   list_display = ("username", "published")

@admin.register(ContactUs)
class VContactUsAdmin(ImportExportModelAdmin):
    list_display = ("name", "email")

admin.site.register(Suscribe)
#admin.site.register(ContactUs)
#admin.site.register(Addpost)