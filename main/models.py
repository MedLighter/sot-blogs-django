from django.db import models


class section(models.Model):
    section_name = models.CharField("Название раздела", max_length=50)

    def __str__(self):
        return self.section_name

    class Meta:
        verbose_name = "Раздел"
        verbose_name_plural = "Разделы"


class article(models.Model):
    title_article = models.CharField("Название статьи", max_length=75)
    section_id = models.ForeignKey(section, null=True, on_delete=models.PROTECT)
    text_article = models.TextField("Статья")
    date_publish = models.DateTimeField("Дата публикации")

    def __str__(self):
        return self.title_article

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"


class photo_for_article(models.Model):
    path = models.ImageField(upload_to='photoForArticle')
    id_article = models.ForeignKey(article, on_delete=models.CASCADE)


class comment(models.Model):
    article_id = models.ForeignKey(article, on_delete=models.CASCADE)
    author_name = models.CharField("Имя автора", max_length=50)
    comment_text = models.TextField("Текст комментария", max_length=200)

    class Meta:
        verbose_name = "Коментарий"
        verbose_name_plural = "Коментарии"

    def __str__(self):
        return self.author_name



