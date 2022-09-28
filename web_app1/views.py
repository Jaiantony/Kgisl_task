from .forms import *
from django.shortcuts import render, redirect


def animal_items(request):
    animals_data = Animal.objects.all()
    animal_query = Animal_data.objects.all()
    context = {"animals_data": animals_data, "animal_query": animal_query}
    if request.method == "POST":
        form = AnimalCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'breeds.html', context)
        else:
            pass

    return render(request, 'breeds.html', context)


def modules(request):
    breed = request.GET.get('animal')
    breed_data = Breed.objects.filter(animal=breed)
    context = {"breed_data": breed_data}
    return render(request, 'modules.html', context)


def animal_delete(request, id):
    item = Animal_data.objects.get(id=id)
    item.delete()
    return redirect('home')
