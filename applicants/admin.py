from django.contrib import admin

from .models import * 
# Register your models here.
admin.site.register(ApplicantDetail)
admin.site.register(PersonalDetail)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Project)


class SkillAdmin(admin.ModelAdmin):
    list_display=['id','skill_name']

    
admin.site.register(Skill,SkillAdmin)
    
admin.site.register(Accomplishment)