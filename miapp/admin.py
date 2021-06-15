from django.contrib import admin
from .models import Article, Category, Mira, Otros, Iglesias, Ascensores, Escaleras, Publicidad, Arquitectura

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Mira)
admin.site.register(Otros)
admin.site.register(Iglesias)
admin.site.register(Ascensores)
admin.site.register(Escaleras)
admin.site.register(Publicidad)
admin.site.register(Arquitectura)

