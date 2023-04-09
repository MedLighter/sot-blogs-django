from django import forms

from blogs.models import article, section, comment

class UserCreateArtForm(forms.ModelForm):
    title_article = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Введите название статьи'
    }))
    text_article = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control area-for-txtart ', 'placeholder': 'Введите текст статьи'
    }))
    image = forms.ImageField(widget=forms.ClearableFileInput(
        attrs={'class': 'custom-file-input',
               'id': 'image-upload',
               'multiplay': True,
               }),
        required=False
    )
    section_id = forms.ModelChoiceField(queryset=section.objects.all())
    
    
    class Meta:
        model = article
        fields = ("title_article", "text_article", "image", "section_id")


class UserCreateCommentForm(forms.ModelForm):
    comment_text = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control area-for-txtart ', 'placeholder': 'Введите текст комментарий'
    }))


    class Meta:
        model = comment
        fields = ("comment_text",)
        
        
    