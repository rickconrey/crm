from django import forms
from crm.models import Student, StatusStudent, Group
from crm.models import GroupCategory

# Define forms for searching
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'gender',
                'anniv_month', 'rank', 'total_years', 
                'uniform_size', 'belt_size', 'start_date',
                'dob', 'class_time')

class StatusForm(forms.ModelForm):
    class Meta:
        model = StatusStudent
        fields = ('status', )

# Groups
def get_choices(category):
    group_category = GroupCategory.objects.filter(
            group_category=category)
    groups = Group.objects.filter(group_category=group_category)
    group_choices = [group.group for group in groups]
    group_ids = [group.id for group in groups]
    zipped = zip(group_ids,group_choices)
    zipped.insert(0, ('','---------'))
    return tuple(zipped) 

class GroupForm(forms.Form):
    def __init__(self, *args, **kwargs):
        field = kwargs.pop('field', None)
        label = kwargs.pop('label', None)
        title = kwargs.pop('title', None)
        super(GroupForm, self).__init__(*args, **kwargs)
        self.fields[field] = forms.ChoiceField(label=label,
                choices=get_choices(title))

class BBCGroupForm(GroupForm):
    def __init__(self, *args, **kwargs):
        keywords = {'field':'bbc_group', 'label':'BBC Group',
            'title':'Black Belt Club'}
        super(BBCGroupForm, self).__init__(*args, **keywords)

class MCGroupForm(GroupForm):
    def __init__(self, *args, **kwargs):
        keywords = {'field':'mc_group', 'label':'MC Group',
                'title':'Master\'s Club'}
        super(MCGroupForm, self).__init__(*args, **keywords)

class InstructorGroupForm(GroupForm):
    def __init__(self, *args, **kwargs):
        keywords = {'field':'instructor_group', 'label':'Instructor Group',
                'title':'Instructors'}
        super(InstructorGroupForm, self).__init__(*args, **keywords)

class LeadershipGroupForm(GroupForm):
    def __init__(self, *args, **kwargs):
        keywords = {'field':'leadership_group', 'label':'Leadership Group',
                'title':'Leadership'}
        super(LeadershipGroupForm, self).__init__(*args, **keywords)

class AAUGroupForm(GroupForm):
    def __init__(self, *args, **kwargs):
        keywords = {'field':'aau_group', 'label':'AAU Group',
                'title':'AAU'}
        super(AAUGroupForm, self).__init__(*args, **keywords)

