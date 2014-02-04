from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.edit import UpdateView, ModelFormMixin
from django.views.generic import ListView, View
from django.forms.models import modelform_factory, modelformset_factory
from django.core.exceptions import ObjectDoesNotExist
from crm.models import Student, Contact, Relationship
from crm.models import ContactEmail, ContactPhone
from crm.models import StudentEmail, StudentPhone
from crm.models import StatusStudent, Attendance
from crm.models import Test, TestScore, Tip, TippingGroup
from crm.models import TippingStudent, Barcode
from datetime import date, time
import datetime

# utilities

# get path
def get_path_id(path_list):
    for item in path_list:
        if item.isdigit():
            return item

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


def scanner(request):
    return render(request, 'crm/scanner.html',)

def view_student(student_id):#request, student):#student_id):
    try:
        student = Student.objects.get(pk=student_id)
        age = student.get_age()
        classification = student.get_classification()
        contacts = Relationship.objects.filter(student=student)
        tipping_group = student.get_next_tipping()       
        last_test = student.get_last_test_date()
        current_status = student.get_current_status()
        add_tipping = student.add_next_tipping()
        groups = student.get_groups()

        contact_email = []
        for c in contacts:
            contact_email.append(ContactEmail.objects.filter(contact=c))

        contact_phone = []
        for c in contacts:
            contact_phone.append(ContactPhone.objects.filter(contact=c))

        student_email = StudentEmail.objects.filter(student=student)
        student_phone = StudentPhone.objects.filter(student=student)

        status = StatusStudent.objects.filter(student=student).order_by(
                                                        '-start_date')
        attendance = Attendance.objects.filter(
                                        student=student).order_by(
                                             '-attendance_date')[:5]
        code = student.generate_barcode(1)
        # not correct...
        #next_test_date = Test.objects.filter(student=student).order_by(
        #                                    '-test_group')[0]
        StudentForm = modelform_factory(Student,
              #  exclude=("limitations","benefits","state","city","zipcode",
              #      'address1','address2'))
                fields=("first_name", "last_name", "gender",
                    "anniv_month", "rank", "total_years"))
        print StudentForm.as_table
    except Student.DoesNotExist:
        raise Http404

    student_info = {'student':student, 'age':age, 'status':status,
                    'classification':classification, 'contacts':contacts,
                    'contact_phone':contact_phone,
                    'contact_email':contact_email, 'attendance':attendance,
                    'student_email':student_email, 
                    'student_phone':student_phone,
                    'tipping_group':tipping_group, 'last_test':last_test,
                    'current_status':current_status, 'add_tipping':add_tipping,
                    'groups':groups, 'student_form':StudentForm, 'code':code,
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

    def get_context_data(self, **kwargs):
        context = super(StudentUpdate, self).get_context_data(**kwargs)

        pk = get_path_id(self.request.path.split('/'))

        context['studentId'] = pk
        return context
    
    def get_success_url(self):
        return self.request.META['HTTP_REFERER']

class ContactUpdate(UpdateView):
    model = Contact
    success_url = '/crm/1'

    def get_context_data(self, **kwargs):
        context = super(ContactUpdate, self).get_context_data(**kwargs)

        pk = get_path_id(self.request.path.split('/'))

        context['contactId'] = pk 
        return context

    def get_success_url(self):
        return self.request.META['HTTP_REFERER']

class RelationshipUpdate(UpdateView):
    model = Relationship
    success_url = '/crm/1'
    
    def get_context_data(self, **kwargs):
        context = super(RelationshipUpdate, self).get_context_data(**kwargs)

        pk = get_path_id(self.request.path.split('/'))

        context['relId'] = pk
        return context

    def get_success_url(self):
        return self.request.META['HTTP_REFERER']

class Search(ListView):
    model = Student
    template_name = 'crm/search_list.html'

    #def get(self, request, *args, **kwargs):
    #    pass
    def get_queryset(self):
        request = self.request
        kwargs = {}
        for key in request.GET.keys():
            if request.GET.get(key) is not u'':
                kwargs[key] = request.GET.get(key)
        return  Student.objects.filter(**kwargs)

class Scanner(View):
    template_name = 'crm/scanner.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        code = request.POST.get('code', '')
        atype = request.POST.get('atype','A')
        try: 
            student_code = Barcode.objects.get(code=code)
        except ObjectDoesNotExist:
            student_code = None

        # has the student been scanned in the last hour?
        attendance = Attendance.objects.filter(student=student_code.student,
                attendance_date=date.today(), attendance_type=atype)
        if attendance:
            old_time = time(attendance.attendance_time)
            adjusted_time = time(old_time.hour + 1, old_time.minute,
                    old_time.second, old_time.microsecond)
            new_time = datetime.datetime.now().time()
            
            if new_time < adjusted_time:
                status = 'Already scanned.'
                context = {"atype":atype, "status":status}
                return render(request, self.template_name, context)

        # save the latest attendance
        attendance = Attendance(student=student_code.student,
                attendance_date=date.today(), attendance_type=atype)

        attendance.save()
        status = attendance.student + ' added.'
        context = {"code":code, "student_code":student_code, 'status':status}
        return render(request, self.template_name, context)

