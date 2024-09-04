from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306245592',
        'name': 'Christopher Matthew Hendarson',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)