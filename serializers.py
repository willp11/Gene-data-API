from rest_framework import serializers
from .models import *

class PfamIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pfam_id
        fields = ['domain_id', 'domain_description']

class DomainSerializer(serializers.ModelSerializer):
    pfam_id = PfamIdSerializer()
    class Meta:
        model = Domain
        fields = ['pfam_id', 'description', 'start', 'stop']

class OrganismSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organism
        fields = ['taxa_id', 'clade', 'genus', 'species']

class ProteinSerializer(serializers.ModelSerializer):
    taxonomy = OrganismSerializer()
    domains = DomainSerializer(many=True)
    class Meta:
        model = Protein
        fields = ['protein_id', 'sequence', 'length', 'taxonomy', 'domains']

class AddProteinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Protein
        fields = ['protein_id', 'sequence', 'length', 'taxonomy']

    def create(self, validated_data):
        taxa_id = self.initial_data.get('taxonomy')

        protein = Protein(**{**validated_data, 'taxonomy': Organism.objects.get(pk=taxa_id)})
        protein.save()
        return protein

class ProteinIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields = ['id', 'protein_id']

class DomainIdPfamIdSerializer(serializers.ModelSerializer):
    pfam_id = PfamIdSerializer()
    class Meta:
        model = Domain
        fields = ['id', 'pfam_id']
