from django.http import HttpResponse
import datetime

#cada funcion en esta clase se llama vista.
#el primer parametro siempre es una requets de tipo HttpRequest
#y siempre devolvemos un HttpResponse
def saludo(request):
    return HttpResponse("hola quilloooooo")

def despedida(request):
    return HttpResponse("adiooooooos")


def dameFecha(request):
    fecha_actual=datetime.datetime.now()
    documento = """<html>
    <body>
    <h2>
    Fecha y hora actuales %s
    </h2>
    </body>
    </html>""" % fecha_actual
    
    return HttpResponse(documento)