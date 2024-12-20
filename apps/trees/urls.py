from django.urls import path
from .views import PlantedTreeList, PlantedTreeDetail, TreeList, TreeDetail, RegisterTree, RegisterTreeAPI

urlpatterns = [
    path('trees/', TreeList.as_view()),
    path('trees/<int:pk>/', TreeDetail.as_view()),
    path('plantedtrees/', PlantedTreeList.as_view()),
    path('plantedtrees/<int:pk>/', PlantedTreeDetail.as_view()),
    path('api/register/', RegisterTreeAPI.as_view(), name='registrar_arvore'),
    path('register/', RegisterTree, name='register_tree'),
]