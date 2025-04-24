from django.shortcuts import render


def index(request):
    return render(request, 'website/index.html')


def price(request):
    return render(request, 'website/price.html')


def tutor(request):
    return render(request, 'website/tutor.html')


def why_ngs(request):
    return render(request, 'website/why-ngs.html')
