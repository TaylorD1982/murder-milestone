from django.shortcuts import render

# Create your views here.
def index(request):
    """A view that displays the index page"""
    return render(request, "index.html")

def locations(request):
    """Return the locations.html file"""
    return render(request, "locations.html")
    
def contact(request):
    """Return the contact.html file"""
    return render(request, "contact.html")