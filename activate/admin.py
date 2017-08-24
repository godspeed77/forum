from django.contrib import admin
from .models import Activatecode


class ActivateAdmin(admin.ModelAdmin):
    list_display = ("user", "new_code", "expire_timestamp")

admin.site.register(Activatecode,ActivateAdmin)
