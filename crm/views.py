from django.http import HttpResponse, Http404
from django.shortcuts import render
from crm.models import Student, Contact, Relationship

def view_student(request, student_id):
    try:
        student = Student.objects.get(pk=student_id)
        age = student.get_age()
        classification = student.get_classification()
    except Student.DoesNotExist:
        raise Http404
    return render(request, 'crm/view.html', {'student':student,
                                             'age':age,
                                             'classification':classification,
                                             })
