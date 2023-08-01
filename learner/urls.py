from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import LoginForm,MyPasswordResetForm,MyPasswordChangeForm,MySetPasswordForm
from django.contrib import admin
from .views import  DocumentListView, download

urlpatterns = [
    path('mywebview', views.websiteview, name='website'),
    path('contact', views.contactus, name='contactus'),

    path('', views.website, name= 'home'),
    path('pass/verify', views.pass_code, name= 'pass'),
    # path('school/',views.school, name= 'school'),
    path('create/message/dfghrtyapoodhteyrsddavertdffa',views.messagecreate, name= 'message'),
    path('activities/view/myclub', views.activities, name= 'activities'),
    path('viewmyprofile/<slug:value>', views.viewprofile, name='viewprofile'),
    path('galleryview/view/mygallery', views.galleryview, name= 'galleryview'),



    path('create/myclub/<slug:value>/', views.myclub, name= 'createclub'),
    path('create/myclub/add_student/<int:pk>/', views.addtoclub, name= 'addtoclub'),
    path('myclub/view/<slug:value>', views.myclubview, name= 'myclubview'),
    path('create/myclubactivity/<int:pk>', views.createactivity, name= 'createactivity'),


    # path ('<slug:value>', views.student_scores, name ='viewreport'),
    path('view/add/asses/<int:pk>',views.assess, name= 'assess'),
    path('view/asses/<int:pk>', views.view_asses, name='assess-view'),
    path('shgnndhhoerf&gg/',views.school, name= 'school'),
    path('myschool/<slug:value>/', views.students_view, name='school_view'),
    path ('add/addstudent/<slug:value>', views.studentform, name ='add_student'),
    path('view/student/details/<int:pk>',views.student_details, name= 'studentdetails'),

    # path('school/<slug:value>/<value>', views.students_grade, name='school-view'),

    # path('school/grade1',views.student_grade1, name='grade1'),

    path('account/updatecontact/<int:pk>', views.updatecontact, name='updatecontact'),
    path('account/contact/<slug:value>', views.contact, name='contact'),
    path('account/createprofile/<slug:value>', views.profileform, name='myprofile'),
    path('account/editprofile/<int:pk>', views.profile_edit, name='editprofile'),
    path ('view/result/', views.student_score, name ='report'),
    path ('view/result/<slug:value>', views.student_scores, name ='viewreport'),
    path('view/add_result/<int:pk>', views.scoreform, name='add_result'),



#  document upload urls

    path('document/upload/<slug:value>', views.document, name='upload'),
    path('document/list/view', DocumentListView.as_view(), name='documentlist'),
    path('download/<int:pk>/', download, name='download'),


    path('view/addteacher/<slug:value>', views.teacheradd, name='teacheradd'),
    path('view/teacher/<int:pk>', views.teacherview, name='teacherview'),
    path('view/teacher/update/<int:pk>', views.teacherupdate, name='teacherupdate'),
    path('view/teacher/confirmdelete/<int:pk>', views.confirmdelete, name='confirmdelete'),
    path('view/teacher/delete/<int:pk>', views.teacherdelete, name='teacherdelete'),



    path('school/view/<int:pk>/', views.student_score, name='result'),
    # path ('result/', views.student_scores, name ='report'),
    # path ('result/<int:pk>', views.student_score, name ='report'),

    path ('add/addstudent/', views.studentform, name ='add_student'),
    path ('edit/editstudent/<int:pk>/', views.editstudent, name ='student_update'),
    path ('edit/editscore/<int:pk>/', views.editscore, name ='score_update'),

    path('view/subject/', views.subjects, name='subject'),
    path('view/add_result/', views.scoreform, name='add_result'),
    
    path('gallery/add/image/<slug:value>', views.addgallery, name='add_photo'),
    path('view/gallery/<slug:value>', views.maingallery, name='gallery'),


    path('school/register/', views.register_school, name='school_register'),
    path('displaycode/', views.displaycode, name='displaycode'),


     #authentication

    path('accounts/profile/<slug:value>', views.profile, name='profile'),
    path('register/',views.personregister, name ='register' ),
    path('account/login', auth_view.LoginView.as_view(template_name='learner/login.html',authentication_form=LoginForm), name='login'),
    path('passwordchange/',auth_view.PasswordChangeView.as_view(template_name='learner/changepassword.html',form_class=MyPasswordChangeForm,success_url='/passwordchangedone'),name='passwordchange'),
    path('passwordchangedone/',auth_view.PasswordChangeDoneView.as_view(template_name='learner/changepassworddone.html' ),name='passwordchangedone'),
    path('logout/', auth_view.LogoutView.as_view(next_page ='login'), name='logout'),
    #password reset url
    path('password-reset/',auth_view.PasswordResetView.as_view(template_name='learner/password_reset.html', form_class= MyPasswordResetForm),name='password_reset'),
    path('password-reset/done',auth_view.PasswordResetDoneView.as_view(template_name='learner/password_reset_done.html'),name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>',auth_view.PasswordResetConfirmView.as_view(template_name='learner/password_reset_confirm.html', form_class=MySetPasswordForm),name='passsword_reset_confirm'),
    path('password_reset_complete/',auth_view.PasswordResetCompleteView.as_view(template_name='learner/password_reset_complete.html'), name='password_reset_complete'),



]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



admin.site.site_header= "Simani Technologies"
admin.site.site_title= "Simani Technologies"
admin.site.site_index_title = "welcome to simani technologies"