from django.shortcuts import render, redirect
from .forms import UsuarioForm, ProductoForm, TiendaForm
from .models import Usuario, Producto, Tienda

def index(request):
    usuario_form = UsuarioForm()
    producto_form = ProductoForm()
    tienda_form = TiendaForm()
    return render(request, 'index.html', {
        'usuario_form': usuario_form,
        'producto_form': producto_form,
        'tienda_form': tienda_form,
    })

def usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios.html', {'usuarios': usuarios})

def productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos.html', {'productos': productos})

def tiendas(request):
    tiendas = Tienda.objects.all()
    return render(request, 'tiendas.html', {'tiendas': tiendas})


def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UsuarioForm()
    return render(request, 'crear_usuario.html', {'form': form})

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductoForm()
    return render(request, 'crear_producto.html', {'form': form})

def crear_tienda(request):
    if request.method == 'POST':
        form = TiendaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TiendaForm()
    return render(request, 'crear_tienda.html', {'form': form})

def buscar(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        if query:
            usuarios = Usuario.objects.filter(nombre__icontains=query)
            return render(request, 'buscar.html', {'usuarios': usuarios, 'query': query})
    return redirect('index')