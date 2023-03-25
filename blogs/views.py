from django.shortcuts import HttpResponseRedirect, render
from .forms import UserCreateArtForm
from .models import section


def news(request):
    context = {
        'title': 'Новости'
    }
    return render(request, 'blogs/news.html', context)

def new_art(request):
    if request.method == "POST":
        form = UserCreateArtForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = UserCreateArtForm()
    sections = section.objects.all()
    context = {
        'title': "Новая статья",
        'form': form,
        'sections': sections,
    }
    return render(request, 'blogs/new_article.html', context)