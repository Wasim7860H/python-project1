from django.shortcuts import render

# Create your views here.
def home(request):
    context = {'home': 'active'}
    return render(request, 'core/home.html')
def contact(request):
    return render(request, 'core/contact.html')


