from pyexpat import model
from django.db import models
from accounts.models import MyUser
# Create your models here.
# from applicants.models import ApplicantDetail
TYPE_WORK_CHOICES  = ( 
                      ("full_time","full_time"),
                      ("part_time","part_time")
                    )

class Company(models.Model) :
    
    comapny_name    = models.CharField(max_length=200,null=True,blank=True)
    company_email   = models.EmailField()
    location        = models.CharField(max_length=100,null=True,blank=True)
    contact_no      = models.CharField(max_length=200,null=True,blank=True)
    description     = models.TextField(null=True,blank=True)
    no_of_employees = models.IntegerField(null=True,blank=True)
    address         = models.TextField(null=True,blank=True)
    
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True) 
    
    created_by      = models.ForeignKey(MyUser,on_delete=models.CASCADE,null=True,blank=True)
    
    def __str__(self):
        return self.comapny_name
    

class RecruiterDetail(models.Model) : 
    
    company       = models.ForeignKey(Company,on_delete=models.CASCADE,null=True,blank=True)
    
    name          = models.CharField(max_length=200,null=True,blank=True)
    contact_no    = models.CharField(max_length=200,null=True,blank=True)
    about         = models.TextField(null=True,blank=True)
    
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)
    

    
    def __str__(self):
        return self.name
    
class JobDetail(models.Model) :
    # main job Model 
    recruiter            = models.ForeignKey(RecruiterDetail,on_delete=models.CASCADE,null=True,blank=True)
    
    job_designation      = models.CharField(max_length=200,null=True,blank=True)
    company_name         = models.ForeignKey(Company,on_delete=models.CASCADE,null=True,blank=True)
    country              = models.CharField(max_length=200,null=True,blank=True)
    job_address          = models.CharField(max_length=200,null=True,blank=True)
    type_of_work         = models.CharField(max_length=200,choices=TYPE_WORK_CHOICES,default="full_time",null=True,blank=True)
    city                 = models.CharField(max_length=200,null=True,blank=True)
    no_of_opening        = models.CharField(max_length=200,null=True,blank=True)
    job_description      = models.TextField(null=True,blank=True)
    qualification        = models.CharField(max_length=200,null=True,blank=True)
    exp_required         = models.CharField(max_length=200,null=True,blank=True)
    probation_period     = models.BooleanField(default=True)
    probation_duration   = models.IntegerField(null=True,blank=True)
    key_resposibilities  = models.TextField(null=True,blank=True)
    
    created_at           = models.DateTimeField(auto_now_add=True)
    updated_at           = models.DateTimeField(auto_now=True)
     
    created_by           = models.ForeignKey(MyUser,on_delete=models.CASCADE,null=True,blank=True)  
    
    # applicants            = models.ManyToManyField(ApplicantDetail,on_delete=models.CASCADE)
    def __str__(self):
            return str(self.id)

    
class Responsbilities(models.Model) :
    
    job          = models.ForeignKey(JobDetail,on_delete=models.CASCADE,null=True,blank=True)

    desc         = models.CharField(max_length=200,null=True,blank=True)
    title        = models.CharField(max_length=200,null=True,blank=True)
    
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)  
    
    created_by   = models.ForeignKey(MyUser,on_delete=models.CASCADE)   


    def __str__(self):
            return self.desc
        
        
class SalaryAndPerk(models.Model) :
    job                 = models.OneToOneField(JobDetail,on_delete=models.CASCADE,null=True,blank=True)
   
    avg_salary          = models.CharField(max_length=200,null=True,blank=True)
    min_salary          = models.CharField(max_length=200,null=True,blank=True)
    max_salary          = models.CharField(max_length=200,null=True,blank=True)
    five_days_week      = models.BooleanField(default=False,null=True,blank=True)
    life_insurence      = models.BooleanField(default=False,null=True,blank=True)
    health_insurence    = models.BooleanField(default=False,null=True,blank=True)
    dress_code          = models.BooleanField(default=False,null=True,blank=True)
    snack_lunch         = models.BooleanField(default=False,null=True,blank=True)
    probation_period    = models.BooleanField(default=False,null=True,blank=True)
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)   
    
    created_by          = models.ForeignKey(MyUser,on_delete=models.CASCADE,null=True,blank=True)  
    
    def __str__(self):
        return str(self.id)

    
class Salary(models.Model) :
    
    job                 = models.OneToOneField(JobDetail,on_delete=models.CASCADE,null=True,blank=True)
    avg_salary          = models.CharField(max_length=200,null=True,blank=True)
    min_salary          = models.CharField(max_length=200,null=True,blank=True)
    max_salary          = models.CharField(max_length=200,null=True,blank=True)
    
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)   
    
    created_by          = models.ForeignKey(MyUser,on_delete=models.CASCADE)  
    
    def __str__(self):
            return self.avg_salary
    
class Perk(models.Model) :
    
    job              = models.OneToOneField(JobDetail,on_delete=models.CASCADE,null=True,blank=True)
    
    five_days_week   = models.BooleanField(default=False,null=True,blank=True)
    life_insurence   = models.BooleanField(default=False,null=True,blank=True)
    health_insurence = models.BooleanField(default=False,null=True,blank=True)
    dress_code       = models.BooleanField(default=False,null=True,blank=True)
    snack_lunch      = models.BooleanField(default=False,null=True,blank=True)
    
    created_at       = models.DateTimeField(auto_now_add=True)
    updated_at       = models.DateTimeField(auto_now=True)   
    
    created_by       = models.ForeignKey(MyUser,on_delete=models.CASCADE)  
    


class Required_Skill(models.Model) :
    
    job           = models.ForeignKey(JobDetail,on_delete=models.CASCADE,null=True,blank=True)
    
    skill_name    = models.CharField(max_length=200,null=True,blank=True)
    
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)  
    
    created_by    = models.ForeignKey(MyUser,on_delete=models.CASCADE)   
    
    def __str__(self):
            return str(self.skill_name)
        
    