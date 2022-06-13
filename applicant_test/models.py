from venv import create
from django.db import models
from flask_sqlalchemy import Model

from accounts.models import MyUser

# Create your models here.

class Job_Test(models.Model):
    
    test_name            = models.CharField(max_length=200,null=True,blank=True)
    no_of_question       = models.IntegerField(null=True,blank=True,default=50)
    total_marks          = models.IntegerField(null=True,blank=True,default=50)
    total_time           = models.IntegerField(null=True,blank=True,default=50)
    
    created_at           = models.DateTimeField(auto_now_add=True)
    updated_at           = models.DateTimeField(auto_now=True)
    
    created_by           = models.ForeignKey(MyUser,on_delete=models.CASCADE)
    

class Question(models.Model):
    
    question_no         = models.IntegerField(null=True,blank=True)
    question_desc       = models.CharField(max_length=500,null=True,blank=True)
    option_one          = models.CharField(max_length=200,null=True,blank=True)
    option_two          = models.CharField(max_length=200,null=True,blank=True)
    option_three        = models.CharField(max_length=200,null=True,blank=True)
    option_four         = models.CharField(max_length=200,null=True,blank=True)
    
    test_name           = models.ForeignKey(Job_Test,on_delete=models.CASCADE)
    
class AnswerSheet(models.Model) :
        pass
    
    

