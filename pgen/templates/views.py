from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, get_object_or_404
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required

##### _new -> Cria um novo #####
##### _detail -> Mostra mais sobre #####
##### _list -> Lista todos #####
##### _edit -> Abre edição #####
##### _remove -> Remove #####



##### Views Categoria #####

@login_required
def categoria_new(request):
	if request.method == 'POST':
		form = CategoriaForm(request.POST)
		if form.is_valid():
			categoria_new = form.save(commit=False)
			categoria_new.save()
			return redirect('categoria_list')
	else:
		form = CategoiraForm()
	return render(request,'pgen/categoria_new.html', {'form': form})

@login_required
def categoria_list(request):
	categoria = Categoria.objects.all()
	return render(request, 'pgen/categoria_list.html', {'categorias': categoria})

@login_required
def categoria_edit(request, pk):
	categoria = get_object_or_404(Categoria, pk=pk)
	if request.method == "POST":
		form = CategoriaForm(request.POST, instance=categoria)
		if form.is_valid():
			categoria = form.save(commit=False)
			categoria.save()
			return redirect('categoria_list')
	else:
		form = CategoriaForm(instance=tag)
	return render(request, 'pgen/categoria_new.html', {'form': form})

@login_required
def categoria_remove(request, pk):
	categoria = get_object_or_404(Categoria, pk=pk)
	categoria.delete()
	return redirect('categoria_list')




##### Views Instituição #####

@login_required
def instituicao_new(request):
	if request.method == 'POST':
		form = InstituicaoForm(request.POST)
		if form.is_valid():
			instituicao_new = form.save(commit=False)
			instituicao_new.save()
			return redirect('instituicao_list')
	else:
		form = InstituicaoForm()
	return render(request,'pgen/instituicao_new.html', {'form': form})

@login_required
def instituicao_list(request):
	instituicao = Instituicao.objects.all()
	return render(request, 'pgen/instituicao_list.html', {'instituicoes': instituicao})

@login_required
def instituicao_edit(request, pk):
	instituicao = get_object_or_404(Instituicao, pk=pk)
	if request.method == "POST":
		form = InstituicaoForm(request.POST, instance=instituicao)
		if form.is_valid():
			instituicao = form.save(commit=False)
			instituicao.save()
			return redirect('instituicao_list')
	else:
		form = InstituicaoForm(instance=instituicao)
	return render(request, 'pgen/instituicao_new.html', {'form': form})

@login_required
def instituicao_remove(request, pk):
	instituicao = get_object_or_404(Instituicao, pk=pk)
	instituicao.delete()
	return redirect('instituicao_list')




##### Views Estado #####

@login_required
def estado_new(request):
	if request.method == 'POST':
		form = EstadoForm(request.POST)
		if form.is_valid():
			estado_new = form.save(commit=False)
			estado_new.save()
			return redirect('estado_list')
	else:
		form = EstadoForm()
	return render(request,'pgen/estado_new.html', {'form': form})

@login_required
def estado_list(request):
	estado = Estado.objects.all()
	return render(request, 'pgen/estado_list.html', {'estados': estado})

@login_required
def estado_edit(request, pk):
	estado = get_object_or_404(Estado, pk=pk)
	if request.method == "POST":
		form = EstadoForm(request.POST, instance=estado)
		if form.is_valid():
			estado = form.save(commit=False)
			estado.save()
			return redirect('estado_list')
	else:
		form = EstadoForm(instance=estado)
	return render(request, 'pgen/estado_new.html', {'form': form})

@login_required
def estado_remove(request, pk):
	estado = get_object_or_404(Estado, pk=pk)
	estado.delete()
	return redirect('estado_list')




##### Views Cidade #####

@login_required
def cidade_new(request):
	if request.method == 'POST':
		form = CidadeForm(request.POST)
		if form.is_valid():
			cidade_new = form.save(commit=False)
			cidade_new.save()
			return redirect('cidade_list')
	else:
		form = CidadeForm()
	return render(request,'pgen/cidade_new.html', {'form': form})

@login_required
def cidade_list(request):
	cidade = Cidade.objects.all()
	return render(request, 'pgen/cidade_list.html', {'cidades': cidade})

@login_required
def cidade_edit(request, pk):
	cidade = get_object_or_404(Cidade, pk=pk)
	if request.method == "POST":
		form = CidadeForm(request.POST, instance=cidade)
		if form.is_valid():
			cidade = form.save(commit=False)
			cidade.save()
			return redirect('cidade_list')
	else:
		form = CidadeForm(instance=cidade)
	return render(request, 'pgen/cidade_new.html', {'form': form})

@login_required
def cidade_remove(request, pk):
	cidade = get_object_or_404(Cidade, pk=pk)
	cidade.delete()
	return redirect('cidade_list')





##### Views Cidade #####

@login_required
def sede_new(request):
	if request.method == 'POST':
		form = SedeForm(request.POST)
		if form.is_valid():
			sede_new = form.save(commit=False)
			sede_new.save()
			return redirect('sede_list')
	else:
		form = SedeForm()
	return render(request,'pgen/sede_new.html', {'form': form})

@login_required
def sede_list(request):
	sede = Sede.objects.all()
	return render(request, 'pgen/sede_list.html', {'sedes': sede})

@login_required
def sede_edit(request, pk):
	sede = get_object_or_404(Sede, pk=pk)
	if request.method == "POST":
		form = SedeForm(request.POST, instance=sede)
		if form.is_valid():
			sede = form.save(commit=False)
			sede.save()
			return redirect('sede_list')
	else:
		form = SedeForm(instance=sede)
	return render(request, 'pgen/sede_new.html', {'form': form})

@login_required
def sede_remove(request, pk):
	sede = get_object_or_404(Sede, pk=pk)
	sede.delete()
	return redirect('sede_list')
































