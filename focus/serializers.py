from rest_framework import serializers
from .models import *

class ApiSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FocusActor
        fields = '__all__'