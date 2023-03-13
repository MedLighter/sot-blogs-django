from django.shortcuts import render


def index(request):
    context = {
        'title': 'Главная'
    }
    return render(request, 'main/index.html', context)


def achivments(request):
    context = {
        'title': 'Достижения'
    }
    return render(request, 'main/achivments.html', context)


def items_chests(request):
    context = {
        'title': 'Сундуки'
    }
    return render(request, 'main/items_chests.html', context)

def items_weapons(request):
    context = {
        'title': 'Оружие'
    }
    return render(request, 'main/items_weapons.html', context)


def npc(request):
    context = {
        'title': 'Существа'
    }
    return render(request, 'main/npc.html', context)


def ships(request):
    context = {
        'title': 'Корабли'
    }
    return render(request, 'main/ships.html', context)


def storytellings_seasons(request):
    context = {
        'title': 'Сезоны'
    }
    return render(request, 'main/storytellings_seasons.html', context)

def storytellings_TallTales(request):
    context = {
        'title': 'TallTales'
    }
    return render(request, 'main/storytellings_TallTales.html', context)
