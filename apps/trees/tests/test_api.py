from rest_framework.test import APITestCase
from ...accounts.models import Account
from ..models import Tree, PlantedTree
from django.contrib.auth import get_user_model

User = get_user_model()

class TreeAPITests(APITestCase):
    def setUp(self):
        """Configuração inicial para os testes de API."""
        self.account1 = Account.objects.create(name="Account 1")
        self.user1 = User.objects.create_user(
            username="user1", password="password", account=self.account1
        )
        self.tree1 = Tree.objects.create(
            common_name="Common Name 1", scientific_name="Scientific Name 1"
        )
        self.client.force_authenticate(user=self.user1)

    def test_create_tree(self):
        """Testa a criação de uma árvore via API."""
        url = '/api/trees/'
        data = {'common_name': 'Ipê', 'scientific_name': 'Tabebuia impetiginosa'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Tree.objects.count(), 2)  # Inclui a árvore criada no setUp
        self.assertEqual(Tree.objects.get(common_name='Ipê').scientific_name, 'Tabebuia impetiginosa')

    def test_list_trees(self):
        """Testa a listagem de árvores via API."""
        url = '/api/trees/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)  # Deve retornar a árvore criada no setUp

    def test_retrieve_tree(self):
        """Testa a recuperação de uma árvore específica via API."""
        url = f'/api/trees/{self.tree1.id}/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['common_name'], 'Common Name 1')

    def test_create_planted_tree(self):
        """Testa o registro de uma árvore plantada via API."""
        url = '/api/planted_trees/'
        data = {'tree': self.tree1.id, 'latitude': 123.456, 'longitude': 789.012}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(PlantedTree.objects.count(), 1)
        self.assertEqual(PlantedTree.objects.get().tree, self.tree1)

    def test_list_planted_trees(self):
        """Testa a listagem de árvores plantadas via API."""
        PlantedTree.objects.create(tree=self.tree1, planted_by=self.user1, latitude=123.456, longitude=789.012)
        url = '/api/planted_trees/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_planted_tree(self):
        """Testa a recuperação de uma árvore plantada específica via API."""
        planted_tree = PlantedTree.objects.create(tree=self.tree1, planted_by=self.user1, latitude=123.456, longitude=789.012)
        url = f'/api/planted_trees/{planted_tree.id}/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['tree'], self.tree1.id)