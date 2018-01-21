# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .forms import SubjectForm, ArticleForm, UserForm
from .models import Subject, Article

# Create your views here.

def index(request):
    if not request.user.is_authenticated():
        return render(request, 'content/login.html')
    else:
        subjects = Subject.objects.filter(user=request.user)
        article_results = Article.objects.all()
        query = request.GET.get("q")
        if query:
            subjects = subjects.filter(
                    Q(subject_title__icontains=query) |
                    Q(user__icontains=query)
            ).distinct()
            article_results = article_results.filter(
                    Q(subject_title__icontains=query)
            ).distinct()
            return render(request, 'content/index.html', {
                    'subjects': subjects,
                    'articles': article_results,
            })
        else:
            return render(request, 'content/index.html', {'subjects':subjects})
        
        
def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'content/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                subjects = Subject.objects.filter(user=request.user)
                return render(request, 'content/index.html', {'subjects':subjects})
            else:
                return render(request, 'content/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'content/login.html', {'error_message': 'Invalid login'})
    return render(request, 'content/login.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                subjects = Subject.objects.filter(user=request.user)
                return render(request, 'content/index.html', {'subjects':subjects})
    context = {
        "form": form,
    }
    return render(request, 'content/register.html', context)

def subject(request):
    if not request.user.is_authenticated():
        return render(request, 'content/login.html')
    else:
        return render(request, 'content/subject.html', {
##            'filter_by': filter_by,
        })
    
def create_subject(request):
    if not request.user.is_authenticated():
        return render(request, 'content/login.html')
    else:
        form = SubjectForm(request.POST or None)
        if form.is_valid():
            subject = form.save(commit=False)
            subject.user = request.user
            return render(request, 'content/detail.html', {'subject': subject})
        context = {
            "form": form,
        }
        return render(request, 'content/create_subject.html', context)
    
def detail(request, subject_id):
    if not request.user.is_authenticated():
        return render(request, 'content/login.html')
    else:
        user = request.user
        subject = get_object_or_404(Subject, pk=subject_id)
        return render(request, 'content/detail.html', {'subject': subject, 'user': user})
    
    