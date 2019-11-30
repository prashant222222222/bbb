from django.shortcuts import render
from .forms import NewUserForm

def index(request):
    return render(request,'os1/index.html')

def help(request):
    helpdict = {'help_insert':'HELP PAGE'}
    return render(request,'os1/help.html',context=helpdict)

def users(request):
    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')

    return render(request,'os1/users.html',{'form':form})
