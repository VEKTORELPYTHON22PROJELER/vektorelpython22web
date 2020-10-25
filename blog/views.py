from django.shortcuts import render, get_object_or_404,redirect
from .models import GonderiModel
from django.views.generic.edit import CreateView
#--------------------------
from .forms import GonderiForm
from django.utils import timezone

def gonderiliste(request):
    gonderiler=GonderiModel.objects.all()
    return render(request,"blog/liste.html",{"gonderis":gonderiler})

def gonderidetay(request,pk):
    #gonderi=GonderiModel.objects.get(pk=pk)
    gonderi=get_object_or_404(GonderiModel,pk=pk)
    return render(request,"blog/gonderidetay.html",{"gonderi":gonderi})

def yeniGonderi(request):
    if request.method == "POST":
        form = GonderiForm(request.POST)
        if form.is_valid():
            gonderi = form.save(commit=False)
            gonderi.yazar = request.user
            gonderi.yayimzaman = timezone.now()
            gonderi.save()
            return redirect("gonderidetay",pk=gonderi.pk)
    else:
        form = GonderiForm()
    return render(request,'blog/yenigonderi.html',{"form":form})


def gonderiduzenle(request,pk):
    gonderi=get_object_or_404(GonderiModel,pk=pk)
    if request.method == "POST":
        form = GonderiForm(request.POST,instance=gonderi)
        if form.is_valid():
            gonderi = form.save(commit=False)
            gonderi.yazar = request.user
            gonderi.yayimzaman = timezone.now()
            gonderi.save()
            return redirect("gonderidetay",pk=gonderi.pk)
    else:
        form = GonderiForm(instance=gonderi)
    return render(request,'blog/gonderiduzenle.html',{"form":form})

class CreateGonderiView(CreateView):
    model = GonderiModel
    form_class= GonderiForm
    template_name = "blog/yenigonderi.html"
    success_url = "blog/gonderidetay.html"