from django import forms
from .models import Video, Comment


class VideoForm(forms.ModelForm):

    class Meta:

        model = Video
        fields = ('title', 'name', 'description', 'rating',
                  'length', 'video_file', 'premium',)


class CommentForm(forms.ModelForm):

    class Meta:

        model = Comment
        fields = ('content',)
        exclude = ('video', 'user', 'created_on', 'visible',)

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            placeholders = {
                'content': 'Comment',
            }

            for field in self.fields:
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].label = False
