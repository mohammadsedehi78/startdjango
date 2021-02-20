from django.db import models


class question(models.Model):
    questionText = models.CharField(max_length=200)
    publishDate = models.DateTimeField('date published')


class chioce(models.Model):
    question = models.ForeignKey(question, on_delete=models.CASCADE)
    chioce = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
