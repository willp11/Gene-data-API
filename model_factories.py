import factory
from random import randint
from django.test import TestCase
from django.conf import settings
from django.core.files import File
from .models import *

class OrganismFactory(factory.django.DjangoModelFactory):
    taxa_id = str(randint(1000,100000))
    clade = 'E'
    genus = 'Ancylostoma' 
    species = 'ceylanicum'

    class Meta:
        model = Organism

class PfamFactory(factory.django.DjangoModelFactory):
    domain_id = 'PF00001'
    domain_description = '7transmembranereceptor(rhodopsinfamily)'

    class Meta:
        model = Pfam_id

class ProteinFactory(factory.django.DjangoModelFactory):
    protein_id = 'A0A016S8J7'
    sequence = 'MVIGVGFLLVLFSSSVLGILNAGVQLRIEELFDTPGHTNNWAVLVCTSRFWFNYRHVSNVLALYHTVKRLGIPDSNIILMLAEDVPCNPRNPRPEAAVLSA'
    length = len(sequence)
    taxonomy = factory.SubFactory(OrganismFactory)

    class Meta:
        model = Protein

class DomainFactory(factory.django.DjangoModelFactory):
    pfam_id = 'PF00001'
    description = 'Peptidase C13 legumain'
    start = randint(1,1000)
    stop = start + randint(10,200)
    protein_id = factory.SubFactory(ProteinFactory)
    organism = factory.SubFactory(OrganismFactory)

    class Meta:
        model = Domain

