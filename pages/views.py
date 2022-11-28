from django.shortcuts import render

def index_view(request):
    return render(request, 'pages/index.html', {})


def contact_view(request):
    return render(request, 'pages/contact.html', {})
