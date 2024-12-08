from apps.trees.models.planted_tree import PlantedTree

def create_planted_tree(user, tree, location):
    """
    Creates a new PlantedTree object and associates it with the user, tree, and account.

    Args:
        user: The User object who planted the tree.
        tree: The Tree object that was planted.
        location: A tuple containing the latitude and longitude as Decimal objects.
    """

    location_str = f"{location[0]:.6f},{location[1]:.6f}"

    account = user.account_set.first()

    PlantedTree.objects.create(
        user=user,
        tree=tree,
        account=account,
        location=location_str
    )