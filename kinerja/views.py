from django.shortcuts import render, redirect
from django.contrib import messages

from .models import *
from .forms import BuatUserForm

from django.contrib.auth.decorators import login_required
from .decorators import *

from django.contrib.auth import authenticate, login, logout

@unauthenticated_user
def registerPage(request):
    form = BuatUserForm() 
    if request.method == "POST":
        form = BuatUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, 'User "' + username + '" berhasil dibuat')
            return redirect('login')
            
    context = {
        'form': form
    }
    return render(request, 'kinerja/register.html', context)

@unauthenticated_user
def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username atau Password salah!')

    context = {}
    return render(request, 'kinerja/login.html', context)

def logoutPage(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    pegawai = request.user.pegawai
    penilai = pegawai.penilai_set.get()
    target_kegiatan = pegawai.targetkegiatan_set.all()

    print(target_kegiatan)
    context = {
        'pegawai': pegawai,
        'penilai': penilai,
        'target_kegiatan': target_kegiatan
    }
    
    return render(request, 'kinerja/dashboard.html', context)
