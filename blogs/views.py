from django.shortcuts import HttpResponseRedirect, render, get_object_or_404
from .forms import UserCreateArtForm
from .models import section, article, comment


def news(request):
    context = {
        'title': 'Новости',
        'sections': section.objects.all(),
        'articles': article.objects.all(),
        'comments': comment.objects.all(),
    }
    return render(request, 'blogs/news.html', context)

def new_art(request):
    if request.method == "POST":
        form = UserCreateArtForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user_creator = request.user
            form.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = UserCreateArtForm()
    context = {
        'title': "Новая статья",
        'form': form,
        'sections': section.objects.all(),
    }
    return render(request, 'blogs/new_article.html', context)


def article_detail(request, article_id):
    article_detail = get_object_or_404(article, id=article_id)
    return render(request, 'blogs/article_detail.html', {'article': article_detail})