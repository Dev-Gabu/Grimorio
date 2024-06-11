from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import View
from django.conf import settings


class Login(View):
    def get(self, request):
        contexto = {'mensagem':'login'}
        if request.user.is_authenticated:
            return redirect('/item')
        else:
            return render(request,'autenticacao.html', contexto)
    
    def post(self,request):

        usuario = request.POST.get('username',None)
        senha = request.POST.get('password',None)

        user = authenticate(request, username=usuario, password=senha)
        if user is not None:
            if user.is_active:
                return redirect("/item")

            return render(request, "autenticacao.html", {'mensagem':'Usuário Inativo'})
        return render(request, "autenticacao.html", {'mensagem':'Usuário ou senha inválidos'})
    
class Logout(View):
    def get(self, request):
        logout(request)
        return request(settings.LOGIN_URL)