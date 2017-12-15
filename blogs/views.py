from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from blogs import forms
from blogs.forms import UserRegistrationForm
from blogs.models import BlogsModel


def home(request):
    query_results = BlogsModel.objects.all()
    return render(request, 'mysite/home.html', {'query_results':query_results})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email =  userObj['email']
            password =  userObj['password']

            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username = username, password = password)
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                raise forms.ValidationError('Looks like a username with that email or password already exists')
    else:
        form = UserRegistrationForm()
    return render(request, 'mysite/register.html', {'form' : form})

def blog_detail(request):
    query_result = BlogsModel.objects.all()
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        file = FileSystemStorage()
        filename = file.save(myfile.name, myfile)
        uploaded_file_url = file.url(filename)
        return render(request, 'mysite/blog_detail.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'mysite/blog_detail.html', {'description':query_result})

