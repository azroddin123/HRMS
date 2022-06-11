from cgitb import lookup
from django.http import HttpResponse
from .models import *
from accounts.authentication import CustomAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from HRMS.GM import GenericMethodsMixin
from accounts.authentication import CustomAuthentication

class ApplicantDetailView(GenericMethodsMixin,APIView) :
    authentication_classes = [CustomAuthentication]
    model = ApplicantDetail
    serializer_class = ApplicantDetailSerializers
    lookup_field = 'id'


class PersonalDetailView(GenericMethodsMixin,APIView) :
    authentication_classes = [CustomAuthentication]
    model = PersonalDetail
    serializer_class = PersonalDetailSerializer
    lookup_field = 'id'

class EducationApiView(GenericMethodsMixin,APIView):
    # authentication_classes = [CustomAuthentication]
    model = Education
    serializer_class = EducationSerializer
    lookup_field = 'id'

class ExperienceApiView(GenericMethodsMixin,APIView) :
    authentication_classes = [CustomAuthentication]
    model = Experience
    serializer_class = ExperienceSerializer
    lookup_field = 'id'

class ProjectApiView(GenericMethodsMixin,APIView) :
    authentication_classes = [CustomAuthentication]
    model = Project
    serializer_class = ProjectSerializer
    lookup_field = 'id'

class SkillApiView(GenericMethodsMixin,APIView) :
    # authentication_classes = [CustomAuthentication]
    model = Skill
    serializer_class = SkillSerializer
    lookup_field = 'id'
    
class AccomplishmentApiView(GenericMethodsMixin,APIView) :
    authentication_classes = [CustomAuthentication]
    model = Accomplishment
    serializer_class = AccomplishmentSerializer
    lookup_field = 'id'
    
    
class UserProfileApiView(GenericMethodsMixin,APIView) :
    model = ApplicantDetail
    serializer_class = UserProfileSerializer
    lookup_field = 'id'

class AddMultipleSkillView(APIView) :
    def post(self,request,*args, **kwargs) :
        skill_list = []
        skill_data = request.data['skill_name']
        for item in skill_data :
            print(item, "Items Printed")
            skill = Skill(skill_name= item)
            skill_list.append(skill)
        response = SkillSerializer(Skill.objects.bulk_create(skill_list),many=True).data
        
        print(skill_list)
        return Response({"Message" : response},status=status.HTTP_201_CREATED)
# we are creating bulk data in skill table 





