from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from app.models import Course, Session_Year, CustomUser, Student, Staff, Subject, Student_Notification, Student_leave, Student_feedback, Attendance, AttendanceReport, StudentResult
from django.contrib import messages

def HOME(request):
    return render(request, 'Student/home.html')

@login_required(login_url='/')
def NOTIFICATIONS(request):
    student = Student.objects.filter(admin=request.user.id)
    for i in student:
        student_id =i.id
        
        notification = Student_Notification.objects.filter(student_id = student_id)

        context = {
            'notification': notification,
        }
    return render(request, 'Student/notification.html', context)

@login_required(login_url='/')
def MARK(request, status):
    notification = Student_Notification.objects.get(id = status)
    notification.status = 1
    notification.save()
    return redirect('student_notifications')

@login_required(login_url='/')
def STUDENT_LEAVE(request):
    student = Student.objects.filter(admin = request.user.id)
    for i in student:
        student_id = i.id
        student_leave_history = Student_leave.objects.filter(student_id=student_id)
        context = {
            'student_leave_history': student_leave_history,
        }

    return render(request, 'Student/apply_leave.html', context)

@login_required(login_url='/')
def STUDENT_SAVE_LEAVE(request):
    if request.method == 'POST':
        leave_date = request.POST.get('leave_date')
        leave_message = request.POST.get('leave_message')
        student = Student.objects.get(admin = request.user.id)
        leave = Student_leave(
            student_id = student, 
            data = leave_date,
            message = leave_message
        )
        leave.save()
        messages.success(request, 'Your request is submitted successfully!')
        return redirect('student_leave')

def STUDENT_FEEDBACK(request):
    student_id = Student.objects.get(admin = request.user.id)
    feedback_history = Student_feedback.objects.filter(student_id=student_id)
    context = {
        'feedback_history': feedback_history,
    }
    return render(request, 'Student/feedback.html', context)

def STUDENT_SAVE_FEEDBACK(request):
    if request.method == 'POST':
        feedback = request.POST.get('feedback_message')
        student = Student.objects.get(admin=request.user.id)
        feedback = Student_feedback(
            student_id = student, 
            feedback = feedback,
            feedback_reply = "",
        )
        feedback.save()
        messages.success(request, 'Feedback was successfully sent.')
        return redirect("student_feedback")

def VIEW_ATTENDANCE(request):
    student = Student.objects.get(admin=request.user.id)
    subjects = Subject.objects.filter(course=student.course_id)
    action = request.GET.get('action')
    get_subject=None
    attendance_report=None
    if action is not None:
        if request.method == "POST":
            subject_id = request.POST.get('subject_id')
            get_subject = Subject.objects.get(id=subject_id)
            attendance_report = AttendanceReport.objects.filter(student_id=student, attendance_id__subject_id=subject_id)
    context = {
        'subjects': subjects,
        'action' : action,
        'get_subject': get_subject,
        'attendance_report': attendance_report,
    }
    return render(request, 'Student/view_attendance.html', context)

def VIEW_RESULT(request):
    student = Student.objects.get(admin=request.user.id)
    result=StudentResult.objects.filter(student_id=student)
    mark=None
    for i in result:
        assignment_marks=i.assignment_marks
        exam_marks=i.exam_marks
        mark=assignment_marks+exam_marks
    context = {
        'result': result,
        'mark': mark
    }
    return render(request, 'Student/view_result.html', context)