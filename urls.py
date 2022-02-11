from django.urls import include, path
from . import views
from . import api

urlpatterns = [
    path('', views.Home, name='home'),
    path('api/protein/', api.new_protein, name='add_new_protein'),
    path('api/protein/<protein_id>', api.ProteinDetail.as_view(), name='protein_detail'),
    path('api/proteins/<taxa_id>', api.ProteinsByTaxaId.as_view(), name='proteins_by_taxa_id'),
    path('api/pfam/<pfam_id>', api.PfamDescription.as_view(), name='pfam_description'),
    path('api/pfams/<taxa_id>', api.DomainsByTaxaId.as_view(), name='domains_by_taxa_id'),
    path('api/coverage/<protein_id>', api.protein_coverage, name='protein_coverage')
]