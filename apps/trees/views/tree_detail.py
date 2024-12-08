from ..models.trees import Tree
from rest_framework import generics
from ..services.planted_tree import TreeSerializer

class TreeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tree.objects.all()
    serializer_class = TreeSerializer