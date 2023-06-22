from django.shortcuts import render, redirect
from .models import *
from random import sample
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')

def Login(request):
    if request.user.is_authenticated:
        return redirect("index")
    else:
        if request.method=="POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("index")
        else:
            return render(request, 'login.html')

@login_required(login_url='login')
def add_question(request):
    if request.method == "POST":
        short_ques = (request.POST['short_ques']).split('\n')
        comp_ques = (request.POST['comp_ques']).split('\n')
        
        short_ques = [i.replace('\r', '') for i in short_ques]
        for i in short_ques:
            new_ques = Short_question()
            new_ques.ques = i
            new_ques.save()
        comp_ques = [i.replace('\r', '') for i in comp_ques]
        for i in comp_ques:
            new_ques = Comp_question()
            new_ques.ques = i
            new_ques.save()
        print(short_ques)
    return render(request, 'add_question.html')

@login_required(login_url='login')
def view_question(request):
    s_ques = Short_question.objects.all()
    c_ques = Comp_question.objects.all()
    con = {
        's_ques' : s_ques,
        'c_ques' : c_ques,
    }
    return render(request, 'view.html', con)

@login_required(login_url='login')
def generate(request):
    s_ques = Short_question.objects.all()
    c_ques = Comp_question.objects.all()

    s_ques_num = sample(range(1, len(s_ques)), 5)
    c_ques_num = sample(range(1, len(c_ques)), 3)
    s_ques_list = [s_ques[i] for i in s_ques_num]
    c_ques_list = [c_ques[i] for i in c_ques_num]

    con = {
        "short_list" : s_ques_list,
        "comp_list" : c_ques_list
    }
    return render(request, 'generate.html', con)
@login_required(login_url='login')
def Logout(request):
    logout(request)
    return redirect("index")