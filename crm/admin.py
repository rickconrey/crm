from django.contrib import admin
from crm.models import Student, Group, Contact, Rank, AAURank, Relationship
from crm.models import ContactPhone, ContactEmail, StudentPhone, StudentEmail
from crm.models import HoldHarmless, HoldHarmlessStudent, Session
from crm.models import SessionMember, SessionAttendance, BBCGroup, MCGroup
from crm.models import AAUGroup, InstructorGroup, LeadershipGroup, TestGroup
from crm.models import TestScore, Test, RTGroup, TippingGroup, TippingStudent
from crm.models import Tip, Attendance, PresidentialRequirements, Fitness
from crm.models import Tuition

class ContactInline(admin.StackedInline):
    model = Contact
    extra = 1

class ContactEmailInline(admin.TabularInline):
    model = ContactEmail
    extra = 1

class ContactPhoneInline(admin.TabularInline):
    model = ContactPhone
    extra = 1

class StudentEmailInline(admin.TabularInline):
    model = StudentEmail
    extra = 1

class StudentPhoneInline(admin.TabularInline):
    model = StudentPhone
    extra = 1

class TestInline(admin.TabularInline):
    model = Test
    extra = 1

class TestScoreInline(admin.TabularInline):
    model = TestScore
    extra = 1

class TippingInline(admin.TabularInline):
    model = TippingStudent
    extra = 1

class TipInline(admin.TabularInline):
    model = Tip
    extra = 1

class RelationshipInline(admin.TabularInline):
    model = Student.contacts.through
    extra = 1

class SessionMemberInline(admin.TabularInline):
    model = SessionMember
    extra = 1

class StudentAdmin(admin.ModelAdmin):
    inlines = [StudentEmailInline,
               StudentPhoneInline,
               RelationshipInline,
               TestInline,TippingInline,
               SessionMemberInline,
               ]



class ContactAdmin(admin.ModelAdmin):
    inlines = [ContactEmailInline,
            ContactPhoneInline,
            ]


class TestGroupAdmin(admin.ModelAdmin):
    inlines = [TestInline]

class TestAdmin(admin.ModelAdmin):
    inlines = [TestScoreInline]

class TippingAdmin(admin.ModelAdmin):
    inlines = [TippingInline]

class SessionAdmin(admin.ModelAdmin):
    inlines = [SessionMemberInline]

class TippingStudentAdmin(admin.ModelAdmin):
    inlines = [TipInline]
#class RelationshipAdmin(admin.ModelAdmin):
#    inlines = [StudentInline, ContactInline]

#admin.site.register(Relationship, RelationshipAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Contact, ContactAdmin)        
admin.site.register(TestGroup, TestGroupAdmin)
admin.site.register(Test, TestAdmin)
admin.site.register(TippingGroup, TippingAdmin)
admin.site.register(Session, SessionAdmin)
admin.site.register(InstructorGroup)
admin.site.register(TippingStudent, TippingStudentAdmin)
