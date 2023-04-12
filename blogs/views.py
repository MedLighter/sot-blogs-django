from django.contrib import messages
from django.shortcuts import HttpResponseRedirect, render, get_object_or_404
from .forms import UserCreateArtForm, UserCreateCommentForm
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
            messages.success(request, 'Вы успешно создали статью!')
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
    comment_for_art = comment.objects.filter(article_id = article_id)
    if request.method == 'POST':
        form = UserCreateCommentForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = UserCreateCommentForm
        
    context = {
        'article': article_detail,
        'comment': comment_for_art,
        'form': form
    }
    return render(request, 'blogs/article_detail.html', context)


def personal_article(request):
    articles = article.objects.filter(user_creator=request.user)
    context = {
        'title': 'Мои статьи',
        'articles': articles,
    }
    return render(request, 'blogs/personal_article.html', context)


def delete_article(request, article_id):
    print(request.META)
    article_persone = article.objects.get(id=article_id)
    if article_persone.user_creator == request.user:
        article_persone.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))