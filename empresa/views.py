from django.contrib import messages
from django.contrib.messages import constants
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .models import *

# Create your views here.


def nova_empresa(request):
    if request.method == "GET":
        techs = Tecnologia.objects.all()
        return render(request, 'nova_empresa.html', {'techs': techs})

    elif request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        cidade = request.POST.get('cidade')
        endereco = request.POST.get('endereco')
        nicho = request.POST.get('nicho')
        caracteristicas = request.POST.get('caracteristicas')
        tecnologias = request.POST.getlist('tecnologias')
        logo = request.FILES.get('logo')

        if (len(nome.strip()) == 0 or len(email.strip()) == 0 or len(cidade.strip()) == 0 or len(endereco.strip()) == 0 or len(nicho.strip()) == 0 or len(caracteristicas.strip()) == 0 or (not logo)):
            messages.add_message(request, constants.ERROR,
                                 'Preencha todos os campos')
            return redirect('/home/nova_empresa')

        if logo.size > 100_000_000:
            messages.add_message(request, constants.ERROR,
                                 'A logo da empresa deve ter menos de 10MB')
            return redirect('/home/nova_empresa')

        if nicho not in [i[0] for i in Empresa.choices_nicho_mercado]:
            messages.add_message(request, constants.ERROR,
                                 'Nicho de mercado inválido')
            return redirect('/home/nova_empresa')

        empresa = Empresa(logo=logo,
                          nome=nome,
                          email=email,
                          cidade=cidade,
                          endereco=endereco,
                          nicho_mercado=nicho,
                          caracteristica_empresa=caracteristicas)
        empresa.save()
        empresa.tecnologia.add(*tecnologias)
        empresa.save()
        messages.add_message(request, constants.SUCCESS,
                             'Empresa cadastrada com sucesso')
        return redirect('/home/empresas')


def empresas(request):
    tecnologias_filtrar = request.GET.get('tecnologias')
    nome_filtrar = request.GET.get('nome')
    empresas = Empresa.objects.all()

    if tecnologias_filtrar:
        empresas = empresas.filter(tecnologia=tecnologias_filtrar)

    if nome_filtrar:
        empresas = empresas.filter(nome__icontains=nome_filtrar)

    tecnologias = Tecnologia.objects.all()
    return render(request, 'empresa.html', {'empresas': empresas, 'tecnologias': tecnologias})


def excluir_empresa(request, id):
    empresa = Empresa.objects.get(id=id)
    empresa.delete()
    messages.add_message(request, constants.SUCCESS,
                         'Empresa excluída com sucesso')
    return redirect('/home/empresas')


def empresa(request, id):
    empresa_unica = get_object_or_404(Empresa, id=id)
    empresas = Empresa.objects.all()
    tecnologias = Tecnologia.objects.all()
    vagas = Vaga.objects.filter(empresa_id = id)
    return render(request, 'empresa_unica.html', {'empresa': empresa_unica, 
                                                 'tecnologias': tecnologias,
                                                 'empresas': empresas,
                                                 'vagas': vagas})