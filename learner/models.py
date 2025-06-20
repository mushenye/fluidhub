from datetime import datetime
import string
from django.db import models
import uuid
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

# Create your models here.





GRADE=(
    ('RE','Reception'),
    ('P1','Pre-Primary 1'),
    ('P2','Pre-Primary 2'),
    ('G1','Grade 1'),
    ('G2','Grade 2'),
    ('G3','grade 3'),
    ('G4','Grade 4'),
    ('G5','Grade 5'),
    ('G6','grade 6'),
    ('Junior Secondary','Junior Secondary'),
)

import secrets


class School( models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE )
    date_created=models.DateField(auto_now=True)
    school_name= models.CharField(max_length=100)
    school_code= models.UUIDField(primary_key=True, default= uuid.uuid4)
    passcode=models.CharField( max_length=8, unique=True, default = get_random_string(length=6))

    def __str__(self):
        return self.school_name
    

class Profile(models.Model):
    date_created=models.DateField(auto_now=True)
    school =models.OneToOneField(School, on_delete =models.CASCADE )
    school_logo=models.ImageField(upload_to='profile_pics')
    about=models.TextField(max_length=500)

    def __str__(self):
        return self.school.school_name


    # def save (self, *args, **kawrgs) :
    #     super().save (*args, **kawrgs)
    #     img = Image.open (self.image.path)
    #     if img. height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail (output_size)
    #         img.save (self.image.path)



class Contact(models.Model):
    school =models.OneToOneField(School, on_delete =models.CASCADE)
    date_created=models.DateField(auto_now=True)
    address=models.CharField(max_length=20)
    phone_number=models.CharField(max_length=20)
    mobile_number=models.CharField(max_length=20)
    email=models.EmailField(max_length=20)
    physical_address=models.CharField(max_length=20)
    pin_location=models.CharField(max_length=20)

    def __str__(self):
        return self.school.school_name


class Student(models.Model):
    school =models.ForeignKey(School, on_delete =models.CASCADE)
    date_created=models.DateField(auto_now_add=True)
    first_name=models.CharField(max_length=50)
    last_namgti e=models.CharField(max_length=50)
    adm_no= models.IntegerField()
    date_of_birth= models.DateField()
    date_joined= models.DateField(auto_now=True)
    grade=models.CharField( choices= GRADE, max_length=50)

    @property
    def fullname(self):
        return  '{}  {}'.format(self.first_name, self.last_name)

    def __str__(self):
        return self.fullname


class Teacher(models.Model):
    school =models.ForeignKey(School, on_delete =models.CASCADE)
    image=models.ImageField(upload_to="teacher_profile")
    date_created=models.DateField(auto_now_add=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    teach_grade=models.CharField( choices= GRADE, max_length=50)
    
    def __str__(self):
        return  '{} {}'.format(self.first_name, self.last_name)


class Gallery(models.Model):
    school =models.ForeignKey(School, on_delete =models.CASCADE )
    date_created=models.DateField(auto_now_add=True)
    title =models.CharField(max_length=30, null=True, blank=True)
    image=models.ImageField(upload_to='gallery')
    caption=models.TextField(max_length=200)

    def __str__(self):
        return  self.title  



class Subject(models.Model):
    subject_name =models.CharField(max_length=50)

    def __str__(self):
        return self.subject_name


class StrandCreate(models.Model):
    grade=models.CharField( choices= GRADE, max_length=50)
    subject=models.ForeignKey(Subject, on_delete=models.CASCADE)
    strand= models.CharField(max_length=50, help_text='Enter strand only')
    sub_strand1= models.CharField(max_length=200, blank= True, null=True)
    sub_strand2= models.CharField(max_length=200, blank= True, null=True)
    sub_strand3= models.CharField(max_length=200,blank= True, null=True)
    sub_strand4= models.CharField(max_length=200,blank= True, null=True)
    sub_strand5= models.CharField(max_length=200,blank= True, null=True)
    sub_strand6= models.CharField(max_length=200,blank= True, null=True)

    def __str__(self):
        return  '{} - {}- {}'.format(self.subject.subject_name,self.strand,self.grade)


class Assesment(models.Model):
    date_created=models.DateField(auto_now_add=True, blank=True, null=True)
    student=models.ForeignKey(Student, on_delete =models.CASCADE)
    strand= models.ForeignKey(StrandCreate,max_length=200, on_delete=models.CASCADE)

    EXPECTATION=(
        ('BE','BE'),
        ('AP','AP'),
        ('MT','MT'),
        ('EX','EX'),
    )
    expectation= models.CharField(choices= EXPECTATION, max_length= 10,
                                  help_text='KEY: EX- Exceeding expextation, MT-Meet Expectation, AP- Approaches epectation, BE- below expectation' )
    comment=models.TextField(max_length=200)
    def __str__(self):
        return '{} - {} - {}'.format(self.student.fullname,self.strand, self.expectation)

    

class Score(models.Model):
    student=models.ForeignKey(Student, on_delete=models.CASCADE)
    year= models.IntegerField(default= datetime.now().year)

    term=models.CharField( max_length=20)
    exam= models.CharField( max_length=20)
    Mathematics= models.IntegerField(default=0)
    English_language =models.IntegerField(default=0)
    Kiswahili=models.IntegerField(default=0)
    Hygiene_and_Nutrition=models.IntegerField(default=0)
    Environmental=models.IntegerField(default=0)
    Art_and_Craft=models.IntegerField(default=0)
    Music=models.IntegerField(default=0)
    Movement=models.IntegerField(default=0)
    Psychomotorcreative=models.IntegerField(default=0)
    Religious_education=models.IntegerField(default=0)
    

    def total_marks(self):
        self.marks =self.Mathematics + self.English_language +self.Kiswahili + self.Hygiene_and_Nutrition +self.Environmental +self.Art_and_Craft +self.Music + self.Movement + self.Psychomotorcreative + self.Religious_education
        return self.marks
    
    def __str__(self):
            return  '{} - {}'.format(self.student.fullname , self.exam)


   
    
class Message(models.Model):
    date_created=models.DateField(auto_now_add=True)
    name =models.CharField(max_length=80)
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    content=models.TextField(max_length=400)

    def __str__(self):
        return self.name
    



class Myclub(models.Model):
    date_created=models.DateField(auto_now_add=True)
    school =models.ForeignKey(School, on_delete =models.CASCADE)
    club_name =models.CharField(max_length=80)
    about_club =models.CharField(max_length=400)
    
    def __str__(self):
        return self.club_name


class AddtoClub(models.Model):
    club_name =models.ForeignKey(Myclub, on_delete =models.CASCADE)
    student=models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.club_name

class ClubActivity (models.Model):
    date_created=models.DateField(auto_now_add=True)
    school =models.ForeignKey(School, on_delete =models.CASCADE,)
    myclub =models.ForeignKey(Myclub, on_delete =models.CASCADE)
    activity =models.TextField(max_length=400)
    activity_image=models.ImageField(upload_to='club gallery')

    def __str__(self):
        return self.club_name
    


class Document(models.Model):
    school =models.ForeignKey(School, on_delete =models.CASCADE, default= 'none')
    TITLE=(

    ('Exam','Exam'),
    ('Fee Structure','Fee Structure'),
    ('Lesson plan','Lesson plan '),
    ('Schemes','Schemes'),
    )
    title = models.CharField(choices=TITLE, max_length=255)
    grade=models.CharField( choices= GRADE, max_length=50, default='none')
    document = models.FileField(upload_to='documents/')
    date_created = models.DateTimeField(auto_now_add=True)