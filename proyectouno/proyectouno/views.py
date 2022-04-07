from django.http import HttpResponse

def saluda(request): 

    return HttpResponse('Hola a todos! que facil es programar en Djnago')