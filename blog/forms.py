from django import forms
from .models import Post

# Tell django that PostForm is a ModelForm
class PostForm(forms.ModelForm):
    # Tell django which model used to create form
    class Meta:
        model = Post
        # Author and dates are set automatically
        fields = ('title', 'text',)