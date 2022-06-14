# Create your views here.
from cgitb import lookup
from random import randint
from yaml import serialize
from .serializers import *
from .models import *
from applicants.serializers import * 
from applicants.models import * 
from HRMS.GM import GenericMethodsMixin
from HRMS.GM import search3
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from accounts.authentication import CustomAuthentication

class CompanyDetailView(GenericMethodsMixin, APIView):
    authentication_classes = [CustomAuthentication]
    model = Company
    serializer_class = CompanySerializer
    lookup_field = "id"


class RecruiterDetailView(GenericMethodsMixin, APIView):
    authentication_classes = [CustomAuthentication]
    model = RecruiterDetail
    serializer_class = RecruiterDetailSerializer
    lookup_field = "id"


class JobDetailView(GenericMethodsMixin, APIView):
    authentication_classes = [CustomAuthentication]
    model = JobDetail
    serializer_class = JobDetailSerializer
    lookup_field = "id"

class PerkView(GenericMethodsMixin, APIView):
    authentication_classes = [CustomAuthentication]
    model = Perk
    serializer_class = PerkSerializer
    lookup_field = "id"

class ResponsibilitiesView(GenericMethodsMixin, APIView):
    authentication_classes = [CustomAuthentication]
    model = Responsbilities
    serializer_class = ResponsbilitiesSerializer
    lookup_field = "id"

class SalaryView(GenericMethodsMixin, APIView):
    authentication_classes = [CustomAuthentication]    
    model = Salary
    serializer_class = SalarySerializer
    lookup_field = "id"

class Required_SkillView(GenericMethodsMixin, APIView):
    authentication_classes = [CustomAuthentication]
    model = Required_Skill
    serializer_class = Required_SkillSerializer
    lookup_field = "id"

class CompanyRecruiterView(GenericMethodsMixin,APIView) :
    model = RecruiterDetail
    serializer_class = CompanyRecruiterSerializer
    lookup_field = 'id'
    
class GetCandidateProfileView(APIView) :
    authentication_classes = [CustomAuthentication]
    def get(self,request,*args,**kwargs) :
        print("In candidate Profile view")
        applicant_profiles = ApplicantDetail.objects.filter(job_title='Developer')

        
class JobProfileFinalView(GenericMethodsMixin,APIView) :
    model = JobDetail
    serializer_class = JobProfileSerializer
    lookup_field = 'id'
    

class SalaryAndPerkView(GenericMethodsMixin,APIView) :
    model = SalaryAndPerk
    serializer_class = SalaryAndPerkSerializer
    lookup_field = 'id'
    
class OTPApiView(APIView) :
    def get(self,request,*args,**kargs) :
           otp = str(randint(100000, 999999)) 
           return Response({"OTP" : otp },status=status.HTTP_200_OK)
               
               

    
class AddMultipleSkillApi(APIView) :
    def post(self,request,*args, **kwargs) :
        print(request.data)
        skill_list = []
        skill_array = request.data["skill"]
        for item in skill_array :
            skill_list.append(Required_Skill(skill_name=item))
        
        Required_Skill.objects.bulk_create(skill_list)
        return Response({"Success":"Multiple Skill Imported", "skill" : str(skill_list)},status=status.HTTP_201_CREATED)
        
        