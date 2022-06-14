from cgitb import lookup
from django.http import HttpResponse
from django.db.models import Q
from django.db.models import Model
from recruiters.models import JobDetail
from recruiters.serializers import JobDetailSerializer
from .models import *
from accounts.authentication import CustomAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from HRMS.GM import GenericMethodsMixin,search3
from accounts.authentication import CustomAuthentication
from itertools import chain
import operator

class ApplicantDetailView(GenericMethodsMixin, APIView):
    authentication_classes = [CustomAuthentication]
    model = ApplicantDetail
    serializer_class = ApplicantDetailSerializers
    lookup_field = "id"


class PersonalDetailView(GenericMethodsMixin, APIView):
    authentication_classes = [CustomAuthentication]
    model = PersonalDetail
    serializer_class = PersonalDetailSerializer
    lookup_field = "id"


class EducationApiView(GenericMethodsMixin, APIView):
    # authentication_classes = [CustomAuthentication]
    model = Education
    serializer_class = EducationSerializer
    lookup_field = "id"


class ExperienceApiView(GenericMethodsMixin, APIView):
    authentication_classes = [CustomAuthentication]
    model = Experience
    serializer_class = ExperienceSerializer
    lookup_field = "id"


class ProjectApiView(GenericMethodsMixin, APIView):
    authentication_classes = [CustomAuthentication]
    model = Project
    serializer_class = ProjectSerializer
    lookup_field = "id"


class SkillApiView(GenericMethodsMixin, APIView):
    # authentication_classes = [CustomAuthentication]
    model = Skill
    serializer_class = SkillSerializer
    lookup_field = "id"


class AccomplishmentApiView(GenericMethodsMixin, APIView):
    authentication_classes = [CustomAuthentication]
    model = Accomplishment
    serializer_class = AccomplishmentSerializer
    lookup_field = "id"


class UserProfileApiView(GenericMethodsMixin, APIView):
    model = ApplicantDetail
    serializer_class = UserProfileSerializer
    lookup_field = "id"


class AddMultipleSkillView(APIView):
    def post(self, request, *args, **kwargs):
        skill_list = []
        if not request.data["skill_name"]:
            return Response("Data not found")
        skill_data = request.data["skill_name"]

        for item in skill_data:
            print(item, "Items Printed")
            skill = Skill(skill_name=item)
            skill_list.append(skill)
        response = SkillSerializer(
            Skill.objects.bulk_create(skill_list), many=True
        ).data

        print(skill_list)
        return Response({"Message": response}, status=status.HTTP_201_CREATED)


# get job according to user serach
class SerachJobApiView(APIView):
    def get(self, request, *args, **kwargs):
        query = "latur"
        # get field list from model
        field_list = list(
            set(chain.from_iterable((field.name, field.attname) if hasattr(field, "attname") else (field.name,)
                    for field in JobDetail._meta.get_fields()
                    # if not (field.many_to_one and field.related_model is None)
                    if field.concrete and not(
                field.is_relation or field.one_to_one or 
                (field.many_to_one and field.related_model))
                )
            )
        )
        query = search3("MCA",field_list)
        results = JobDetail.objects.filter(query)
      
        return Response({"wye": JobDetailSerializer(results, many=True).data}, )
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
        # for index,field in enumerate(field_list):
        #     # print(field_list[index])
        #     data_set.append((Q(operator.or_,{field_list[index]:query})))

        # # print(data_set)
        # newDataSet = []
        # # for i in data_set:
        # #     print(type(i))

        # # for q in data_set:
        # #     print(q)
        # print(Q(job_designation="Devloper") | Q(country="india") | Q(city="Latur"))
        # print(type(Q(job_designation="Devloper") | Q(country="india") | Q(city="Latur")))
        # data_se = JobDetail.objects.filter(
        #     Q(job_designation="Devloper") | Q(country="india") | Q(city="Latur")
        # )

        # print(data_se)