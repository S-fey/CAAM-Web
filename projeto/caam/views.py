from django.shortcuts import render
from .models import Animal
from .forms import CadastroAnimal

from django.contrib.auth import  login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone

def index(request):
    animais = Animal.objects.all()
    context = dict(
        animais=animais
    )
    return render(request, "caam/index.html", context=context)

def animal(request, id):
    context = dict(animal=Animal.objects.get(id=id))
    return render(request, "caam/animal.html", context=context)



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)  
            return redirect('/')  
    else:
        form = AuthenticationForm()
    return render(request, 'caam/login.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('login')  
    else:
        form = UserCreationForm()
    return render(request, 'caam/register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('logout_success')


def logout_success_view(request):
    return render(request, 'caam/logout.html')

def criar_animal(request):
    if request.method == 'POST':
        form = CadastroAnimal(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CadastroAnimal()
        
    return render(request, 'caam/cadastro_animal.html', {'form': form})

@login_required
def adotar_animal(request, id):
    animal = get_object_or_404(Animal, id=id)
    animal.tutor = request.user
    animal.data_adocao = timezone.now()
    animal.save()
    return redirect('/')