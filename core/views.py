from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import Servicio
from .forms import SolicitarInfoForm


def solicitar_info(request, servicio_id):
    servicio = get_object_or_404(Servicio, id=servicio_id)

    if request.method == 'POST':
        form = SolicitarInfoForm(request.POST)
        if form.is_valid():
            solicitud = form.save(commit=False)
            solicitud.servicio = servicio  # Vincula la solicitud al servicio correcto
            solicitud.save()

            mensaje = (
    f"Nueva solicitud de información:\n\n"
    f"Nombre: {solicitud.nombre}\n"
    f"Email: {solicitud.email}\n"
    f"Teléfono: {solicitud.telefono}\n"
    f"¿Cuándo quiere comenzar?: {solicitud.cuando_comenzar}\n\n"
    f"Requerimientos:\n{solicitud.requerimientos}"
)

            send_mail(
                subject="Solicitud de Información - CBC E.I.R.L.",
                message=mensaje,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=['cbc_web@hotmail.com'],
                fail_silently=False,
            )

            return redirect('gracias')
        else:
            # Si el formulario tiene errores, imprime en consola para debug
            print("Errores del formulario:", form.errors)
    else:
        form = SolicitarInfoForm()

    return render(request, 'solicitar_info.html', {
        'form': form,
        'servicio': servicio
    })


def inicio(request):
    return render(request, 'inicio.html')


def servicios(request):
    
    servicios = Servicio.objects.all()
    return render(request, 'servicios.html', {'servicios': servicios})


def contacto(request):
    return render(request, 'contacto.html')


def gracias(request):
    return render(request, 'gracias.html')
