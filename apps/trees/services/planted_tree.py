from rest_framework import serializers
from ..models.planted_tree import PlantedTree
from apps.trees.services.tree_serializer import TreeSerializer
from apps.accounts.services import UserSerializer, AccountSerializer  # Importe os serializers de User e Account

class PlantedTreeSerializer(serializers.ModelSerializer):
    tree = TreeSerializer()  
    user = UserSerializer()  
    account = AccountSerializer()  

    class Meta:
        model = PlantedTree
        fields = '__all__'  # Ou especifique os campos