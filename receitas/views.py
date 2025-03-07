from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from .models import Receita
from .forms import ReceitaForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required

def index(request):
    receitas = Receita.objects.all()
    return render(request, 'index.html', {'receitas': receitas})

def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    outras_receitas = Receita.objects.exclude(id=receita_id)[:3]
    return render(request, 'receita.html', {'receita': receita, 'outras_receitas': outras_receitas})

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

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            next_url = request.POST.get('next', 'perfil')
            return redirect(next_url)
        else:
            return render(request, 'login.html', {'error': 'Usuário ou Senha inválidos!'})
    return render(request, 'login.html')


def logout_view(request):
    auth_logout(request)
    return redirect('index')

@login_required
def perfil(request):
    return render(request, 'perfil.html')
