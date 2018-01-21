from django import forms
from django.contrib.auth.models import User

from .models import Subject, Article


class SubjectForm(forms.ModelForm):

    class Meta:
        model = Subject
        fields = ['level', 'subject_title', 'user']


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ['article_title', 'article_content', 'pub_date', 'n_comments']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
# -*- coding: utf-8 -*-

