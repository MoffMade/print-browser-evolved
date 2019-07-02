from django.db import models

# Create your models here.

class BasicResource(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class CreatedItem(models.Model):
    ARTISAN = 'A'
    CULINARY = 'C'
    ANY = '-'
    BASIC = 'B'
    PROFICIENT = 'P'
    MASTER = 'M'
    PRODUCTION_CHOICES = [
        (ARTISAN, 'Artisan'),
        (CULINARY, 'Culinary'),
        (ANY, 'Any'),
    ]
    TIER_CHOICES = [
        (BASIC, 'Basic'),
        (PROFICIENT, 'Proficient'),
        (MASTER, 'Master'),
        (ANY, 'Any'),
    ]
    name = models.CharField(max_length=64)
    created_by = models.CharField(max_length=1, choices=PRODUCTION_CHOICES, default=ANY)
    tier = models.CharField(max_length=1, choices=TIER_CHOICES, default=BASIC)
    mind = models.IntegerField()
    time = models.IntegerField()
    #materials_basic = models.ManyToManyField(BasicResourceMaterial, symmetrical=False, blank=True)
    #materials_created = models.ManyToManyField(CreatedItemMaterial, symmetrical=False, blank=True)
    mechanics = models.CharField(max_length=200)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class BasicResourceMaterial(BasicResource):
    amount = models.IntegerField(default=1, null=False, blank=False)
    used_in = models.ManyToManyField(CreatedItem, symmetrical=False, blank=True)


class CreatedItemMaterial(CreatedItem):
    amount = models.IntegerField(default=1, null=False, blank=False)
    used_in = models.ManyToManyField('self', symmetrical=False, blank=True)

