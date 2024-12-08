from datetime import date
from .trees import Tree  
from django.db import models
from apps.accounts.models.user import User
from apps.accounts.models.account import Account

class PlantedTree(models.Model):
    age = models.IntegerField(default=0)
    planted_at = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tree = models.ForeignKey(Tree, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    
    def calcular_idade(self):
        hoje = date.today()
        return hoje.year - self.planted_at.year - ((hoje.month, hoje.day) < (self.planted_at.month, self.planted_at.day))
    
    def __str__(self):
        return f"{self.tree.name} planted by {self.user.username} at {self.location}"