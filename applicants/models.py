from django.db import models
from accounts.models import MyUser
# Create your models here.
# from recruiters.models import * 

class ApplicantDetail(models.Model) :

    fullname            = models.CharField(max_length=200,null=True,blank=True)
    job_title           = models.CharField(max_length=200,null=True,blank=True)
    qualification       = models.CharField(max_length=200,null=True,blank = True)
    contact_no          = models.CharField(max_length=200,null=True,blank=True)
    dateOfBirth         = models.DateField(null=True,blank=True)
    location            = models.CharField(max_length=100,null=True,blank=True)
    portfolioLink       = models.CharField(max_length=200,null=True,blank=True)
    resume              = models.FileField(upload_to='resume/',blank=True,null=True)
    
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)
    
    created_by          = models.OneToOneField(MyUser,on_delete=models.CASCADE,null=True,blank=True)
  
    # applied_job =  models.ManyToManyField(JobDetail,on_delete=models.CASCADE,null=True,blank=True)
    
    def __str__(self):
        return self.fullname
 
LANG_CHOICES = (
    ("English", "English"),
    ("Hindi", "Hindi"),
    ("Bengali","Bengali"),
    ("Burmese","Burmese"),
    ("Chittagonian","Chittagonian"),
)  
 
class PersonalDetail(models.Model) :
    
    applicant            = models.OneToOneField(ApplicantDetail,on_delete=models.CASCADE,null=True,blank=True)
    
    email                = models.EmailField(max_length=255,unique=True)
    nidID                = models.CharField(max_length=200,null=True,blank=True)
    mobile_no            = models.CharField(max_length=200,null=True,blank=True)
  
    preferred_language   = models.CharField(max_length=200,choices=LANG_CHOICES,null=True,blank=True)
    mother_tounge        = models.CharField(max_length=200,null=True,blank=True)
    about                = models.TextField(null=True,blank=True)

    created_at           = models.DateTimeField(auto_now_add=True)
    updated_at           = models.DateTimeField(auto_now=True)   

    created_by           = models.ForeignKey(MyUser,on_delete=models.CASCADE,null=True,blank=True)
    
    def __str__(self):
        return self.email

    
COURSE_CHOICES = (
    ("10", "10th"),
    ("12", "12th"),
    ("ITI","ITI"),
    ("Graduation","Graduation"),
    ("Diploma","Diploma"),
    ("Post_Graduation","Post_Graduation"),
    ("PhD","PhD"),
    ("Doctorate","Doctorate")
)   

class Education(models.Model) :
    
    applicant            = models.ForeignKey(ApplicantDetail,on_delete=models.CASCADE,null=True,blank=True)
   
    eduacation_name      = models.CharField(max_length=200,choices=COURSE_CHOICES,null=True,blank=True)
    course_name          = models.CharField(max_length=200,null=True,blank=True)
    college_name         = models.CharField(max_length=200,null=True,blank=True)
    university           = models.CharField(max_length=200,null=True,blank=True)
    stream               = models.CharField(max_length=200,null=True,blank=True)
    performance          = models.CharField(max_length=200,null=True,blank=True)
    percentage           = models.FloatField(null=True,blank=True)
    strat_date           = models.DateTimeField(auto_now_add=True)
    end_date             = models.DateTimeField(auto_now=True) 
  
    created_at           = models.DateTimeField(auto_now_add=True)
    updated_at           = models.DateTimeField(auto_now=True)  
    
    created_by          = models.ForeignKey(MyUser,on_delete=models.CASCADE,null=True,blank=True) 
    
    def __str__(self):
        return self.eduacation_name

class Experience(models.Model) :
    
    applicant           = models.ForeignKey(ApplicantDetail,on_delete=models.CASCADE,null=True,blank=True)
    
    designation         = models.CharField(max_length=200,null=True,blank=True)
    orgnisation_name    = models.CharField(max_length=200,null=True,blank=True)
    technology          = models.CharField(max_length=200,null=True,blank=True)
    location            = models.CharField(max_length=200,null=True,blank=True)
    start_date          = models.CharField(max_length=200,null=True,blank=True)
    end_date            = models.CharField(max_length=200,null=True,blank=True)
    performance         = models.CharField(max_length=200,null=True,blank=True)
    no_of_years         = models.IntegerField(null=True,blank=True)
    
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True) 
    
    created_by          = models.ForeignKey(MyUser,on_delete=models.CASCADE,null=True,blank=True)  
    
    def __str__(self):
        return self.designation 
    
    

class Project(models.Model) :
    
    applicant           = models.ForeignKey(ApplicantDetail,on_delete=models.CASCADE,null=True,blank=True)
   
    title               = models.CharField(max_length=200,null=True,blank=True)
    description         = models.TextField(null=True,blank=True)
    status              = models.BooleanField(null=True,blank=True,default=False)
    technology          = models.CharField(max_length=200,null=True,blank=True)
    start_date          = models.DateField(null=True,blank=True)
    end_date            = models.DateField(null=True,blank=True)

    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)   
    
    created_by          = models.ForeignKey(MyUser,on_delete=models.CASCADE,null=True,blank=True) 

    def __str__(self):
        return self.title


class Skill(models.Model):
    
    applicant           = models.ForeignKey(ApplicantDetail,on_delete=models.CASCADE,null=True,blank=True)
    skill_name          = models.CharField(max_length=200,null=True,blank=True)
    
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)   
    
    created_by          = models.ForeignKey(MyUser,on_delete=models.CASCADE,null=True,blank=True) 
    
    def __str__(self):
        return self.skill_name


class Accomplishment(models.Model) :
    
    applicant                   = models.ForeignKey(ApplicantDetail,on_delete=models.CASCADE,null=True,blank=True)
    
    certification_name          = models.CharField(max_length=200,null=True,blank=True)
    certificate_institute_name  = models.CharField(max_length=200,null=True,blank=True)
    ceritificate_id             = models.CharField(max_length=200,null=True,blank=True)

    
    created_at                  = models.DateTimeField(auto_now_add=True)
    updated_at                  = models.DateTimeField(auto_now=True)  
    
    created_by                  = models.ForeignKey(MyUser,on_delete=models.CASCADE,null=True,blank=True)  
    
    def __str__(self):
        return self.certification_name
