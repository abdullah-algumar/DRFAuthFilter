from rest_framework.serializers import ModelSerializer
from django_countries.serializer_fields import CountryField
from rest.models import Kurulus


    
class KurulusSerializer(ModelSerializer):
    country = CountryField()

    class Meta:
        model = Kurulus
        fields = '__all__'