from django.db import models
from datetime import datetime

# Create your models here.

class Word(models.Model):
    word = models.CharField(max_length=64)
    translation=models.CharField(max_length=64)
    sentences = models.CharField(max_length=1024)
    
    stage = models.IntegerField(default=0)
    review_date = models.DateField(default=datetime(2020, 1, 1))
    learned_date = models.DateField(default=datetime(2020, 1, 1))
    valid =  models.BooleanField(default=True)
    chosen= models.BooleanField(default=False)



    def __str__(self):
        return self.word+" "+self.translation
