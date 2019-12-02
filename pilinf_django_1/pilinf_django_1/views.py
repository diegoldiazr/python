from django.http import HttpResponse
import datetime
from django.template import Template, Context

#esto es una clase
class Persona(object):
    #esto es el constructor de la clase
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

#cada funcion en esta clase se llama vista.
#el primer parametro siempre es una requets de tipo HttpRequest
#y siempre devolvemos un HttpResponse
def saludo(request):

    nombre = "Juan"
    apellido = "Díaz"
    persona = Persona(nombre, apellido)
    

    #obtenemos la plantilla
    doc_externo = open("C:/_DIEGO_DIAZ/2PERSONAL/workspace-vscode/pilinf_django_1/python/pilinf_django_1/pilinf_django_1\plantillas/miplantilla.html")
    plt=Template(doc_externo.read())
    doc_externo.close()
    
    #creamos el contexto. Aqui es donde pasamos los datos a la vista
    ctx=Context({
        "nombre_persona":nombre, 
        "apellido_persona":apellido,
        "apellido2_persona":"asiTambienSePuede",
        "objeto_valor": persona
    })
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