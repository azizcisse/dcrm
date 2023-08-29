from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from website.forms import SignUpForm
from .models import Record




def home(request):
    records = Record.objects.all()
    #Vérification pour voir si tu es connecté
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        # Si tu es authentifié
        user = authenticate(request, username=username, password=password) 
        if user is not None:
            login(request, user)
            messages.success(request, "Félicitation vous etes conectés!!!")
            return redirect('home')
        else:
            messages.success(request, "Une erreur s'est produite lors de la connexion, veuillez réessayer...")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records':records})




def logout_user(request):
        logout(request) 
        messages.success(request, "Vous avez été déconnecté...")
        return redirect('home')
 
 
def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #Il s'authentifie et se connecte
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Félicitations, Inscription réussie, Bienvenue au CRM-DJANGO")
            return redirect('home') 
    else:
         form = SignUpForm()           
         return render(request, 'register.html', {'form':form})
    return render(request, 'register.html', {'form':form})



def customer_record(request, pk):
    pass