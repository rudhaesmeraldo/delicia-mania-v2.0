from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Receita
from .forms import ReceitaForm

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
    if request.method == "POST":
        form = ReceitaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ReceitaForm()

    return render(request, 'adicionar_receita.html', {'form': form})
