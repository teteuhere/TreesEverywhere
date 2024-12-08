from django.contrib import admin
from .models import Tree, PlantedTree

# Register your models here.
admin.site.register(Tree)
admin.site.register(PlantedTree)