from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    groups = models.ManyToManyField(
          'auth.Group',
          related_name='custom_user_set',
          blank=True,
          help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
          verbose_name='groups',
    )
    account = models.ForeignKey('Account', on_delete=models.CASCADE, blank=True, null=True)
    user_permissions = models.ManyToManyField(
          'auth.Permission',
          related_name='custom_user_set',
          blank=True,
          help_text='Specific permissions for this user.',
          verbose_name='user permissions',
    )

    def plant_tree(self, tree, location):
        """
        Plants a single tree at the specified location.

        Args:
            tree: The Tree object to be planted.
            location: A tuple containing the latitude and longitude as Decimal objects.
        """
        from ...trees.services.planted_tree_service import create_planted_tree
        create_planted_tree(self, tree, location)



    def plant_trees(self, plants):
        """
        Plants multiple trees at the specified locations.

        Args:
            plants: A list of tuples where the first element is the Tree object
                   and the second is a tuple with latitude and longitude as Decimal objects.
        """
        from ...trees.services.planted_tree_service import create_planted_tree
        for tree, location in plants:
            create_planted_tree(self, tree, location)