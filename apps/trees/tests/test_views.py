from django.test import TestCase
from django.contrib.auth import get_user_model
from ...accounts.models import Account
from ..models import Tree, PlantedTree
from django.urls import reverse

User = get_user_model()

class TreeViewTests(TestCase):
    def setUp(self):
        """Configuração inicial para os testes de views."""
        self.account1 = Account.objects.create(name="Account 1")
        self.account2 = Account.objects.create(name="Account 2")
        self.user1 = User.objects.create_user(
            username="user1", password="password", account=self.account1
        )
        self.user2 = User.objects.create_user(
            username="user2", password="password", account=self.account1
        )
        self.user3 = User.objects.create_user(
            username="user3", password="password", account=self.account2
        )
        self.tree1 = Tree.objects.create(
            common_name="Common Name 1", scientific_name="Scientific Name 1"
        )
        self.tree2 = Tree.objects.create(
            common_name="Common Name 2", scientific_name="Scientific Name 2"
        )
        self.user1.plant_tree(self.tree1, latitude=123.456, longitude=789.012)
        self.user2.plant_tree(self.tree2, latitude=456.789, longitude=123.045)
        self.user3.plant_tree(self.tree1, latitude=789.012, longitude=456.378)

    def test_planted_tree_list_view(self):
        """Testa se a listagem de árvores plantadas está correta."""
        self.client.login(username="user1", password="password")
        response = self.client.get(reverse("trees:planted_tree_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Common Name 1")
        self.assertNotContains(response, "Common Name 2")

    def test_planted_tree_list_view_forbidden(self):
        """Testa se o acesso a árvores de outros usuários é proibido."""
        self.client.login(username="user1", password="password")
        response = self.client.get(
            reverse("trees:planted_tree_detail", kwargs={"pk": 3})
        )
        self.assertEqual(response.status_code, 403)

    def test_planted_tree_list_view_account_users(self):
        """Testa se a listagem de árvores plantadas por usuários da mesma conta está correta."""
        self.client.login(username="user1", password="password")
        response = self.client.get(reverse("trees:planted_tree_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Common Name 1")
        self.assertContains(response, "Common Name 2")