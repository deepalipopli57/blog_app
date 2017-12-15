from django import forms

from blogs.models import BlogsModel


class UserRegistrationForm(forms.Form):
    username = forms.CharField(
        required = True,
        label = 'Username',
        max_length = 32
    )
    email = forms.CharField(
        required = True,
        label = 'Email',
        max_length = 32,
    )
    password = forms.CharField(
        required = True,
        label = 'Password',
        max_length = 32,
        widget = forms.PasswordInput()
    )


class Blogs(forms.ModelForm):
    class Meta:
        model = BlogsModel
        fields = ('description', 'image')


class BlogsForm(forms.ModelForm):
    class Meta:
        model = BlogsModel
        fields = ['image', 'description', 'title']

    def __str__(self):
        return self.description