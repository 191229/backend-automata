from rest_framework import serializers
from lenguajes.models import Conjunto

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conjunto
        fields = ['conjuntos']

# from rest_framework import serializers
# from familia_conjuntos.models import fam_conjuntosModel

# class fam_conjuntosSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = fam_conjuntosModel
#         fields = ('conjunto',) 