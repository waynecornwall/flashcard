from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_term', views.add_term, name='add_term'),
    path('edit_term/<int:term_id>', views.edit_term, name='edit_term'),
    path('delete_term/<int:term_id>', views.delete_term, name='delete_term'),

    path('<int:term_id>/definitions', views.definitions, name='definitions'),
    path('<int:term_id>/definitions/add', views.add_def, name='add_def'),
    # path('<int:term_id>/definitions/edit/<int:def_id>', views.edit_def, name='edit_def'),
    # path('<int:term_id>/definitions/delete/<int:def_id>', views.delete_def, name='delete_def'),

    path('sources', views.sources, name='sources'),
    path('sources/add', views.add_source, name='add_source'),
    # path('sources/edit/<int:source_id>', views.edit_source, name='edit_source'),
    # path('sources/delete/<int:source_id>', views.delete_source, name='delete_source'),

]