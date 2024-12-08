from datetime import datetime
from django.shortcuts import render, redirect
from ..forms.planted_tree import PlantedTreeForm

def RegisterTree(request):
    if request.method == 'POST':
        form = PlantedTreeForm(request.POST)
        if form.is_valid():
            planted_tree = form.save(commit=False)
            planted_tree.user = request.user  
            planted_tree.account = request.user.account_set.first()
            planted_tree.planted_at = datetime.now()  
            planted_tree.save()
            return redirect('sucesso') 
    else:
        form = PlantedTreeForm()
    return render(request, 'tree/register.html', {'form': form})