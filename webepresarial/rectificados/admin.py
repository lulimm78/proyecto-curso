from django.contrib import admin
from .models import Rectificado

# Register your models here.
class RectificadoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Rectificado, RectificadoAdmin)


