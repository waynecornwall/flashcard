from django.shortcuts import render, redirect
from .models import Source, Term, Definition
from .forms import TermForm, SourceForm, DefinitionForm

MEDIA_TYPES = {
    'book' : 'page',
    'video' : 'starts at',
    'audio' : 'starts at'
}


def index(request):
    terms = Term.objects.all()
    context = {
        'terms' : terms
    }
    return render(request, 'posts/index.html', context)


def add_term(request):
    if request.method != 'POST':
        form = TermForm()
    else:
        form = TermForm(request.POST)
        form.save()
        return redirect('posts:index')
    context = {
        'form' : form
    }
    return render(request, 'posts/add_term.html', context)


def edit_term(request, term_id):
    term = Term.objects.get(id=term_id)
    if request.method != 'POST':
        form = TermForm(instance=term)
    else:
        form = TermForm(instance=term, data = request.POST)
        form.save()
        return redirect('posts:index')
    context = {
        'term' : term,
        'form' : form
    }
    return render(request, 'posts/edit_term.html', context)


def delete_term(request, term_id):
    term = Term.objects.get(id=term_id)
    if request.method == 'POST':
        term.delete()
        return redirect('posts:index')
    context = {
        'term' : term
    }
    return render(request, 'posts/delete_term.html', context)


def sources(request):
    sources = Source.objects.order_by('title')
    context = {
        'sources' : sources
    }
    return render(request, 'posts/sources.html', context)


def add_source(request):
    if request.method != 'POST':
        form = SourceForm()
    else:
        form = SourceForm(request.POST)
        form.save()
        return redirect('posts:sources')
    context = {
        'form' : form
    }
    return render(request, 'posts/add_source.html', context)


def definitions(request, term_id):
    term = Term.objects.get(id=term_id)
    defs = term.definition_set.all()
    context = {
        'term' : term,
        'defs' : defs,
        'MEDIA_TYPES' : MEDIA_TYPES
    }
    return render(request, 'posts/defs.html', context)


def add_def(request, term_id):
    term = Term.objects.get(id=term_id)
    if request.method != 'POST':
        form = DefinitionForm()
    else:
        form = DefinitionForm(request.POST)
        form.save()
        return redirect('posts:definitions', term_id=term.id)
    context = {
        'form': form,
        'term': term
    }
    return render(request, 'posts/add_def.html', context)