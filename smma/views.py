
from django.shortcuts import render

# Create your views here.
def smma(request):
    return render(request, 'smma/main.html' )

def services(request):
    return render(request, 'smma/services.html' )