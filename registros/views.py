from django.shortcuts import render
from django.views.generic import DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Log
from rest_framework import viewsets, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import LogModelSerializer
from rest_framework.filters import SearchFilter, OrderingFilter


def login_cadastro(request):
    return render(request, 'registros/login_cadastro.html', {'title': 'Home'})

@login_required(login_url='registros-login-cadastro')
def central_errors(request):
    logs = Log.objects.all()

    context = {'logs': logs}

    return render(request, 'registros/home.html', context=context)


class LogDetailView(LoginRequiredMixin, DetailView):
    model = Log
    template_name = 'registros/detail.html'


class LogCreateView(LoginRequiredMixin, CreateView):
    model = Log
    fields = ['level', 'descricao', 'origem', 'detalhes', 'ambiente', 'data', 'event']
    success_url = '/'


class LogUpdateView(LoginRequiredMixin, UpdateView):

    model = Log
    fields = ['level', 'descricao', 'origem', 'detalhes', 'ambiente', 'data', 'event']
    success_url = '/'


class LogDeleteView(LoginRequiredMixin, DeleteView):
    model = Log
    success_url = '/'


#API views
class LogApiViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Log.objects.all()
    serializer_class = LogModelSerializer


class LogListAPIView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Log.objects.all()
    serializer_class = LogModelSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('ambiente', 'level', 'descricao', 'origem')
    ordering_fields = ('level', 'ambiente')
