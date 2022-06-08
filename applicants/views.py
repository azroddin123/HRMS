from cgitb import lookup
from django.http import HttpResponse
from .models import *
from accounts.authentication import CustomAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from HRMS.GM import GenericMethodsMixin


class ApplicantDetailView(GenericMethodsMixin,APIView) :
    model = ApplicantDetail
    serializer_class = ApplicantDetailSerializers
    lookup_field = 'id'

class PersonalDetailView(GenericMethodsMixin,APIView) :
    model = PersonalDetail
    serializer_class = PersonalDetailSerializer
    lookup_field = 'id'

class EducationApiView(GenericMethodsMixin,APIView):
    model = Education
    serializer_class = EducationSerializer
    lookup_field = 'id'

class ExperienceApiView(GenericMethodsMixin,APIView) :
    model = Experience
    serializer_class = ExperienceSerializer
    lookup_field = 'id'

class ProjectApiView(GenericMethodsMixin,APIView) :
    model = Project
    serializer_class = ProjectSerializer
    lookup_field = 'id'

class SkillApiView(GenericMethodsMixin,APIView) :
    model = Skill
    serializer_class = SkillSerializer
    lookup_field = 'id'
    
class AccomplishmentApiView(GenericMethodsMixin,APIView) :
    model = Accomplishment
    serializer_class = AccomplishmentSerializer
    lookup_field = 'id'
