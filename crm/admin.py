from django.contrib import admin
from crm.models import Student, Group, Contact, Rank, AAURank, Relationship
from crm.models import ContactPhone, ContactEmail, StudentPhone, StudentEmail
from crm.models import HoldHarmless, HoldHarmlessStudent, Session
from crm.models import SessionMember, SessionAttendance, BBCGroup, MCGroup
from crm.models import AAUGroup, InstructorGroup, LeadershipGroup, TestGroup
from crm.models import TestScore, Test, RTGroup, TippingGroup, TippingStudent
from crm.models import Tip, Attendance, PresidentialRequirements, Fitness
from crm.models import Tuition, StatusStudent, GroupCategory

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
    model = Relationship
    extra = 1

class SessionMemberInline(admin.TabularInline):
    model = SessionMember
    extra = 1

class TuitionInline(admin.TabularInline):
    model = Tuition
    extra = 1

class AttendanceInline(admin.TabularInline):
    model = Attendance
    extra = 1

class HoldHarmlessInline(admin.TabularInline):
    model = HoldHarmlessStudent
    extra = 1

class FitnessInline(admin.TabularInline):
    model = Fitness
    extra = 1

class SessionAttendanceInline(admin.TabularInline):
    model = SessionAttendance
    extra = 1

class StatusStudentInline(admin.TabularInline):
    model = StatusStudent
    extra = 1
class GroupInline(admin.TabularInline):
    model = Group
    extra = 1

class StudentAdmin(admin.ModelAdmin):
    inlines = [StatusStudentInline,
               StudentEmailInline,
               StudentPhoneInline,
               RelationshipInline,
               TestInline,TippingInline,
               SessionMemberInline,
               #TuitionInline,
               AttendanceInline,
               HoldHarmlessInline,
               FitnessInline
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

class HoldHarmlessAdmin(admin.ModelAdmin):
    inlines = [HoldHarmlessInline]

class SessionAttendanceAdmin(admin.ModelAdmin):
    inlines = [SessionAttendanceInline]
#class RelationshipAdmin(admin.ModelAdmin):
#    inlines = [StudentInline, ContactInline]

class GroupAdmin(admin.ModelAdmin):
    inlines = [GroupInline]

class BBCAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        idx_group_category = GroupCategory.objects.filter(
                        group_category='Black Belt Club')
        if db_field.name == 'group':
            kwargs['queryset'] = Group.objects.filter(
                        group_category=idx_group_category)
        if db_field.name == 'group_category':
            kwargs['queryset'] = idx_group_category

        return super(BBCAdmin, self).formfield_for_foreignkey(db_field,
                                                              request,
                                                              **kwargs)

class InstructorsAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        idx_group_category = GroupCategory.objects.filter(
                        group_category='Instructors')
        if db_field.name == 'group':
            kwargs['queryset'] = Group.objects.filter(
                        group_category=idx_group_category)
        if db_field.name == 'group_category':
            kwargs['queryset'] = idx_group_category

        return super(InstructorsAdmin, self).formfield_for_foreignkey(db_field,
                                                                      request,
                                                                      **kwargs)

class LeadershipAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        idx_group_category = GroupCategory.objects.filter(
                        group_category='Leadership')
        if db_field.name == 'group':
            kwargs['queryset'] = Group.objects.filter(
                        group_category=idx_group_category)
        if db_field.name == 'group_category':
            kwargs['queryset'] = idx_group_category

        return super(LeadershipAdmin, self).formfield_for_foreignkey(db_field,
                                                                     request,
                                                                     **kwargs)

class MCAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        idx_group_category = GroupCategory.objects.filter(
                        group_category='Master\'s Club')
        if db_field.name == 'group':
            kwargs['queryset'] = Group.objects.filter(
                        group_category=idx_group_category)
        if db_field.name == 'group_category':
            kwargs['queryset'] = idx_group_category

        return super(MCAdmin, self).formfield_for_foreignkey(db_field,
                                                             request,
                                                             **kwargs)



#admin.site.register(Relationship, RelationshipAdmin)
admin.site.register(GroupCategory, GroupAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Contact, ContactAdmin)        
admin.site.register(TestGroup, TestGroupAdmin)
admin.site.register(Test, TestAdmin)
admin.site.register(TippingGroup, TippingAdmin)
admin.site.register(Session, SessionAdmin)
admin.site.register(InstructorGroup, InstructorsAdmin)
admin.site.register(TippingStudent, TippingStudentAdmin)
admin.site.register(RTGroup)
admin.site.register(BBCGroup, BBCAdmin)
admin.site.register(MCGroup, MCAdmin)
admin.site.register(HoldHarmless, HoldHarmlessAdmin)
admin.site.register(PresidentialRequirements)
admin.site.register(SessionMember, SessionAttendanceAdmin)
admin.site.register(AAUGroup)
admin.site.register(LeadershipGroup, LeadershipAdmin)
