from django.shortcuts import render
from django.views.generic import(DetailView)
from django.contrib.auth.decorators import login_required
from .models import Log

def login_cadastro(request):
    return render(request, 'registros/login_cadastro.html', {'title': 'Home'})

@login_required(login_url='registros-login-cadastro')
def central_errors(request):
    logs = Log.objects.all()

    context = {'logs': logs}

    return render(request, 'registros/home.html', context=context)


class LogDetailView(DetailView):
    model = Log
    template_name = 'registros/detail.html'