from django.db import models

class Organism(models.Model):
    taxa_id = models.CharField(primary_key=True, max_length=256, null=False, blank=False)
    clade = models.CharField(max_length=256, null=False, blank=False)
    genus = models.CharField(max_length=256, null=False, blank=False)
    species = models.CharField(max_length=256, null=False, blank=False)

    def __str__(self):
        return self.taxa_id

class Pfam_id(models.Model):
    domain_id = models.CharField(max_length=256, null=False, blank=False)
    domain_description = models.CharField(max_length=256, null=False, blank=False)

    def __str__(self):
        return self.domain_id

class Protein(models.Model):
    protein_id = models.CharField(primary_key=True, max_length=256, null=False, blank=False)
    sequence = models.CharField(max_length=40000, null=True, blank=True)
    length = models.IntegerField(default=0, null=False, blank=False)
    taxonomy = models.ForeignKey(Organism, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.protein_id

class Domain(models.Model):
    pfam_id = models.ForeignKey(Pfam_id, on_delete=models.DO_NOTHING)
    description = models.CharField(max_length=256, null=False, blank=False)
    start = models.IntegerField(null=True, blank=True)
    stop = models.IntegerField(null=True, blank=True)
    protein_id = models.ForeignKey(Protein, on_delete=models.DO_NOTHING, related_name='domains', null=True)
    organism = models.ForeignKey(Organism, on_delete=models.DO_NOTHING, null=True)


