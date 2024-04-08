from django.shortcuts import render


def home(request):
    print(request)
    return render(request, 'home_page.html')


def pr(request):
    print(request)
    return render(request, 'home_page.html')


