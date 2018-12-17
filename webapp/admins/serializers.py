from rest_framework.serializers import ModelSerializer

from webapp.models import Registro


class RegistroSerializer(ModelSerializer):
    class Meta:
        model = Registro
        fields = ('')
