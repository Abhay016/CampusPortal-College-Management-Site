"""
URL configuration for student_management_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views, hod_views, staff_views, student_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.BASE,name='base'),
    path('', views.LOGIN,name='login'),
    path('doLogin/', views.doLogin,name='doLogin'),
    path('doLogout/', views.doLogout,name='doLogout'),
    path('Profile', views.PROFILE,name='profile'),
    path('Hod/Home', hod_views.HOME,name='hod_home'),
    path('Hod/Student/Add', hod_views.ADD_STUDENT,name='add_student'),
    path('Hod/Student/View', hod_views.VIEW_STUDENT,name='view_student'),
    path('Hod/Student/Edit/<str:id>', hod_views.EDIT_STUDENT,name='edit_student'),
    path('Hod/Student/Update',hod_views.UPDATE_STUDENT,name='update_student'),
    path('Hod/Student/Delete/<str:admin>',hod_views.DELETE_STUDENT,name='delete_student'),
    path('Hod/Course/Add',hod_views.ADD_COURSE,name='add_course'),
    path('Hod/Course/View',hod_views.VIEW_COURSE,name='view_course'),
    path('Hod/Course/Edit/<str:id>',hod_views.EDIT_COURSE,name='edit_course'),
    path('Hod/Course/Update',hod_views.UPDATE_COURSE,name='update_course'),
    path('Hod/Course/Delete/<str:id>',hod_views.DELETE_COURSE,name='delete_course'),
    path('Hod/Staff/Add', hod_views.ADD_STAFF,name='add_staff'),
    path('Hod/Staff/View', hod_views.VIEW_STAFF,name='view_staff'),
    path('Hod/Staff/Edit/<str:id>', hod_views.EDIT_STAFF,name='edit_staff'),
    path('Hod/Staff/Update',hod_views.UPDATE_STAFF,name='update_staff'),
    path('Hod/Staff/Delete/<str:admin>',hod_views.DELETE_STAFF,name='delete_staff'),
    path('Hod/Subject/Add',hod_views.ADD_SUBJECT,name='add_subject'),
    path('Hod/Subject/View',hod_views.VIEW_SUBJECT,name='view_subject'),
    path('Hod/Subject/Edit/<str:id>', hod_views.EDIT_SUBJECT,name='edit_subject'),
    path('Hod/Subject/Update',hod_views.UPDATE_SUBJECT,name='update_subject'),
    path('Hod/Subject/Delete/<str:id>',hod_views.DELETE_SUBJECT,name='delete_subject'),
    path('Hod/Session/Add',hod_views.ADD_SESSION,name='add_session'),
    path('Hod/Session/View',hod_views.VIEW_SESSION,name='view_session'),
    path('Hod/Session/Edit/<str:id>', hod_views.EDIT_SESSION,name='edit_session'),
    path('Hod/Session/Update',hod_views.UPDATE_SESSION,name='update_session'),
    path('Hod/Session/Delete/<str:id>',hod_views.DELETE_SESSION,name='delete_session'),
    path('Hod/Send_Notification', hod_views.STAFF_SEND_NOTIFICATION,name='staff_send_notification'),
    path('Hod/Save_Notification', hod_views.STAFF_SAVE_NOTIFICATION,name='staff_save_notification'),
    path('Hod/Student_Send_Notification', hod_views.STUDENT_SEND_NOTIFICATION,name='student_send_notification'),
    path('Hod/Student_Save_Notification', hod_views.STUDENT_SAVE_NOTIFICATION,name='student_save_notification'),
    path('Hod/ViewLeave', hod_views.STAFF_VIEW_LEAVE,name='staff_view_leave'),
    path('Hod/ApproveLeave/<str:id>', hod_views.STAFF_APPROVE_LEAVE,name='staff_approve_leave'),
    path('Hod/DisapproveLeave/<str:id>', hod_views.STAFF_DISAPPROVE_LEAVE,name='staff_disapprove_leave'),
    path('Hod/feedbackReply', hod_views.STAFF_FEEDBACK_REPLY, name='staff_feedback_reply'),
    path('Hod/feedbackSave', hod_views.STAFF_FEEDBACK_SAVE, name='staff_feedback_save'),
    path('Hod/StudentfeedbackReply', hod_views.STUDENT_FEEDBACK_REPLY, name='student_feedback_reply'),
    path('Hod/StudentfeedbackSave', hod_views.STUDENT_FEEDBACK_SAVE, name='student_feedback_save'),
    path('Hod/Student/ViewLeave', hod_views.STUDENT_VIEW_LEAVE,name='student_view_leave'),
    path('Hod/Student/ApproveLeave/<str:id>', hod_views.STUDENT_APPROVE_LEAVE,name='student_approve_leave'),
    path('Hod/Student/DisapproveLeave/<str:id>', hod_views.STUDENT_DISAPPROVE_LEAVE,name='student_disapprove_leave'),
    path('Hod/ViewAttendance', hod_views.VIEW_ATTENDANCE, name='hod_view_attendance'),


    path('Staff/Home', staff_views.HOME,name='staff_home'),
    path('Staff/Notifications', staff_views.NOTIFICATIONS,name='notifications'),
    path('Staff/mark_as_done/<str:status>', staff_views.MARK,name='mark'),
    path('Staff/ApplyLeave', staff_views.STAFF_LEAVE,name='staff_leave'),
    path('Staff/SaveLeave', staff_views.STAFF_SAVE_LEAVE,name='staff_save_leave'),
    path('Staff/Feedback', staff_views.STAFF_FEEDBACK,name='staff_feedback'),
    path('Staff/SaveFeedback', staff_views.STAFF_SAVE_FEEDBACK,name='staff_save_feedback'),
    path('Staff/TakeAttendance', staff_views.TAKE_ATTENDANCE, name='staff_take_attendance'),
    path('Staff/SaveAttendance', staff_views.SAVE_ATTENDANCE, name='staff_save_attendance'),
    path('Staff/ViewAttendance', staff_views.VIEW_ATTENDANCE, name='staff_view_attendance'),
    path('Staff/AddResult', staff_views.ADD_RESULT, name='staff_add_result'),
    path('Staff/SaveResult', staff_views.SAVE_RESULT, name='staff_save_result'),


    path('Student/Home', student_views.HOME,name='student_home'),
    path('Student/Notifications', student_views.NOTIFICATIONS,name='student_notifications'),
    path('Student/mark_as_done/<str:status>', student_views.MARK,name='student_mark'),
    path('Student/Feedback', student_views.STUDENT_FEEDBACK,name='student_feedback'),
    path('Student/SaveFeedback', student_views.STUDENT_SAVE_FEEDBACK,name='student_save_feedback'),
    path('Student/ApplyLeave', student_views.STUDENT_LEAVE,name='student_leave'),
    path('Student/SaveLeave', student_views.STUDENT_SAVE_LEAVE,name='student_save_leave'),
    path('Student/ViewAttendance', student_views.VIEW_ATTENDANCE, name='student_view_attendance'),
    path('Student/ViewResult', student_views.VIEW_RESULT, name='student_view_result'),
    

    path('Profile/update', views.PROFILE_UPDATE, name='profile_update')
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
