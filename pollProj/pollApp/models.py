from django.db import models

# Create your models here.
class Question(models.Model):
    question = models.TextField()
    option1 = models.CharField(max_length=30)
    option2 = models.CharField(max_length=30)
    option3 = models.CharField(max_length=30)
    count1 = models.IntegerField(default=0)
    count2 = models.IntegerField(default=0)
    count3 = models.IntegerField(default=0)

    def __str__(self):
        return self.question
