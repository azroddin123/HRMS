from django.db import models
from flask_sqlalchemy import Model

# Create your models here.

class Test(models.Model):
    
    test_name          = models.CharField(max_length=200,null=True,blank=True)
    no_of_question     = models.IntegerField(null=True,blank=True,default=50)
    total_marks        = models.IntegerField(null=True,blank=True,default=50)
    total_time         = models.IntegerField(null=True,blank=True,default=50)
    

class Question(models.Model):
    
    question_no        = models.IntegerField(null=True,blank=True)
    question_name      = models.CharField(max_length=500,null=True,blank=True)
    option_one         = models.CharField(max_length=200,null=True,blank=True)
    option_two         = models.CharField(max_length=200,null=True,blank=True)
    option_three       = models.CharField(max_length=200,null=True,blank=True)
    option_four        = models.CharField(max_length=200,null=True,blank=True)
    
    test_name          = models.ForeignKey(Test,on_delete=models.CASCADE)
    
class AnswerSheet(models.Model) :
        pass
    
    

