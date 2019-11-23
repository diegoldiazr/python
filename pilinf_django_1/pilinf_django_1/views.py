from django.http import HttpResponse

#cada funcion en esta clase se llama vista.
#el primer parametro siempre es una requets de tipo HttpRequest
#y siempre devolvemos un HttpResponse
def saludo(request):
    return HttpResponse("hola quilloooooo")

def despedida(request):
    return HttpResponse("adiooooooos")