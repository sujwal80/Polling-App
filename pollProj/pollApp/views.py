from django.shortcuts import render, redirect
from .models import Question
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    return render(request, 'home.html', {'polls':Question.objects.all()})

@login_required(login_url='login_page')
def vote(request, pk):
    if request.method == 'POST':
        form = get_object_or_404(Question, pk = pk)
        selected_option = request.POST.get('poll')
        
        if selected_option[-1:] == '1':
            form.count1 += 1
        
        elif selected_option[-1:] == '2':
            form.count2 += 1

        elif selected_option[-1:] == '3':
            form.count3 += 1

        else:
            return HttpResponse(400, 'Invalid Form!')
        
        form.save()
        return redirect('result_page', form.id)


    return render(request, 'vote.html', {'poll': Question.objects.get(id=pk)})

@login_required(login_url='login_page')
def result(request, pk):
    return render(request, 'result.html', {'poll': Question.objects.get(id=pk)})


def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')

    return render(request, 'register.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('/')