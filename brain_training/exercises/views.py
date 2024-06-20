from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'exercises/home.html')


def memory(request):
    return render(request, 'exercises/memory.html')


def attention(request):
    return render(request, 'exercises/attention.html')


def problem_solving(request):
    return render(request, 'exercises/problem_solving.html')


def creativity(request):
    return render(request, 'exercises/creativity.html')