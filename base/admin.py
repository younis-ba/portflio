from django.contrib import admin
from .models import  Profile,SocialLink,Certifcation,Interest,Service,Testimonial ,Contact, Experience , Note , Education , Category ,Project
# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['firstname','lastname' ,'title','birth_date','phone','email','address']


class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ['name','link']

class CertifcationAdmin(admin.ModelAdmin):
    list_display = ['title','code']

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name','title','rating']

class NoteAdmin(admin.ModelAdmin):
    list_display = ['note','content_type','object_id','content_object']

class EducationAdmin(admin.ModelAdmin):
    list_display = ['title','address','company','start_date','end_date']

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['title','address','company','start_date','end_date']

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title','link','category']


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','email','subject','message']

admin.site.register(Profile ,ProfileAdmin)
admin.site.register(SocialLink ,SocialLinkAdmin)
admin.site.register(Certifcation ,CertifcationAdmin)
admin.site.register(Testimonial ,TestimonialAdmin)
admin.site.register(Note ,NoteAdmin)
admin.site.register(Education ,EducationAdmin)
admin.site.register(Experience ,ExperienceAdmin)
admin.site.register(Project ,ProjectAdmin)
admin.site.register(Contact ,ContactAdmin)

admin.site.register([Interest,Service,Category ])