from django.shortcuts import render


def news(request):
    context = {
        'title': 'Новости'
    }
    return render(request, 'blogs/news.html', context)
