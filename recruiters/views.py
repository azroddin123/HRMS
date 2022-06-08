from cgitb import lookup
from django.shortcuts import render

# Create your views here.
from .serializers import *
from .models import *
from HRMS.GM import GenericMethodsMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse


class CompanyDetailView(GenericMethodsMixin, APIView):
    model = Company
    serializer_class = CompanySerializer
    lookup_field = "id"


class RecruiterDetailView(GenericMethodsMixin, APIView):
    model = RecruiterDetail
    serializer_class = RecruiterDetailSerializer
    lookup_field = "id"


class JobDetailView(GenericMethodsMixin, APIView):
    model = JobDetail
    serializer_class = JobDetailSerializer
    lookup_field = "id"


class PerkView(GenericMethodsMixin, APIView):
    model = Perk
    serializer_class = PerkSerializer
    lookup_field = "id"


class RequirementView(GenericMethodsMixin, APIView):
    model = RecruiterDetail
    serializer_class = RecruiterDetailSerializer
    lookup_field = "id"


class ResponsibilitiesView(GenericMethodsMixin, APIView):
    model = Responsbilities
    serializer_class = ResponsbilitiesSerializer
    lookup_field = "id"


class SalaryView(GenericMethodsMixin, APIView):
    model = Salary
    serializer_class = SalarySerializer
    lookup_field = "id"


class Required_SkillView(GenericMethodsMixin, APIView):
    model = Required_Skill
    serializer_class = Required_SkillSerializer
    lookup_field = "id"
