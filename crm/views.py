from django.http import HttpResponse, Http404
from django.shortcuts import render
from crm.models import Student, Contact, Relationship
from crm.models import ContactEmail, ContactPhone
from crm.models import StudentEmail, StudentPhone
from crm.models import StatusStudent, Attendance
from crm.models import Test, TestScore, Tip

def view_student(request, student_id):
    try:
        student = Student.objects.get(pk=student_id)
        age = student.get_age()
        classification = student.get_classification()
        contacts = Relationship.objects.filter(student=student)
        
        contact_email = []
        for c in contacts:
            contact_email.append(ContactEmail.objects.filter(contact=c))

        contact_phone = []
        for c in contacts:
            contact_phone.append(ContactPhone.objects.filter(contact=c))

        status = StatusStudent.objects.filter(student=student).order_by(
                                                        '-start_date')
        attendance = Attendance.objects.filter(
                                        student=student).order_by(
                                             '-attendance_date')[:5]
        # not correct...
        #next_test_date = Test.objects.filter(student=student).order_by(
        #                                    '-test_group')[0]
        
    except Student.DoesNotExist:
        raise Http404
    return render(request, 'crm/view.html', {'student':student,
                                             'age':age,
                                             'classification':classification,
                                             'contacts':contacts,
                                             'contact_phone':contact_phone,
                                             'contact_email':contact_email,
                                             'status':status,
                                             'attendance':attendance,
                                             #'next_test_date':next_test_date,
                                             })
