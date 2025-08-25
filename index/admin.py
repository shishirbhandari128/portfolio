from django.contrib import admin

# Register your models here.
from .models import ContactDetails, Portfolio, TechnicalSkill, ProfessionalSkill, Experience, Tools, education, Project, SocialLink


@admin.register(Portfolio)  
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'description', 'image')
    search_fields = ('name','title',)  

@admin.register(ContactDetails)
class ContactDetailsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'location')
    search_fields = ('name', 'email')

@admin.register(TechnicalSkill)  
class SkillAdmin(admin.ModelAdmin): 
    list_display = ('name', 'proficiency')
    search_fields = ('name',)

@admin.register(ProfessionalSkill)  
class SkillAdmin(admin.ModelAdmin): 
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Tools)  
class SkillAdmin(admin.ModelAdmin): 
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'company', 'start_date', 'end_date')
    search_fields = ('job_title', 'company')
    list_filter = ('start_date', 'end_date')

@admin.register(education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'start_date', 'end_date')
    search_fields = ('degree', 'institution')
    list_filter = ('start_date', 'end_date')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image', 'url', 'github_url')
    search_fields = ('title', 'description')
    list_filter = ('url', 'github_url')

admin.site.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('github', 'linkedin', 'twitter', 'facebook')
    search_fields = ('github', 'linkedin', 'twitter', 'facebook')
