from django import forms
from .models import Video


class VideoForm(forms.ModelForm):

    class Meta:

        model = Video
        fields = ('title', 'name', 'description', 'rating',
                  'length', 'video_file',)
    
        # def __init__(*args, **kwargs):
        # super().__init__(*args, **kwargs)
        # placeholders = {
        #     'title': 'Title',
        #     'name': 'Name',
        #     'description': 'Description',
        #     'rating': 'Rating',
        #     'length': 'Length',
        #     'video_file': 'Clip',
        # }

        # self.fields['title'].widget.attrs['autofocus'] = True
        # for field in self.fields:
        #     if self.fields[field].required:
        #         placeholder = f'{placeholders[field]}'
        #     else:
        #         placeholder = placeholders[field]
        #     self.fields[field].label = False
