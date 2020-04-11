from django.shortcuts import render

# Create your views here.
def index(request):
    """A view that displays the index page"""
    return render(request, "index.html")

def locations(request):
    """Return the locations.html file"""
    return render(request, "locations.html")
    
def about(request):
    """Return the about.html file"""
    return render(request, "about.html")
    
def contact(request):
    """Return the contact.html file"""
    return render(request, "contact.html")