from django.db import models
class Question(models.Model):
   question_text = models.CharField(max_length=200)
   pub_date = models.DateTimeField("date published")


class Choice(models.Model):
   question = models.ForeignKey(Question, on_delete=models.CASCADE)
   choice_text = models.CharField(max_length=200)
   votes = models.IntegerField(default=0)

class year(models.Model):
   year = models.CharField(max_length=4)
   def __str__(self):
       return self.year
   
class appname(models.Model):
   appname = models.CharField(max_length=100)
   def __str__(self):
       return self.appname