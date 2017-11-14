from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'counter/index.html')

def dashboard(request):
    return render(request, 'counter/dashboard.html')