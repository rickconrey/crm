from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.edit import UpdateView, ModelFormMixin
from crm.models import Student, Contact, Relationship
from crm.models import ContactEmail, ContactPhone
from crm.models import StudentEmail, StudentPhone
from crm.models import StatusStudent, Attendance
from crm.models import Test, TestScore, Tip

def listing(request, student_id):
    student_list = Student.objects.all()
    paginator = Paginator(student_list, 1)

    page = student_id
    try:
        student_page = paginator.page(page)
    except PageNotAnInteger:
        student_page = paginator.page(1)
    except EmptyPage:
        student_page = paginator.page(paginator.num_pages)

    results = view_student(student_page.number)
    results['student_page'] = student_page

    return render(request, 'crm/view.html', results)


def view_student(student_id):#request, student):#student_id):
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

    student_info = {'student':student, 'age':age, 'status':status,
                    'classification':classification, 'contacts':contacts,
                    'contact_phone':contact_phone,
                    'contact_email':contact_email, 'attendance':attendance,
                    }

    return student_info

    #return render(request, 'crm/view.html', {'student':student,
    #                                         'age':age,
    #                                         'classification':classification,
    #                                         'contacts':contacts,
    #                                         'contact_phone':contact_phone,
    #                                         'contact_email':contact_email,
    #                                         'status':status,
    #                                         'attendance':attendance,
    #                                         #'next_test_date':next_test_date,
    #                                         })


class StudentUpdate(UpdateView):
    model = Student
    success_url = '/crm/1'   

    def form_valid(self, form):
        self.object = form.save(commit=False)
        Relationship.objects.filter(student=self.object).delete()
        for contact in form.cleaned_data['contacts']:
            relationship = Relationship()
            relationship.student = self.object
            relationship.contact = contact
            relationship.save()
        
        return super(StudentUpdate, self).form_valid(form)

class ContactUpdate(UpdateView):
    model = Contact
    success_url = '/crm/1'

