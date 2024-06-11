from django.contrib import admin
from itens.models import Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao', 'raridade','durabilidade','foto']
    search_fields = ['nome']

admin.site.register(Item,ItemAdmin)
