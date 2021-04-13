from django.contrib import admin
from .models import Source, Term
# Register your models here.


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'media')
    list_filter = ('media',)
    ordering = ('title',)
    search_fields = ('title', 'author')


@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
    # term = Term()
    # definition = term.definition
    list_display = ('word', 'definition', 'source', 'ref_point')
    list_filter = ('word', 'source')
    ordering = ('word',)
    search_fields = ('word', 'source')

    # def __str__(self):
    #     if len(self.definition) > 30:
    #         return self.definition[:30]
    #     else:
    #         return self.definition
