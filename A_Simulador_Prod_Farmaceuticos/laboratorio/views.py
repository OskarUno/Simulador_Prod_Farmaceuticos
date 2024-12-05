from django.shortcuts import render, redirect, get_object_or_404
from .models import Laboratorio
from .forms import LaboratorioForm
from django.contrib import messages



def index(request):
    laboratorios = Laboratorio.objects.all().order_by('id')
    if 'visitas' not in request.session:
        request.session['visitas'] = 0
    request.session['visitas'] += 1
    context = {
        'laboratorios': laboratorios,
        'visitas': request.session['visitas']
    }
    return render(request, 'laboratorio/index.html',  context)



def crear_o_editar_laboratorio(request, id = None):
    laboratorio = get_object_or_404(Laboratorio, id = id) if id else None
    
    if request.method == "POST":
        form = LaboratorioForm(request.POST, instance = laboratorio)
        if form.is_valid():
            form.save()
            if laboratorio:
                messages.success(request, 'El Laboratorio se ha sido actualizada con éxito!')
            else:  # 3.8
                messages.success(request, 'El Laboratorio se ha sido creada con éxito!')
            return redirect('laboratorio:index')  # Redirige a una pagina determinada
        
    else:  # 3.8
        form = LaboratorioForm(instance = laboratorio)
        context = {
            'form': form,
            'es_editar': laboratorio is not None
        }
    return render(request, 'laboratorio/crear_laboratorio.html', context)   


def eliminar_laboratorio(request, id):
    laboratorio = get_object_or_404(Laboratorio, id = id)
    
    if request.method == "POST":
        laboratorio.delete()
        return redirect('laboratorio:index')
    return render(request, 'laboratorio/eliminar_laboratorio.html', {'laboratorio': laboratorio})
