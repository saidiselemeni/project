from . models import *
from rest_framework import serializers

class ChairPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = chairperson
        fields = "__all__"