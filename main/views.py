from django.shortcuts import render, HttpResponse

def home(request):
   return render(request, 'main/index.html')
# Create your views here.
def about(request):
   return render(request, 'main/about.html')
def contacts(request):
   return render(request, 'main/contacts.html')