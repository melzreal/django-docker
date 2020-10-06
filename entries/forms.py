from django.forms import ModelForm
from .models import Entry

class EntryForm(ModelForm):
  class Meta:
    model = Entry
    fields = ('text', )

    # we want to add a class to our entry text, so we do it by overriding the entry widget attributes below
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['text'].widget.attrs.update({'class' : 'textarea', 'placeholder': 'What\'s on your mind?'})