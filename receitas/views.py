from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from .models import Receita
from .forms import ReceitaForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def index(request):
    receitas = Receita.objects.all()

    dados = {
        'receitas': receitas
    }

    return render(request,'index.html', dados)

def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)

    receita_a_exibir = {
        'receita': receita
    }

    return render(request,'receita.html', receita_a_exibir)

def buscar(request):
    query = request.GET.get('q', '')

    if query:
        receitas = Receita.objects.filter(nome_receita__icontains=query)
    else:
        receitas = []

    return render(request, 'buscar.html', {'receitas': receitas, 'query': query})

def adicionar_receita(request):
    if request.method == 'POST':
        form = ReceitaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ReceitaForm()

    return render(request, 'adicionar_receita.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('perfil')
        else:
            return render(request, 'login.html',{'error':'Usuário ou Senha inválidos!'})
    return render(request, 'login.html')

def logout(request):
    logout(request)
    return redirect('index')

@login_required
def perfil(request):
    return render(request, "perfil.html", {"user": request.user})
