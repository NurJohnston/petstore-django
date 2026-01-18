from django.shortcuts import render, redirect
from .models import Pet
from .forms import PetForm 

def pet_list(request):
    pets = Pet.objects.all()
    return render(request, 'pets/pet_list.html', {'pets': pets})

def pet_create(request):
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pet_list') 
    else:
        form = PetForm()
    return render(request, 'pets/pet_form.html', {'form': form})

def pet_edit(request, pk):
    pet = Pet.objects.get(pk=pk)  # fetch the pet by primary key
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pet_list')
    else:
        form = PetForm(instance=pet)
    return render(request, 'pets/pet_form.html', {'form': form})

def pet_delete(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'POST':
        pet.delete()
        return redirect('pet_list')
    return render(request, 'pets/pet_confirm_delete.html', {'pet': pet})

