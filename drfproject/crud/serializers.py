from rest_framework import serializers
from .models import boleto 
from .models import empresa

class BoletoSerializers(serializers.ModelSerializer):
    class Meta:
        model = boleto
        fields = '__all__'

class EmpresaSerializers(serializers.ModelSerializer):
    class Meta:
        model = empresa
        fields = '__all__'