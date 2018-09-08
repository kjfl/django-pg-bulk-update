"""
This file contains sample models to use in tests
"""
from django.db import models

from django_pg_bulk_update.manager import BulkUpdateManager
from django_pg_bulk_update.compatibility import jsonb_available, hstore_available, array_available

class Meta:
    unique_together = ['id', 'name']

# Not all fields are available in different django and postgres versions
model_attrs = {
    'name': models.CharField(max_length=50, null=True, blank=True, default=''),
    'int_field': models.IntegerField(null=True, blank=True),
    'objects': BulkUpdateManager(),
    'Meta': Meta,
    '__module__': __name__
}

if array_available():
    from django.contrib.postgres.fields import ArrayField
    model_attrs['array_field'] = ArrayField(models.IntegerField(null=True, blank=True))

if hstore_available():
    from django.contrib.postgres.fields import HStoreField
    model_attrs['hstore_field'] = HStoreField(null=True, blank=True)

if jsonb_available():
    from django.contrib.postgres.fields import JSONField
    model_attrs['json_field'] = JSONField(null=True, blank=True)

TestModel = type('TestModel', (models.Model,), model_attrs)
