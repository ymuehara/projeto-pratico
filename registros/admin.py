from django.contrib import admin
from .models import Log


class LogAdmin(admin.ModelAdmin):
    list_display = ('level', 'descricao', 'data', 'origem')
    list_filter = ('ambiente', 'origem')


admin.site.register(Log, LogAdmin)

