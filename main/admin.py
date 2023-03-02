from django.contrib import admin
from .models import section, article, comment, photo_for_article

admin.site.register(section)
admin.site.register(article)
admin.site.register(comment)
admin.site.register(photo_for_article)
