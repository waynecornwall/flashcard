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
    page_title = 'Homepage'
    context = {
        'terms' : terms,
        'page_title': page_title
    }
    return render(request, 'posts/index.html', context)


def add_term(request):
    page_title = 'Add a Term'
    if request.method != 'POST':
        form = TermForm()
    else:
        form = TermForm(request.POST)
        form.save()
        return redirect('posts:index')
    context = {
        'form' : form,
        'page_title': page_title
    }
    return render(request, 'posts/add_term.html', context)


def edit_term(request, term_id):
    term = Term.objects.get(id=term_id)
    page_title = f'Edit {term.word}'
    if request.method != 'POST':
        form = TermForm(instance=term)
    else:
        form = TermForm(instance=term, data = request.POST)
        form.save()
        return redirect('posts:index')
    context = {
        'term' : term,
        'form' : form,
        'page_title': page_title
    }
    return render(request, 'posts/edit_term.html', context)


def delete_term(request, term_id):
    term = Term.objects.get(id=term_id)
    page_title = f'Delete {term.word}'
    if request.method == 'POST':
        term.delete()
        return redirect('posts:index')
    context = {
        'term' : term,
        'page_title': page_title
    }
    return render(request, 'posts/delete_term.html', context)


def sources(request):
    sources = Source.objects.order_by('title')
    page_title = 'Sources'
    context = {
        'sources' : sources,
        'page_title': page_title
    }
    return render(request, 'posts/sources.html', context)


def add_source(request):
    page_title = f'Add a source'
    if request.method != 'POST':
        form = SourceForm()
    else:
        form = SourceForm(request.POST)
        form.save()
        return redirect('posts:sources')
    context = {
        'form' : form,
        'page_title': page_title
    }
    return render(request, 'posts/add_source.html', context)


def definitions(request, term_id):
    term = Term.objects.get(id=term_id)
    defs = term.definition_set.all()
    page_title = f'{term.word} definitions'
    context = {
        'term' : term,
        'defs' : defs,
        'MEDIA_TYPES' : MEDIA_TYPES,
        'page_title': page_title
    }
    return render(request, 'posts/defs.html', context)


def add_def(request, term_id):
    term = Term.objects.get(id=term_id)
    page_title = 'Add a definition'
    if request.method != 'POST':
        form = DefinitionForm()
    else:
        form = DefinitionForm(request.POST)
        form.save()
        return redirect('posts:definitions', term_id=term.id)
    context = {
        'form': form,
        'term': term,
        'page_title' : page_title
    }
    return render(request, 'posts/add_def.html', context)