from django.shortcuts import render
from .models import Asistencias

def registrar(request):
    if request.method == "POST":
        asistencias = Asistencias(
         tipo_documento =request.POST["tipodocumento"],
         documento = request.POST["documento"],
         nombres = request.POST["nombres"],
         apellidos = request.POST["apellidos"],
         whatsapp = request.POST["whatsapp"],
         fecha =request.POST["fecha"],
         asistio = request.POST["asisitio"]
        )
        asistencias.save()

    return render(
        request,
        "asistencias/registro.html"
    )


def listar(request):

    asistencias = Asistencias.objects.all()

    return render(
        request,
        "asistencias/lista.html",
        {"asistencias": asistencias}
    )

def detalle(request, id):

    asistencias = Asistencias.objects.get(id=id)

    return render(
        request,
        "asistencias/detalle.html",
        {"asistencias": asistencias}
    )


def editar(request, id):

    asistencias = Asistencias.objects.get(id=id)

    if request.method == "POST":
        asistencias.tipo_documento =request.POST["tipodocumento"]
        asistencias.documento = request.POST["documento"]
        asistencias.nombres = request.POST["nombres"]
        asistencias.apellidos = request.POST["apellidos"]
        asistencias.whatsapp = request.POST["whatsapp"]
        asistencias.fecha =request.POST["fecha"]
        asistencias.asistio = request.POST["asisitio"]
                
        asistencias.save()

        return render(
            request,
            "asistencias/detalle.html",
            {"asistencias": asistencias}
        )

    return render(
        request,
        "asistencias/formulario.html",
        {"asistencias": asistencias}
    )


def eliminar(request, id):

    asistencias = Asistencias.objects.get(id=id)

    asistencias.delete()

    asistencias = Asistencias.objects.all()

    return render(
        request,
        "asistencias/lista.html",
        {"asistencias": asistencias}
    )