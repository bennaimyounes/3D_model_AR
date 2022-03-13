from django.shortcuts import render
from .models import Document

# Create your views here.
def index(request):
    obj=Document.objects.all()
    context={
        "obj":obj,
    }
    return render(request,"index.html",context)