from rest_framework import serializers
from .models import *

class ApiSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = info
        fields = '__all__'
    class Meta:
        model = FocusActor
        fields = '__all__'