from pyrsistent import field
from rest_framework import serializers
from .models import *


class RecruiterDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecruiterDetail
        fields = "__all__"


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class JobDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobDetail
        fields = "__all__"


class PerkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perk
        fields = "__all__"


class RequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirement
        fields = "__all__"


class ResponsbilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsbilities
        fields = "__all__"


class SalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Salary
        fields = "__all__"


class Required_SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Required_Skill
        fields = "__all__"
