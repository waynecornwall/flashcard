from django.contrib import admin
from .models import Source, Term, Definition
# Register your models here.


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'media')
    list_filter = ('media',)
    ordering = ('title',)
    search_fields = ('title', 'author')


@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
    list_display = ('word',)
    list_filter = ('word',)
    ordering = ('word',)
    search_fields = ('word',)


@admin.register(Definition)
class DefinitionAdmin(admin.ModelAdmin):
    list_display = ('definition', 'term', 'source', 'ref_point')
    list_filter = ('term', 'source')
    ordering = ('term',)
    search_fields = ('term', 'source')

