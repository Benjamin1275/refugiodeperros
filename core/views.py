from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import ensure_csrf_cookie
from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'core/home.html')

@login_required
def dogs(request):
    return render(request, 'core/dogs.html')


def exit(request):
    logout(request)
    return redirect('home')

@ensure_csrf_cookie
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            if user is not None:
                login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/register.html', {'form': form})



def health_check(request):
    return HttpResponse("OK")


"""
@csrf_exempt: Este decorador marca una vista como exenta de la protección CSRF proporcionada por el middleware. 
Úsalo con precaución ya que desactiva la protección CSRF para esa vista específica.
@csrf_protect: Decorador que proporciona la protección de CsrfViewMiddleware a una vista1. 
Asegúrate de que solo las vistas que necesitan protección CSRF lo tengan.
@requires_csrf_token: Si csrf_token no funciona porque CsrfViewMiddleware.process_view no se ha ejecutado, 
este decorador garantiza que la etiqueta de plantilla funcione correctamente.
@ensure_csrf_cookie: Este decorador fuerza a una vista a enviar la cookie CSRF, 
lo cual es útil si tu formulario CSRF se encuentra en una página diferente a la que procesa la solicitud.
"""