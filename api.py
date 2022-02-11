from django.http.response import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework import mixins
from django.forms.models import model_to_dict
from .models import *
from .serializers import *
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

class ProteinDetail(generics.RetrieveAPIView):
    serializer_class = ProteinSerializer

    def get_queryset(self):
        protein_id = self.kwargs['protein_id']
        protein = Protein.objects.filter(protein_id=protein_id)
        return protein

    def get_object(self):
        queryset = self.get_queryset()
        protein_id = self.kwargs['protein_id']
        obj = get_object_or_404(queryset, protein_id=protein_id)
        return obj

class PfamDescription(generics.RetrieveAPIView):
    serializer_class = PfamIdSerializer

    def get_queryset(self):
        pfam_id = self.kwargs['pfam_id']
        pfam = Pfam_id.objects.filter(domain_id=pfam_id)
        return pfam
    
    def get_object(self):
        queryset = self.get_queryset()
        pfam_id = self.kwargs['pfam_id']
        obj = get_object_or_404(queryset, domain_id=pfam_id)
        return obj

class ProteinsByTaxaId(generics.ListAPIView):
    serializer_class = ProteinIdSerializer

    def get_queryset(self):
        taxa_id = self.kwargs['taxa_id']
        proteins = Domain.objects.filter(organism=taxa_id)
        return proteins

class DomainsByTaxaId(generics.ListAPIView):
    serializer_class = DomainIdPfamIdSerializer

    def get_queryset(self):
        taxa_id = self.kwargs['taxa_id']
        domains = Domain.objects.filter(organism=taxa_id)
        return domains

@api_view(['GET'])
def protein_coverage(request, protein_id):
    try:
        protein = Protein.objects.get(protein_id=protein_id)
    except Protein.DoesNotExist:
        return HttpResponse(status=404)

    domains = Domain.objects.filter(protein_id=protein_id)
    length = 0
    for domain in domains:
        length += domain.stop - domain.start
    coverage = length / protein.length

    return Response({"coverage": coverage})

@api_view(['POST'])
def new_protein(request):
    serializer = AddProteinSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)