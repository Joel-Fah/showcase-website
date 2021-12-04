from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        'nbar': 'home',
    }
    return render(request, 'home.html', context)

def services(request):
    context = {
        'nbar': 'services',
    }
    return render(request, 'services.html', context)

def realisation(request):
    context = {
        'nbar': 'realisation',
    }
    return render(request, 'realisation.html', context)

def contact(request):
    context = {
        'nbar': 'contacts',
    }
    return render(request, 'contacts.html', context)

def about(request):
    context = {
        'nbar': 'about',
    }
    return render(request, 'about.html', context)