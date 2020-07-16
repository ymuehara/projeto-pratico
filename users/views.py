from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserCadastroForm


def cadastro(request):
    if request.method == 'POST':
        form = UserCadastroForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'{username} o seu cadastro foi criado'
            )
            return redirect('login')
    else:
        form = UserCadastroForm()
    return render(request, 'users/cadastro.html', {'form':form})
