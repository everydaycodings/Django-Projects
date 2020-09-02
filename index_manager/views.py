from django.shortcuts import render, HttpResponse

# Create your views here.
def error404(request, exception):
    return render(request, "error404.html")

def index(request):
    return render(request, "index.html")