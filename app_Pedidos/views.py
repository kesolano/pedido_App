from django.shortcuts import render, redirect
from .models import Pedido
from django import forms

# Formulario basado en el modelo Pedido
class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'  # Todos los campos del modelo

def crear_pedido(request):
    if request.method == 'POST':
        print("Datos recibidos:", request.POST)
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("pedido_exitoso")  # Redirige a la página de éxito (por nombre)
    else:
        form = PedidoForm()
    return render(request, 'app_Pedidos/pedido.html', {'form': form})
