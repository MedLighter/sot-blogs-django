from django.db import models
from users.models import User


class section(models.Model):
    section_name = models.CharField("Название раздела", max_length=50)

    def __str__(self):
        return self.section_name

    class Meta:
        verbose_name = "Раздел"
        verbose_name_plural = "Разделы"


class article(models.Model):
    title_article = models.CharField("Название статьи", max_length=75)
    section_id = models.ForeignKey(section, null=True, verbose_name='Раздел', on_delete=models.PROTECT)
    text_article = models.TextField("Статья")
    date_publish = models.DateTimeField("Дата публикации", auto_now_add=True, null=True, blank=True)
    image = models.ImageField(upload_to='photoForArticle', null=True, blank=True)
    user_creator = models.ForeignKey(User, verbose_name='Создатель статьи', on_delete=models.PROTECT)
    

    def __str__(self):
        return self.title_article

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"





class comment(models.Model):
    article_id = models.ForeignKey(article, on_delete=models.CASCADE)
    user_message = models.ForeignKey(User, verbose_name='Создатель комментария', on_delete=models.PROTECT)
    comment_text = models.TextField("Текст комментария", max_length=200)
    comment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Коментарий"
        verbose_name_plural = "Коментарии"

    def __str__(self):
        return self.author_name
