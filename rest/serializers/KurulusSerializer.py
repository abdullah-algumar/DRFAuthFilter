from rest_framework.serializers import ModelSerializer
from rest.models import Kurulus


class KurulusSerializer(ModelSerializer):
    class Meta:
        model = Kurulus
        fields = '__all__'