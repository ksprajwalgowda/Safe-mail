from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DeleteView 
from .forms import *
from .models import *
# Create your views here.
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate




def home(request):
    return render(request ,"index.html")

def compose(request,sen=""):

    dic = {
        "sen": sen
    }
     
    if request.method == 'POST': 
        Userm = get_user_model()
        users = Userm.objects.values()
        names = []
        for i in range(len(users)):
            names.append(users[i]["username"])

        
         
        to = request.POST['to']
        if to not in names:
            di = {
                "sen":"username does not exist"
            }
            return render(request,'compose.html',di)


        sender = request.user.username
        mes = request.POST['message']
        sub = request.POST['sub']
        
        
        content = Mailbox(to=to,sender=sender,sub=sub, message = mes)
       
        
        content.save()
        return redirect('mail:home')
     
    return render(request,'compose.html',dic)


def inbox(request):

    obj = Mailbox.objects.filter(to = request.user.username).order_by('-id')

    dic  = {
        "obj":obj
    }

    return render(request,'inbox.html',dic)



def sent(request):
    obj = Mailbox.objects.filter(sender = request.user.username).order_by('-id')

    dic  = {
        "obj":obj
    }

    return render(request,'sent.html',dic)


class Maildelete(DeleteView):
    model = Mailbox
    template_name = "delete.html"
    success_url ="/inbox"


# def getin(request):
#     if request.method == 'POST': 
        
        
         
#         usernane = request.POST['username']
        


        
#         password = request.POST['password']
        
        
#         content = authenticate(username=usernane, password=password)
#         if content is not None:
#             return redirect('mail:home')
     
            
#         else:
#             return render(request,'getin.html')
#             # No backend authenticated the credentials
        
        
        
#     return render(request,'getin.html')
