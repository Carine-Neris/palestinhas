from django.contrib import admin
from .models import Palestras


@admin.register(Palestras)
class PalestrasAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()