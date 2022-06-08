from pyrsistent import field
from .models import * 
from rest_framework import serializers

class ApplicantDetailSerializers(serializers.ModelSerializer) :
    class Meta :
        model = ApplicantDetail
        fields = '__all__'
        


class PersonalDetailSerializer(serializers.ModelSerializer) :
    class Meta :
        model = PersonalDetail
        fields = '__all__'
        

class EducationSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Education
        fields = '__all__'
        

class ExperienceSerializer(serializers.ModelSerializer) :
    class Meta : 
        model = Experience
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer) :
    class Meta : 
        model = Project 
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Skill
        fields = '__all__'

class AccomplishmentSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Accomplishment
        fields = '__all__'
