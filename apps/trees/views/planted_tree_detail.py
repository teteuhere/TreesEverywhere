from rest_framework import generics
from ..models.planted_tree import PlantedTree
from ..services.planted_tree import PlantedTreeSerializer

class PlantedTreeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PlantedTree.objects.all()
    serializer_class = PlantedTreeSerializer
