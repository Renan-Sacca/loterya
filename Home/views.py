from django.shortcuts import render
from .models import fichas
def index(request):
    
    ficha = fichas.objects.all()
    
    dados={
        'fichas' : ficha
    }

    if request.user.is_authenticated:
        return render(request,'dashboard.html',dados)
    else:
        return render(request,'index.html', dados)


    

