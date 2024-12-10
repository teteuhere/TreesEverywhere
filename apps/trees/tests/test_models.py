from django.test import TestCase
from django.contrib.auth import get_user_model
from ...accounts.models import Account
from ..models import Tree, PlantedTree

User = get_user_model()

class TreeModelTests(TestCase):
    def setUp(self):
        """Configuração inicial para os testes de modelo."""
        self.account1 = Account.objects.create(name="Account 1")
        self.user1 = User.objects.create_user(
            username="user1", password="password", account=self.account1
        )
        self.tree1 = Tree.objects.create(
            common_name="Common Name 1", scientific_name="Scientific Name 1"
        )

    def test_create_tree(self):
        """Testa a criação de uma árvore."""
        tree = Tree.objects.create(
            common_name="Teste", scientific_name="Teste"
        )
        self.assertTrue(isinstance(tree, Tree))
        self.assertEqual(tree.__str__(), tree.common_name)

    def test_plant_tree_method(self):
        """Testa o método User.plant_tree()."""
        planted_tree = self.user1.plant_tree(
            self.tree1, latitude=987.654, longitude=321.098
        )
        self.assertTrue(isinstance(planted_tree, PlantedTree))
        self.assertEqual(planted_tree.tree, self.tree1)
        self.assertEqual(planted_tree.planted_by, self.user1)

    def test_plant_trees_method(self):
        """Testa o método User.plant_trees()."""
        trees = [
            {'tree': self.tree1, 'latitude': 111.222, 'longitude': 333.444},
        ]
        planted_trees = self.user1.plant_trees(trees)
        self.assertEqual(len(planted_trees), 1)
        self.assertTrue(isinstance(planted_trees[0], PlantedTree))
        self.assertEqual(planted_trees[0].tree, self.tree1)
        self.assertEqual(planted_trees[0].planted_by, self.user1)