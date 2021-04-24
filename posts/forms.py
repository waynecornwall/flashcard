from django import forms
from .models import Definition, Term, Source


class TermForm(forms.ModelForm):
    class Meta:
        model = Term
        fields = ['word']
        labels = {
            'word' : 'Word'
        }


class SourceForm(forms.ModelForm):
    class Meta:
        model = Source
        fields = ['title', 'media', 'author']
        labels = {
            'title' : 'Title',
            'media' : 'Media',
            'author' : 'Author'
        }


class DefinitionForm(forms.ModelForm):
    class Meta:
        model = Definition
        fields = ['definition', 'source', 'ref_point', 'term']
        labels = {
            'definition' : 'Definition',
            'ref_point' : 'Reference point',
            'source' : 'Source',
            'term' : 'Term'
        }