from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def achivments(request):
    return render(request, 'main/achivments.html')


def items(request):
    return render(request, 'main/items.html')


def npc(request):
    return render(request, 'main/npc.html')


def ships(request):
    return render(request, 'main/ships.html')


def storytellings(request):
    return render(request, 'main/storytellings.html')
