# Create your views here.
from cgitb import lookup
from .serializers import *
from .models import *
from applicants.serializers import * 
from applicants.models import * 
from HRMS.GM import GenericMethodsMixin
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
    model = JobDetailView
    serializer_class = JobProfileSerializer
    lookup_field = 'id'

    
