from django.http import JsonResponse
from numpy import source
from pyrsistent import field
from requests import request
from rest_framework import serializers
from applicants.models import Project

import recruiters
from .models import *
from accounts.serializers import MyUserSerializer

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model  = Company
        fields = "__all__"
        
class CompanySerializerInline(serializers.ModelSerializer):
    created_by = MyUserSerializer()
    class Meta:
        model  = Company
        fields = ("id","created_by")

class JobDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model  = JobDetail
        fields = "__all__"
        
class RecruiterDetailSerializer(serializers.ModelSerializer):
    jobs = JobDetailSerializer(source="jobdetail_set", many=True)
    class Meta:
        model  = RecruiterDetail
        fields = "__all__"        

class PerkSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Perk
        fields = "__all__"

class ResponsbilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Responsbilities
        fields = "__all__"

class SalarySerializer(serializers.ModelSerializer):
    class Meta:
        model  = Salary
        fields = "__all__"

class Required_SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Required_Skill
        fields  = "__all__"


class CompanyRecruiterSerializer(serializers.ModelSerializer):
    class Meta :
         model       = RecruiterDetail
         fields      = ['name','contact_no','about','company']

    def to_representation(self, instance):
        try:
            company = Company.objects.get(id=instance.company.id)
            print("compnay",company)
            serializedd_data = CompanySerializerInline(company).data
            print("After Serialization",serializedd_data)
            data = super(CompanyRecruiterSerializer, self).to_representation(instance)
            print(super(CompanyRecruiterSerializer, self).to_representation(instance))
            print("companies data",data)
            data.update({"company": serializedd_data})
            print("comapny data",data)
            return data
        except AttributeError:
            return super(CompanyRecruiterSerializer, self).to_representation(instance)
        
        
class JobProfileSerializer(serializers.ModelSerializer) :
    skills = Required_SkillSerializer(source="required_skill_set",many=True)
    # perks = PerkSerializer(source="perk_set",many=True)
    requirements = ResponsbilitiesSerializer(source='responsbilities_set',many=True)
    perks = PerkSerializer(read_only=True,source='perk')
    
    # comapny = CompanySerializer()
    class Meta :
        model = JobDetail
        fields = '__all__'

class SalaryAndPerkSerializer(serializers.ModelSerializer) :
    class Meta :
        model = SalaryAndPerk
        fields = '__all__'
        