from django.shortcuts import render


def news(request):
    context = {
        'title': 'Новости'
    }
    return render(request, 'blogs/news.html', context)

def new_art(request):
    # if request.method == "POST":
        # form = 
    context = {
        'title': "Новая статья"
    }
    return render(request, 'blogs/new_article.html', context)