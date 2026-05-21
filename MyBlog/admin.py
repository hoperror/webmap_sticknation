from django.contrib import admin
from .models import Stick, Comment, MapLayer

@admin.register(Stick)
class StickAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish', 'status', 'handling_score', 'is_weaponizable')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    # Attention, j'ai changé 'post' en 'stick' ici aussi
    list_display = ('name', 'stick', 'created', 'active') 
    list_filter = ('active', 'created')
    search_fields = ('name', 'email', 'body')
    
@admin.register(MapLayer)
class MapLayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'geojson_file')