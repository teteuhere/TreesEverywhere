from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.trees.models import PlantedTree

@login_required
def account_trees(request):
    trees = PlantedTree.objects.filter(planted_by__account=request.user.account)
    context = {'trees': trees}
    return render(request, 'trees/account_trees.html', context)