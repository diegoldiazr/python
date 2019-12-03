from django.http import HttpResponse
import datetime
#from django.template import Template
from .clases.persona import Persona

#importamos el cargador de plantillas
from django.template import loader, Context



#cada funcion en esta clase se llama vista.
#el primer parametro siempre es una requets de tipo HttpRequest
#y siempre devolvemos un HttpResponse
def saludo(request):

    nombre = "Pedro"
    apellido = "Díaz"
    persona = Persona(nombre, apellido)
    temas_curso = [
        "Plantillas", 
        "Modelos", 
        "Formularios",
        "Vistas",
        "Despliegues"
    ]


    #obtenemos la plantilla
    #doc_externo = open("C:/_DIEGO_DIAZ/2PERSONAL/workspace-vscode/pilinf_django_1/python/pilinf_django_1/pilinf_django_1/plantillas/miplantilla.html")
    #plt=Template(doc_externo.read())
    #doc_externo.close()

    doc_externo = loader.get_template('miplantilla.html')
    
    #creamos el contexto. Aqui es donde pasamos los datos a la vista
    #ctx=Context({
    #    "nombre_persona":nombre, 
    #    "apellido_persona":apellido,
    #    "apellido2_persona":"asiTambienSePuede",
    #    "objeto_valor": persona,
    #    "temas": temas_curso
    #})

    diccionario = {
        "nombre_persona":nombre, 
        "apellido_persona":apellido,
        "apellido2_persona":"asiTambienSePuede",
        "objeto_valor": persona,
        "temas": temas_curso
    }
    documento = doc_externo.render(diccionario)

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
