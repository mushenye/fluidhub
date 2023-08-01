import datetime
import os
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView
from django.conf import settings
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from .forms import AssesmentForm, DocumentForm, SchoolForm, StudentForm, ScoreForm, ProfileForm,CustomerRegistrationForm, GalleryForm, TeacherForm,Teacher, MessageForm,MyclubForm,AddClubForm,ClubActivityForm, ContactForm
from . models import AddtoClub, Assesment, Document,School,Student, Score,Subject, Profile,StrandCreate,Gallery, Myclub, ClubActivity,Contact
import pandas as pd
# Create your views here.

def home(request, ):
    items= Score.objects.all()
    item=items.values()
    df= pd.DataFrame(item)
    my_dict={
        'df':df.to_html(classes=["table-bordered", "table-striped", "table-hover"])
    }

    
    return render(request, 'learner/home.html',context=my_dict)


@login_required

def profile(request, value ):

    my_school=School.objects.get(school_code = value)
    
    profile= Profile.objects.filter(school = my_school)
    gallery= Gallery.objects.filter(school = my_school).order_by('-date_created')[:4]
    teacher=Teacher.objects.filter(school=my_school)
    contact=Contact.objects.filter(school=my_school)
    tech=Teacher.objects.filter(school=my_school).count()
    stud=Student.objects.filter(school=my_school).count()
    myclubs=Myclub.objects.filter(school=my_school)

    context={
        'profile':profile,
        'gallery' :gallery,
        'teacher':teacher,
        'my_school':my_school,
        'myclubs': myclubs,
        'contact':contact
    }

    return render(request, 'learner/profile.html',context)



@login_required

def profileform(request, value):

    my_school=School.objects.get(school_code = value)
    my_data = {
            'school': my_school,
        }

    form=ProfileForm(initial= my_data)
    if request.method =='POST':
        form=ProfileForm(request.POST, request.FILES,initial= my_data )
        if form.is_valid():
            form.save()
            return redirect('/accounts/profile/%s' %value)
   
    context={
        'form':form
    }
    
    return render(request, 'learner/profileform.html', context)

@login_required

def profile_edit(request,pk ):
    context={}
   
    profile=Profile.objects.get(id=pk)
    value=profile.school.school_code
    form=ProfileForm( instance=profile )
    if request.method =='POST':
        form=ProfileForm(request.POST, request.FILES,instance=profile )
        if form.is_valid():
            form.save()
           
            return redirect('/accounts/profile/%s' %value)
           
    context={
        'form':form
    }
    
    return render(request, 'learner/updateprofile.html', context)

    
@login_required

def personregister(request):
    form = CustomerRegistrationForm ()
    if request.method == 'POST':
        form=CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/account/login")

    context={
        'form':form
    }
    return render(request,'learner/register.html', context)


# def dataframe(request,value):
#     items= Score.objects.filter(exam=value)
#     item=items.values()
#     df= pd.DataFrame(item)
#     my_dict={
#         'df':df.to_html
#     }
    

#     return render(request, 'learner/dataframe.html', context=my_dict)

@login_required

def subjects (request):
    student_obj=Student.objects.all()
    subjects=Subject.objects.all().count()
    score_data= Score.objects.all()
    subject_name = []
    subject_data=Subject.objects.all()

    for subject in subject_data:
        subject_name.append(subject.subject_name)

    context={
        'subject_name':subject_name
    }
    return render (request, 'learner/subject.html', context)

    
# assesment details
@login_required

def Teacher_account (request) :
    if request.session.has_key('teacher') :
        return render(request, 'Teacher_account.html' )
    elif request.session.has_key('student'):
        return render (request,'Studentaccount . html')


@login_required

def assess (request, pk):
    
    student= Student.objects.get(id=pk)
    strand= StrandCreate.objects.filter(grade= student.grade)
    value= student.id
    
    my_data = {
            'student': student,    
        }
    form =AssesmentForm(initial= my_data)
    if request.method == 'POST':
        form=AssesmentForm(request.POST, initial= my_data)
        if form.is_valid():
            form.save()
            return redirect ( '/view/asses/%d' %value)
    context={
        'form':form,
        'student':student
    }
    return render(request,'learner/assess.html' , context)


@login_required

def view_asses(request,pk):
    
    user=request.user
    student =Student.objects.get(id=pk)
    assesment=Assesment.objects.all()
    asses=assesment.filter( student = pk)

    context={
        'asses':asses,
        'student':student
    }
    return render(request,'learner/asess_view.html', context)


#student model

# list 
@login_required

def pass_code(request):
    user=request.user
    my_passcode=request.POST.get("my_passcode")
    
    schools=School.objects.all().filter( passcode=my_passcode).filter(user=user)

    my_profile=Profile.objects.all()
    context ={
                "schools":schools,
                'my_profile':my_profile
            }

    return render(request, "learner/passcode.html",context )

@login_required

def register_school(request):
    user=request.user
    my_data={
        'user':user
    }
    form=SchoolForm(initial=my_data)
    school = request.POST.get("school_name")
    schoolcode=School.objects.all().filter(school_name = school).filter(user=user)
    if request.method =='POST':
        form=SchoolForm(request.POST, initial=my_data )
        if form.is_valid(): 
            form.save()
    context={
        'form':form,
        'schoolcode':schoolcode 
     }

    return render(request, 'learner/schoolregister.html', context)

@login_required

def displaycode(request):
    school = request.POST.get("school_name")
    school=School.objects.all()
    schoolcode=school.filter(school_name = "school")

    context={
        'schoolcode':schoolcode,
        'school':school
    }
    return render(request, 'learner/yourcode.html', context)








@login_required

def school(request):

    user=request.user
    
    schools=School.objects.all()
    context={
        'schools':schools
    }

    return render(request,'learner/school_list.html', context)
        
         

@login_required

def students_view(request, value):
    
    user=request.user
    my_school=School.objects.filter(school_code=value)
    
    students=Student.objects.filter(school= value)
    
# filter according to grade gets response from request.POST

    if 'RE'== request.POST.get('RE'):
        students=Student.objects.filter(school= value).filter(grade = 'RE')
    elif 'P1'== request.POST.get('P1'):
        students=Student.objects.filter(school= value).filter(grade = 'P1')
    elif 'P2'== request.POST.get('P2'):
        students=Student.objects.filter(school= value).filter(grade = 'P2')
    elif 'G1'== request.POST.get('G1'):
        students=Student.objects.filter(school= value).filter(grade = 'G1')
    elif 'G2'== request.POST.get('G2'):
        students=Student.objects.filter(school= value).filter(grade = 'G2')
    elif 'G3'== request.POST.get('G3'):
        students=Student.objects.filter(school= value).filter(grade = 'G3')
    elif 'G4'== request.POST.get('G4'):
        students=Student.objects.filter(school= value).filter(grade = 'G4')
    elif 'G5'== request.POST.get('G5'):
        students=Student.objects.filter(school= value).filter(grade = 'G5')
    elif 'G6'== request.POST.get('G6'):
        students=Student.objects.filter(school= value).filter(grade = 'G6')
    else:
        students=Student.objects.filter(school= value)

    context={
                                                        'my_school':my_school,
        'students':students
    }

    return render(request, 'learner/students_view.html', context)


@login_required

def student_details(request, pk):
    student=Student.objects.get(id=pk)
    club=AddtoClub.objects.filter(student=student)
    teacher=Teacher.objects.filter(school=student.school).filter(teach_grade=student.grade)
    context={
        'student':student,
        'club':club,
        'teacher':teacher
    }
    return render(request, 'learner/studentdetails.html', context)




def student_scores(request,value):
   
    results= Score.objects.filter(exam=value)
    context={
        'results':results
    }
    return render (request, 'learner/student_result.html', context)






# view report card
@login_required

def student_score(request, pk):
    
    student=Student.objects.get(id=pk)

    result= Score.objects.filter(student=pk).exclude(
    
        Mathematics = 0,
        English_language =0,
        Kiswahili= 0,
        Hygiene_and_Nutrition=0,
        Environmental= 0,
        Art_and_Craft= 0,
        Music=0,
        Movement=0, 
        Psychomotorcreative= 0,
        Religious_education= 0,
    )
    context={
        'student':student,
        'result':result
    }

    return render (request, 'learner/student_report.html', context)


# add student

@login_required

def studentform(request, value):

    my_school=School.objects.get(school_code = value)
    my_data = {
            'school': my_school,
        }

    form=StudentForm(initial= my_data)
    if request.method =='POST':
        form=StudentForm(request.POST, initial= my_data)
        if form.is_valid():
            form.save()
            return redirect('/school/%s' %value)
   
    context={
        'form':form,
        'my_school':my_school
    }
    
    return render(request, 'learner/add_student.html', context)


@login_required
def editstudent(request,pk ):
    context={}

    persons=Student.objects.get(id=pk)
    form=StudentForm(instance=persons)
    value= persons.school.school_code
    if request.method=="POST":
        form=StudentForm(request.POST, instance=persons)
        if form.is_valid():
            form.save()
            return redirect('/school/%s' %value)
 
    context={                                                                     
        'form':form
    }

    return render(request, 'learner/edit_student.html', context)

# add result
@login_required

def scoreform(request,pk):

    student= Student.objects.get(id=pk)
    result= Score.objects.filter(student=student)
    month_now =datetime.datetime.now().month 

    if month_now > 1 and month_now < 5:
        when_date= 'Term one'
    elif month_now > 5 and month_now < 8 :
        when_date= 'Term two'
    else:
        when_date= 'Term three'
    

    if month_now == 2 or month_now == 5:
        data_now = 'Opener Exam'
    elif month_now ==3 or month_now == 6:
        data_now = 'Mid Term exam'
    elif month_now == 4 or month_now == 7:
        data_now= 'End Term Exam'
    elif month_now == 10 and  month_now== 11:
        data_now = 'End Year Exams'
    elif month_now == 9:
        data_now= 'Opener/Midterm Exams'

    my_data= {
        'term': when_date,
        'exam': data_now,
        'student': pk
    }
    
    value= student.id
    form=ScoreForm( initial=my_data)
    if request.method =='POST':
        form=ScoreForm(request.POST, initial=my_data) 
        if form.is_valid():
            form.save()
            return redirect('/school/view/%d' %value)
   
    context={
        'form':form,
        'student':student,
        'result':result,
        'my_data':my_data
    }
    
    return render(request, 'learner/add_score.html', context)

# edit score
@login_required

def editscore(request,pk ):
    score_obj=Score.objects.get(id=pk)
    value=score_obj.student.id
    form=ScoreForm(instance= score_obj)
    if request.method =="POST":
        form=ScoreForm(request.POST, instance= score_obj)
        if form.is_valid():
            form.save()
            return redirect('/school/view/%d' %value)
    context={
        'form':form
    }

    return render(request, 'learner/edit_score.html', context)


#  profile page  and view all 
@login_required

def viewgallery(request, value):
    my_school=School.objects.get(school_code = value)
    gallery= Gallery.objects.filter(school=my_school)

    context= {
        'gallery':gallery
    }

    return render (request, 'learner/gallery.html', context)

@login_required

def maingallery (request, value):
    my_school=School.objects.get(school_code = value)
    gallery= Gallery.objects.filter(school=my_school).order_by('-date_created')

    context= {
            'gallery':gallery
        }

    return render(request, 'learner/chatgallery.html', context)


# add images to gallery 
@login_required

def addgallery(request, value):

    my_school=School.objects.get(school_code = value)
    my_data = {
            'school': my_school,
        }     
    form=GalleryForm(initial= my_data)
    if request.method =='POST':
        form=GalleryForm(request.POST,request.FILES, initial= my_data)
        if form.is_valid():
            form.save()
            return redirect('/accounts/profile/%s' %value)
   
    context={
        'form':form
    }
    
    return render(request, 'learner/addgallery.html', context)

@login_required

def websiteview(request):
    my_school=School.objects.all()
    gallery = Gallery.objects.all()
    slide = Gallery.objects.all().order_by('-date_created')[:3]
    context={
        'my_school':my_school,
        'gallery':gallery,
        'slide':slide
    }

    return render(request, 'learner/mysite.html', context)



# add teacher
@login_required

def teacheradd(request, value ):

    my_school=School.objects.get(school_code = value)
    my_data = {
            'school': my_school,
        }
    form=TeacherForm(initial= my_data)

    if request.method =='POST':
        form=TeacherForm(request.POST,request.FILES,initial= my_data)
        if form.is_valid():
            form.save()
            return redirect('/accounts/profile/%s' %value)
   
    context={
        'form':form,
        'my_school':my_school
    }
    
    return render(request, 'learner/addteacher.html', context)


@login_required

def teacherupdate(request, pk ):
    teacher=Teacher.objects.get(id = pk)
    form=TeacherForm(instance=teacher)
    if request.method =='POST':
        form=TeacherForm(request.POST,request.FILES, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('/view/teacher/%d' %pk)
    context={
        'form':form,
        'teacher':teacher
    }
    return render(request, 'learner/teacherupdate.html', context)



# view teachers details 
@login_required

def teacherview(request, pk):
    teacher= Teacher.objects.get(id=pk)
    context={
        'teacher':teacher
    }
    return render( request, 'learner/teacherview.html', context)

@login_required

def confirmdelete(request, pk):
    teacher= Teacher.objects.get(id=pk)
    context={
        'teacher':teacher
    }
    return render(request, 'learner/teacherdelete.html', context)

@login_required

def teacherdelete(request, pk):
    teacher= Teacher.objects.get(id=pk)
    teacher.delete()
    return  HttpResponseRedirect(reverse('pass_code'))

@login_required

def messagecreate(request):
    form=MessageForm()
    if request.method== 'POST':
        form=MessageForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('/')
    context={
            'form':form
        }
        
    return render(request, 'learner/messagecreate.html', context)

@login_required

def myclub(request,value):
    my_school=School.objects.get(school_code = value)
    my_data = {
            'school': my_school,
    }
    form=MyclubForm(initial= my_data)
    if request.method== 'POST':
        form=MyclubForm(request.POST, initial= my_data)
        if form.is_valid():
            form.save()
            redirect('/')
    context={
            'form':form
        }
        
    return render(request, 'learner/add_club.html', context)


@login_required

def addtoclub(request, pk):
    student=Student.objects.get(id=pk)

    club = Myclub.objects.filter(school=student.school.school_code)
   
    my_data = {
            'student': student,
            'club_name':club
    }
    form=AddClubForm(initial= my_data)
    if request.method== 'POST':
        form=AddClubForm(request.POST, initial= my_data)
        if form.is_valid():
            form.save()
            return redirect('/school/view/%d' %pk)
    context={
            'form':form,
            'student':student
        }  
    return render(request, 'learner/addtoclub.html', context)


@login_required

def myclubview(request,value):
    my_school=School.objects.get(school_code = value)

    activity=ClubActivity.objects.filter(school= my_school)
    context ={ 
        'activity':activity
    }
    return render(request, 'learner/viewmyclub.html',context)


@login_required

def createactivity(request, pk):
    my_club=Myclub.objects.get(id=pk)
    school=my_club.school
    value=school.school_code
    my_data={
        'school':school,
        'myclub':my_club
    }
    form = ClubActivityForm(initial=my_data)
    if request.method == 'POST':
        form=ClubActivityForm(request.POST, request.FILES,initial=my_data)
        if form.is_valid():
            form.save()
            return redirect('account/createprofile/%s' %value)

    context= {
       'form':form     
    }
    return render(request,'learner/clubactivity.html', context)

# add contact function

def contact(request,value):

    #  to get the initial value ie the school name to a form 
    my_school=School.objects.get(school_code = value)
    my_data = {
            'school': my_school,
    }
    form=ContactForm(initial= my_data)
    if request.method== 'POST':
        form=ContactForm(request.POST, initial= my_data)
        if form.is_valid():
            form.save()

            return redirect('/account/createprofile/%s' %value)
    context={
            'form':form
        }
        
    return render(request, 'learner/contact.html', context)


# update contact 
@login_required

def updatecontact(request,pk):

    contact=Contact.objects.get(id=pk)
    value=contact.school.school_code
    form=ContactForm(instance=contact)
    if request.method== 'POST':
        form=ContactForm(request.POST,instance=contact )
        if form.is_valid():
            form.save()
            return redirect('/accounts/profile/%s' %value)
    context={
            'form':form
        } 
    return render(request, 'learner/updatecontact.html', context)


@login_required


def document(request,value):

    #  to get the initial value ie the school name to a form 
    my_school=School.objects.get(school_code = value)
    my_data = {
            'school': my_school,
    }
    form=DocumentForm(initial= my_data)
    if request.method== 'POST':
        form=DocumentForm(request.POST,request.FILES, initial= my_data)
        if form.is_valid():
            form.save()
            
            return redirect('/accounts/profile/%s' %value)
    context={
            'form':form
        }
        
    return render(request, 'learner/documentupload.html', context)

@login_required


def download(request, pk):
    document = get_object_or_404(Document, id=pk)
    response = HttpResponse(document.document, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{document.document.name}"'
    return response


class DocumentListView(ListView):
    model = Document
    template_name = 'documents.html'
    context_object_name = 'documents'

  

def website(request):
    user=request.user
    teacher=Teacher.objects.all().order_by('-date_created')[:10]
    gallery =Gallery.objects.all().order_by('-date_created')[:3]
    activity=ClubActivity.objects.all().order_by('-date_created')[:10]
    document=Document.objects.all().order_by('-date_created')[:10]
    profile=Profile.objects.all().order_by('-date_created')[:10]
    
    context={
        'teacher':teacher,
        'gallery': gallery,
        'activity':activity,
        'document':document,
        'profile':profile
    }
    return render(request,'learner/mysite.html', context)
@login_required

def contactus(request):
    form=MessageForm()
    if request.method== 'POST':
        form=MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/contact')
    context={
            'form':form
        }
    return render(request,'learner/contactus.html', context)
@login_required

def activities(request):
    activity=ClubActivity.objects.all().order_by('-date_created')
    context={
        'activity':activity,
        
    }
    return render(request, 'learner/activities.html',context) 
@login_required

def galleryview(request):
    gallery= Gallery.objects.all().order_by('-date_created')
    context={
        
        'gallery':gallery
    }
    return render(request, 'learner/galleryview.html',context) 


@login_required

def viewprofile(request, value ):

    my_school=School.objects.get(school_code = value)
    
    profile= Profile.objects.filter(school = my_school)
    gallery= Gallery.objects.filter(school = my_school).order_by('-date_created')[:4]
    teacher=Teacher.objects.filter(school=my_school)
    contact=Contact.objects.filter(school=my_school)
    
    stud=Student.objects.filter(school=my_school).count()
    myclubs=Myclub.objects.filter(school=my_school)

    context={
        'profile':profile,
        'gallery' :gallery,
        'teacher':teacher,
        'my_school':my_school,
        'myclubs': myclubs,
        'contact':contact
    }

    return render(request, 'learner/viewmyprofile.html',context)