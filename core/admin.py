from django.contrib import admin
from .models import Profile, Valoracion


admin.site.register(Profile)
admin.site.register(Valoracion)


class ValoracionAdmin(admin.ModelAdmin):
    list_display = ('user', 'comentario', 'valoracion', 'creado', 'activo')
    list_filter = ('activo', 'creado', 'editado')
    search_fields = ('user', 'cuento', 'creado')