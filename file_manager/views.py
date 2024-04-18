from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import UploadedFile
import boto3

# Create your views here.


def home(request):
    if request.user.is_authenticated:
        return redirect('file_list')
    else:
        return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('file_list')
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('login')


@login_required
def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        s3 = boto3.client('s3')
        s3.upload_fileobj(file, settings.AWS_STORAGE_BUCKET_NAME, file.name)
        UploadedFile.objects.create(user=request.user, name=file.name)
        return redirect('file_list')
    return render(request, 'upload.html')


@login_required
def file_list(request):
    users = User.objects.all()
    users_with_files = {}
    for user in users:
        files = UploadedFile.objects.filter(user=user)
        users_with_files[user] = files
    return render(request, 'file_list.html', {'users_with_files': users_with_files})


@login_required
def download_file(request, file_id):
    file = UploadedFile.objects.get(id=file_id)
    s3 = boto3.client('s3')
    url = s3.generate_presigned_url(
        ClientMethod='get_object',
        Params={'Bucket': settings.AWS_STORAGE_BUCKET_NAME, 'Key': file.name},
        ExpiresIn=3600
    )
    return redirect(url)
