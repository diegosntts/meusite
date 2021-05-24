# Chamada
from django.contrib import messages
from django.core.paginator import InvalidPage, Paginator
from django.shortcuts import redirect, render, get_object_or_404

# Chamada forms
from ..forms import ProdutosForm
from ..models import Produtos

ITEMS_PER_PAGE = 4

# Home produto
# Home produto ainda precisa ser modificada


def home_produtos(request, template_name="produtos/home.html"):
    context = {
        'produtos': Produtos.objects.all()
    }
    return render(request, template_name, context)

# Cadastrar Produto


def cadastrar_produtos(request, template_name="produtos/cadastrar.html"):
    form = ProdutosForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        try:
            if form.is_valid():
                produto = form.save(commit=False)
                produto.user_id = request.user.id
                produto.save()
                messages.success(request, "Produto salvo com sucesso!")
                return redirect('home_produtos')
        except:
            messages.error(request, "Error ao cadastrar produto")
    return render(request, template_name, {'form': form})

# Editar Produto


def editar_produtos(request, pk, template_name="produtos/cadastrar.html"):
    produto = Produtos.objects.get(pk=pk)
    form = ProdutosForm(request.POST or None, request.FILES or None, instance=produto)
    
    if form.is_valid():
        form.save()
        return redirect('home_produtos')
    return render(request, template_name, {'form':form, 'produto':produto})
       

