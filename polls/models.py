'''
@author Ryan Kilbride
@since 2018-08-12
'''


import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):
    strQuestionText = models.CharField(max_length=200)
    dtmPublishDate = models.DateTimeField('date published')

    def __str__(self):
        return self.strQuestionText

    def was_published_recently(self):
        return self.dtmPublishDate >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    strChoiceText = models.CharField(max_length=200)
    lngVotes = models.IntegerField(default=0)

    def __str__(self):
        return self.strChoiceText
