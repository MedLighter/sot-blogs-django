from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def achivments(request):
    return render(request, 'main/achivments.html')


def items_chests(request):
    return render(request, 'main/items_chests.html')

def items_weapons(request):
    return render(request, 'main/items_weapons.html')


def npc(request):
    return render(request, 'main/npc.html')


def ships(request):
    return render(request, 'main/ships.html')


def storytellings_seasons(request):
    return render(request, 'main/storytellings_seasons.html')

def storytellings_TallTales(request):
    return render(request, 'main/storytellings_TallTales.html')
