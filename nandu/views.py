from django.shortcuts import render

# Create your views here.
def looping(request):
    d={'name':'Aishu','L':[11,22,33,77]}
    return render(request, 'looping.html', d)