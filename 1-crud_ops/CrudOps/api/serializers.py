from rest_framework import serializers
from base.models import Person
"""
To enable APIs to read data more easily,
serializers transform complex Django models
into JSON objects.
"""


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
        # alt: fields=('name', 'id')
