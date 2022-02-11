from django.test import TestCase
import json
from django.urls import reverse
from django.urls import reverse_lazy

from rest_framework.test import APIRequestFactory, APITestCase

from .model_factories import *
from .serializers import *

class ProteinTest(APITestCase):

    organism = None
    protein = None
    pfam = None
    domain = None

    def setUp(self):
        self.organism = OrganismFactory.create()
        self.protein = ProteinFactory.create(taxonomy=self.organism)
        self.pfam = PfamFactory.create()
        self.domain = DomainFactory.create(pfam_id=self.pfam, protein_id=self.protein, organism=self.organism)

    def tearDown(self):
        Protein.objects.all().delete()
        Organism.objects.all().delete()
        Pfam_id.objects.all().delete()
        Domain.objects.all().delete()
        ProteinFactory.reset_sequence(0)
        OrganismFactory.reset_sequence(0)
        PfamFactory.reset_sequence(0)
        DomainFactory.reset_sequence(0)

    def test_proteinDetailReturnSuccess(self):
        url = reverse('protein_detail', kwargs={'protein_id': self.protein.protein_id})
        response = self.client.get(url)
        response.render()
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertTrue('protein_id' in data)
        self.assertTrue('sequence' in data)
        self.assertTrue('length' in data)
        self.assertTrue('taxonomy' in data)
        self.assertTrue('domains' in data)
        self.assertTrue(data['taxonomy'], self.organism)
        self.assertTrue(data['domains'][0]['pfam_id'], self.domain.pfam_id)
        self.assertTrue(data['domains'][0]['description'], self.domain.description)
        self.assertTrue(data['domains'][0]['start'], self.domain.start)
        self.assertTrue(data['domains'][0]['stop'], self.domain.stop)

    def test_proteinsByTaxaIdReturnSuccess(self):
        url = reverse('proteins_by_taxa_id', kwargs={'taxa_id': self.organism.taxa_id})
        response = self.client.get(url)
        response.render()
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertTrue('id' in data[0])
        self.assertTrue('protein_id' in data[0]) 
        self.assertTrue(data[0]['id'], self.domain.id)
        self.assertTrue(data[0]['protein_id'], self.domain.protein_id)

    def test_pfamDescriptionReturnSuccess(self):
        url = reverse('pfam_description', kwargs={'pfam_id': self.pfam.domain_id})
        response = self.client.get(url)
        response.render()
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertTrue('domain_id' in data)
        self.assertTrue('domain_description' in data) 
        self.assertTrue(data['domain_id'], self.pfam.domain_id)
        self.assertTrue(data['domain_description'], self.pfam.domain_description) 

    def test_domainsByTaxaIdReturnSuccess(self):
        url = reverse('domains_by_taxa_id', kwargs={'taxa_id': self.organism.taxa_id})
        response = self.client.get(url)
        response.render()
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertTrue('id' in data[0])
        self.assertTrue('pfam_id' in data[0]) 
        self.assertTrue(data[0]['id'], self.domain.id)
        self.assertTrue(data[0]['pfam_id'], self.pfam)
    
    def test_proteinCoverageReturnSuccess(self):
        url = reverse('protein_coverage', kwargs={'protein_id': self.protein.protein_id})
        response = self.client.get(url)
        response.render()
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        coverage = (self.domain.stop - self.domain.start) / self.protein.length
        self.assertTrue('coverage' in data)
        self.assertTrue(data['coverage'], coverage)

    def test_addNewProteinReturnSuccess(self):
        url = reverse('add_new_protein')
        data = {
            "protein_id": "TEST",
            "sequence": "ABC",
            "length": 3,
            "taxonomy": self.organism.taxa_id
        }
        response = self.client.post(url, data, format='json')
        response.render()
        self.assertEqual(response.status_code, 201)

    def test_addNewProteinReturnFail(self):
        url = reverse('add_new_protein')
        data = {
            "protein_id": "TEST",
            "sequence": "ABC",
            "length": 3,
            "taxonomy": 'DEF'
        }
        response = self.client.post(url, data, format='json')
        response.render()
        self.assertEqual(response.status_code, 400)