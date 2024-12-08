from rest_framework.test import APITestCase
from ..models.trees import Tree

class TreeTests(APITestCase):
    def test_create_tree(self):
        """
        Testa a criação de uma nova árvore.
        """
        url = '/api/trees/'
        data = {'name': 'Ipê', 'scientific_name': 'Tabebuia impetiginosa'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)  # Verifica se a árvore foi criada com sucesso
        self.assertEqual(Tree.objects.count(), 1)  # Verifica se a árvore foi salva no banco de dados
        self.assertEqual(Tree.objects.get().name, 'Ipê')  # Verifica se o nome da árvore está correto