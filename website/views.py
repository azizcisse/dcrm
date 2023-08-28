from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
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
        return render(request, 'home.html', {})




def logout_user(request):
        logout(request) 
        messages.success(request, "Vous avez été déconnecté...")
        return redirect('home')
 
 
def register_user(request):
     return render(request, 'home.html', {})