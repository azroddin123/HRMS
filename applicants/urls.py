from django.urls import path
from .views import * 


urlpatterns = [
    # path('<int:id>',ApplicantDetailView.as_view()),
    # path('person/<int:id>',PersonDetailView.as_view()),
    
  
    path('profile/<int:pk>',ApplicantDetailView.as_view()),
    path('profile',ApplicantDetailView.as_view()),
    
    path('personal_detail/<int:pk>',PersonalDetailView.as_view()),
    path('personal_detail',PersonalDetailView.as_view()),
    
    path('education/<int:pk>',EducationApiView.as_view()),
    path('education/',EducationApiView.as_view()),
    
    path('experience/<int:pk>',ExperienceApiView.as_view()),
    path('experience',ExperienceApiView.as_view()),
    
        
    path('project/<int:pk>',ProjectApiView.as_view()),
    path('project',ProjectApiView.as_view()),
   
    path('skill/<int:pk>',SkillApiView.as_view()),
    path('skill',SkillApiView.as_view()),
    
    path('accomplishment/<int:pk>',AccomplishmentApiView.as_view()),
    path('accomplishment',AccomplishmentApiView.as_view()),
    
]
