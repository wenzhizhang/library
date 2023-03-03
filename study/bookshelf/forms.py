from django import forms
from .models import Comment, Book, BookImage


class BookForm(forms.Form):
    registered = forms.Select()

    def update_registered_status(self):
        pass


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')


class BaseMultiImageFormSet(forms.BaseModelFormSet):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.queryset = BookImage.objects.none()

MultiImageForm = forms.modelformset_factory(BookImage, fields=('image', ), formset=BaseMultiImageFormSet)