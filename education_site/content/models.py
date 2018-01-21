from django.contrib.auth.models import Permission, User
from django.db import models

# Create your models here.


class Subject(models.Model):
    user = models.ForeignKey(User, default=1)
    level = models.CharField(max_length=250)
    subject_title = models.CharField(max_length=100)

    def __str__(self):
        return self.subject_title

class Article(models.Model):
    user = models.ForeignKey(Subject, on_delete=models.CASCADE)
    article_title = models.CharField(max_length=250)
    article_content = models.CharField(max_length=1000)
    pub_date = models.DateField()
    n_comments = models.IntegerField()
    
    def __str__(self):
        return self.article_title