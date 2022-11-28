from django.shortcuts import render


def error_404(request, exception):
        data = {}
        return render(request,'pages/error_404.html', data)

# def error_500(request, exception):
#         data = {}
#         return render(request,'pages/error_500.html', data)



def index_view(request):
    return render(request, 'pages/index.html', {})

def contact_view(request):
    return render(request, 'pages/contact.html', {})
