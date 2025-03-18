from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def contact(request):  # Ensure 'request' is included
    return render(request, 'core/contact.html')
