from django.urls import path
from .views import * 


urlpatterns = [
    # path('<int:id>',ApplicantDetailView.as_view()),
    # path('person/<int:id>',PersonDetailView.as_view()),
  
    path('profile/<int:pk>',RecruiterDetailView.as_view()),
    path('profile',RecruiterDetailView.as_view()),
    
    path('company/<int:pk>',CompanyDetailView.as_view()),
    path('company',CompanyDetailView.as_view()),
    
    path('job_details/<int:pk>',JobDetailView.as_view()),
    path('job_details/',JobDetailView.as_view()),
    
    path('perks/<int:pk>',PerkView.as_view()),
    path('perks',PerkView.as_view()),
        
    # path('requirement/<int:pk>',RequirementView.as_view()),
    # path('requirement',RequirementView.as_view()),
   
    path('responsibilities/<int:pk>',ResponsibilitiesView.as_view()),
    path('responsibilities',ResponsibilitiesView.as_view()),
    
    path('salary/<int:pk>',SalaryView.as_view()),
    path('salary',SalaryView.as_view()),
     
    path('required_skill/<int:pk>',Required_SkillView.as_view()),
    path('required_skill',Required_SkillView.as_view()),
    
    path('company_view/<int:pk>',CompanyRecruiterView.as_view()),
    path('finaljobview/<int:pk>',JobProfileFinalView.as_view())
    
    # path('applicantProfiles',GetCandidateProfileView.as_view())
]
