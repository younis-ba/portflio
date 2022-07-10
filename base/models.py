from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


# Create your models here.

class SocialLink(models.Model):
    name=models.CharField(max_length=200)
    link=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Profile(models.Model):
    logo=models.ImageField(blank=True)
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    avatar=models.ImageField()
    title=models.CharField(max_length=200)
    description=models.TextField(blank=True)
    birth_date=models.DateField(auto_now=False , null=True)
    phone=models.CharField(max_length=200, blank=True)
    email=models.EmailField()
    address=models.CharField(max_length=200)

    def fullname(self):
        return self.firstname + '  ' + self.lastname

    def __str__(self):
        return self.firstname + '  ' + self.lastname


class Interest(models.Model):
    name=models.CharField(max_length=200)
    icon=models.ImageField(blank=True)
    def __str__(self):
        return self.name


class Testimonial(models.Model):
    name=models.CharField(max_length=200)
    img=models.ImageField(blank=True)
    title=models.CharField(max_length=200)
    description=models.TextField(blank=True)
    rating = models.FloatField(default=0)

    def __str__(self):
        return self.name
class Note(models.Model):
    note=models.TextField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    def __str__(self):
        return self.note

class Education(models.Model):
    title=models.CharField(max_length=200)
    icon=models.ImageField(blank=True)
    address=models.CharField(max_length=200,blank=True)
    company=models.CharField(max_length=200)
    description=models.TextField(blank=True)
    start_date=models.CharField(max_length=50)
    end_date=models.CharField(max_length=50)
    def __str__(self):
        return self.title 



class Experience(models.Model):
    title=models.CharField(max_length=200)
    icon=models.ImageField(blank=True)
    address=models.CharField(max_length=200,blank=True)
    company=models.CharField(max_length=200)
    note=GenericRelation(Note , related_name='note')
    start_date=models.CharField(max_length=50)
    end_date=models.CharField(max_length=50)
    def __str__(self):
        return self.title 
class Certifcation(models.Model):
    title=models.CharField(max_length=200)
    code=models.CharField(max_length=200,blank=True)
    def __str__(self):
        return self.title 


class Category(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Project(models.Model):
    title=models.CharField(max_length=200)
    img=models.ImageField(blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    link=models.CharField(max_length=200 , blank=True)
    def __str__(self):
        return self.title



class Service(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField(blank=True)
    icon=models.ImageField(blank=True)

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email=models.EmailField(blank=True)
    subject=models.CharField(max_length=500 , blank=True)
    message=models.TextField()
    def __str__(self):
        return self.subject
       
    