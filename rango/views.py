from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):

    context_dict = {'boldmessage' : "I am bold font from context "}
    #return HttpResponse("Rango says hey world")
    return render(request, 'rango/index.html', context_dict)


def about(request):

    return HttpResponse("About Rango mm lemme think...")