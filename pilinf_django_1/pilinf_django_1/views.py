from django.http import HttpResponse
import datetime
from django.template import Template, Context

#cada funcion en esta clase se llama vista.
#el primer parametro siempre es una requets de tipo HttpRequest
#y siempre devolvemos un HttpResponse
def saludo(request):
    #obtenemos la plantilla
    doc_externo = open("C:/_DIEGO_DIAZ/2PERSONAL/workspace-vscode/pilinf_django_1/python/pilinf_django_1/pilinf_django_1\plantillas/miplantilla.html")
    plt=Template(doc_externo.read())
    doc_externo.close()
    
    #creamos el contexto
    ctx=Context()
    documento = plt.render(ctx)

    return HttpResponse(documento)

def despedida(request):
    return HttpResponse("adiooooooos")

#en python la convencion es que en vez de escribir como nombre de 
#funcion dameFecha se pone dame_fecha
def dame_fecha(request):
    fecha_actual=datetime.datetime.now()
    documento = """<html>
    <body>
    <h2>
    Fecha y hora actuales %s
    </h2>
    </body>
    </html>""" % fecha_actual
    
    return HttpResponse(documento)


def calcula_edad(request, edadActual, anno):

    periodo = anno - 2019
    resultado = periodo + edadActual
    
    documento = """<html>
    <body>
    <h2>
    En %s tendras %s años
    </h2>
    </body>
    </html>""" % (anno, resultado)
    
    return HttpResponse(documento)