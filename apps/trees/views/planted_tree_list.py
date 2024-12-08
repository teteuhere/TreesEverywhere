from rest_framework import generics
from ..models.planted_tree import PlantedTree
from ..services.planted_tree import PlantedTreeSerializer

class PlantedTreeList(generics.ListCreateAPIView):
    queryset = PlantedTree.objects.all()
    serializer_class = PlantedTreeSerializer
