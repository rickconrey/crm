from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.edit import UpdateView, ModelFormMixin
from django.views.generic import ListView, View
from django.forms.models import modelform_factory, modelformset_factory
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from crm.models import Student, Contact, Relationship
from crm.models import ContactEmail, ContactPhone
from crm.models import StudentEmail, StudentPhone
from crm.models import StatusStudent, Attendance
from crm.models import Test, TestScore, Tip, TippingGroup
from crm.models import TippingStudent, Barcode
from crm.forms import StudentForm, StatusForm, BBCGroupForm
from crm.forms import MCGroupForm, InstructorGroupForm, LeadershipGroupForm
from crm.forms import AAUGroupForm, BasicSearchForm
from datetime import date, time, datetime

# utilities

# get path
def get_path_id(path_list):
    for item in path_list:
        if item.isdigit():
            return item

def get_search_form():
    search_form = []
    search_form.append({'student':StudentForm(prefix="student"),
        'status':StatusForm(prefix="status")})
    search_form.append({'bbc':BBCGroupForm(prefix="BBC"),
        'mc':MCGroupForm(prefix="MC"),
        'instructor':InstructorGroupForm(prefix="Instructor"),
        'leadership':LeadershipGroupForm(prefix="Leadership"),
        'aau':AAUGroupForm(prefix="AAU"),})

    return search_form


def render_view(request, template, context):
    search_form = {}
    search_form['basic_search'] = BasicSearchForm()
    context['search_form'] = search_form
    return render(request, template, context)


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

    return render_view(request, 'crm/view.html', results)


def scanner(request):
    return render_view(request, 'crm/scanner.html',)

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
        #search_form = {}
        #search_form['basic_search'] = BasicSearchForm()

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
                    'groups':groups, 'code':code,
                    }

    return student_info

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
    #template_name = 'crm/search_list.html'
    template_name = 'crm/search_adv.html'

    def get_queryset(self):
        request = self.request
        kwargs = {}
        for key in request.GET.keys():
            if request.GET.get(key) is not u'':
                kwargs[key] = request.GET.get(key)
        return  Student.objects.filter(**kwargs)

    def get(self, request, *args, **kwargs):
        last_name = u''
        if request.GET.get('last_name'):
            last_name = request.GET.get('last_name')
        if last_name is not u'':
            results = Student.objects.filter(last_name__istartswith=last_name)
            context = {'results':results}
            return render_view(request, 'crm/search_list.html',context)

        context = {"adv_search_form":get_search_form()}

        return render_view(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        student = StudentForm(request.POST, prefix='student')
        student.is_valid()
        status = StatusForm(request.POST, prefix='status')
        status.is_valid()
        groups = []
        groups.append(BBCGroupForm(request.POST, prefix='BBC'))
        groups.append(AAUGroupForm(request.POST, prefix='AAU'))
        groups.append(MCGroupForm(request.POST, prefix='MC'))
        groups.append(LeadershipGroupForm(request.POST, prefix='Leadership'))
        groups.append(InstructorGroupForm(request.POST, prefix='Instructor'))

        # validate group data
        valid_groups = []
        for group in groups:
            group.is_valid()
            if group.cleaned_data:
                valid_groups.append(group.cleaned_data)

        # find students based on fields
        data = student.cleaned_data
        lst = []
        for key in data:
            if data[key] == '' or data[key] is None:
                lst.append(key)

        for l in lst:
            data.pop(l)

        fname = data.pop('first_name', '')
        lname = data.pop('last_name', '')

        students = Student.objects.filter(
                first_name__istartswith=fname).filter(
                        last_name__istartswith=lname).filter(**data)

        # select only those students that are in searched for groups
        remove = []
        for group in valid_groups:
            for key in group.keys():
                for s in students:
                    student_groups = s.get_groups()
                    if key in student_groups.keys():
                        if int(group[key]) == student_groups[
                                key][0].group.id:
                            continue
                    if s not in remove:
                        remove.append(s)

        # check status
        if status.cleaned_data:
            for s in students:
                student_status = s.get_current_status()
                if student_status and str(
                        student_status.status) == str(
                                status.cleaned_data['status'].status):
                    continue
                if s not in remove:
                    remove.append(s)

        results = list(students)
        for item in remove:
            results.remove(item)

        context = {'results':results}

        return render_view(request, 'crm/search_list.html', context)


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
                attendance_date=date.today(), attendance_type=atype).order_by(
                        '-attendance_date')
        if attendance:
            old_time = attendance[0].attendance_time
            adjusted_time = time(old_time.hour + 1, old_time.minute,
                    old_time.second, old_time.microsecond)
            new_time = datetime.now().time()
            
            if new_time < adjusted_time:
                messages.info(request, 'Already scanned.')
                context = {"atype":atype}
                return render_view(request, self.template_name, context)

        # save the latest attendance
        attendance = Attendance(student=student_code.student,
                attendance_date=date.today(), attendance_type=atype)

        attendance.save()
        messages.success(request, attendance.student.first_name + ' added.')
        context = {"code":code, "student_code":student_code}
        return render_view(request, self.template_name, context)

