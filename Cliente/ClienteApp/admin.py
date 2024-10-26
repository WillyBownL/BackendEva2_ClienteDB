from django.contrib import admin
from ClienteApp.models import cliente

# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nombre','apellido','fecha_nacimiento','rut','correo','telefono','ciudad']

admin.site.register(cliente,ClienteAdmin)

# admin 123