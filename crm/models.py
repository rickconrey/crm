from django.db import models
from datetime import date
import barcode, os

#PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
PROJECT_PATH = os.getcwd()
STATIC_ROOT = os.path.join(PROJECT_PATH, 'uama/static')

# Student and Contact info
class CommonInfo(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address1 = models.CharField(max_length=100, blank=True)
    address2 = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=100, default="Morgan Hill",
                            blank=True)
    state = models.CharField(max_length=50, default="California", 
                             blank=True)
    zipcode = models.IntegerField(default=95037,
                                  blank=True, null=True)

    class Meta:
        abstract = True

class Student(CommonInfo):
    GENDER_CHOICES = (
        ('F', 'Female'),
        ('M', 'Male'),
    )
    SIZE_CHOICES = (
        ('000', '000'),
        ('00', '00'),
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
    )
    ANNIV_MONTH_CHOICES = (
        (1, 'January'),
        (2, 'February'),
        (3, 'March'),
        (4, 'April'),
        (5, 'May'),
        (6, 'June'),
        (7, 'July'),
        (8, 'August'),
        (9, 'September'),
        (10, 'October'),
        (11, 'November'),
        (12, 'December'),
    )
    dob = models.DateField('Date of Birth')                                   #
    start_date = models.DateField('Start Date')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,
                              blank=True, null=True)
    uniform_size = models.CharField(max_length=3, choices=SIZE_CHOICES,
                                    blank=True)
    belt_size = models.CharField(max_length=3, choices=SIZE_CHOICES,
                                 blank=True)
    #status = models.ForeignKey('Status', default='INT')
    class_time = models.ForeignKey('Class', null=True, blank=True)
    # group = models.ManyToManyField(Group, through='') # change?
    #contacts = models.ManyToManyField('Contact', through='Relationship',
    #                                  null=True)
    rank = models.ForeignKey('Rank', to_field='rank', 
                             null=True, blank=True,
                             verbose_name="Current Rank")
    anniv_month = models.IntegerField(choices=ANNIV_MONTH_CHOICES,
                                      blank=True)
    benefits = models.TextField(blank=True)
    limitations = models.TextField(blank=True)
    referral = models.ForeignKey('Student', blank=True, null=True)
    # hold_harmless = models.BooleanField(default=False)
    total_years = models.IntegerField(blank=True, null=True)
    
    def get_age(self):
        today = date.today()
        try:
            birthday = self.dob.replace(year=today.year)
        except ValueError: #raised when bday is Feb 29 and it's not leapyear
            birthday = birthday.replace(year.today.year, day=birthday.day-1)
        if birthday > today:
            return today.year - self.dob.year - 1
        else:
            return today.year - self.dob.year

    def get_classification(self):
        ''' Return if student is Super Jr, Jr, or Sr '''
        age = self.get_age()
        if age < 7:
            return "Super Jr"
        elif age > 6 and age < 14:
            return "Jr"
        else:
            return "Sr"
    
    def get_current_status(self):
        # Return the current status of the student
        status = StatusStudent.objects.filter(student=self).order_by(
                    '-start_date')
        if status.exists():
            return status[0]

        return None

    def get_last_test_date(self):
        #from test, filter by student, find the closest date to today
        today = date.today()
        last_test = Test.objects.filter(student=self,
                                        test_group__test_date__lte=today)
        if last_test.exists():
            return last_test[0]
        return None

    def get_next_test_date(self):
        # find last test date, add on amount of time for age/belt
        pass

    def add_next_tipping(self):
        # Check to see if there is a next tipping date, add if DNE
        # return the added date or next date if already exists
        next_tipping_date = self.get_next_tipping()

        # next tipping date already exists, return with it
        if next_tipping_date:
            return next_tipping_date

        # base variables
        age = self.get_age()
        rank = Rank.objects.get(rank=self.rank)
        today = date.today()
        month = today.month
        year = today.year
        last_test_date = self.get_last_test_date()
    
        # there was a previous test, base calculation on that date
        if last_test_date:
            ltd = last_test_date.test_date()
            month = ltd.month
            year = ltd.year

        # rules to find next tip group
        if age < 6:
            tip_month = month + 3
        elif age == 6:
            tip_month = month + 2
        elif age == 7:
            tip_month = month + 3
        elif age >= 8:
            tip_month = month + 2
        tip_year = year

        # if the tip_month exceeds 12 increase the year
        if tip_month > 12:
            tip_month -= 12
            tip_year += 1

        # create next tipping
        next_rank = Rank.objects.get(id=(rank.id+1))
        tip_date = date(tip_year,tip_month,1)
        tip_date_str = tip_date.strftime('%B') + ' ' + str(tip_date.year)
        tipping_group = TippingGroup.objects.get(description=tip_date_str)
        ts = TippingStudent(student=self,tipping_group=tipping_group,
                            rank=next_rank)
        ts.save()

        return ts

    def update_total_years(self):
        # if status is active and anniv_month is current month, add a year
        # create list for year patches
        pass

    def check_tips(self):
        # check to see if there are enough tips to test
        # return True or False
        return False

    def get_next_tipping(self):
        # find when the student is tipping next
        # return TippingStudent object or None
        today = date.today()
        next_tipping = TippingStudent.objects.filter(
                                student=self,
                                tipping_group__date__gte=today)
        if next_tipping.exists():
            return next_tipping[0]
        return None

    def is_in_testing_group(self, date):
        pass
        

    def get_days_since_last_test(self):
        last_test_date = self.get_last_test_date()
        attendance = Attendance.objects.filter(student=self
            ).filter(
              attendance_date__gt=last_test_date
            )
        return attendance.count()

    # Groups
    def get_BBC(self):
        return BBCGroup.objects.filter(student=self)

    def get_MC(self):
        return MCGroup.objects.filter(student=self)

    def get_AAU(self):
        return AAUGroup.objects.filter(student=self)

    def get_instructor(self):
        return InstructorGroup.objects.filter(student=self)

    def get_leadership(self):
        return LeadershipGroup.objects.filter(student=self)

    def get_groups(self):
        BBC = self.get_BBC()
        MC = self.get_MC()
        AAU = self.get_AAU()
        Instructor = self.get_instructor()
        Leadership = self.get_leadership()

        groups = {}
        if BBC.exists():
            groups['BBC'] = BBC
        if MC.exists():
            groups['MC'] = MC
        if AAU.exists():
            groups['AAU'] = AAU
        if Instructor.exists():
            groups['Instructor'] = Instructor
        if Leadership.exists():
            groups['Leadership'] = Leadership
        return groups

    def generate_barcode(self, card_type):
        codes = Barcode.objects.filter(student=self)
        for code in codes:
            if code.card_type == card_type:
                return code.code

        # prefix to tell which type of card we are creating
        prefix = {1:'R',2:'C',3:'S',4:'L',5:'A'}

        bcode_string = prefix[card_type] + \
                self.first_name[:10] + self.last_name[:10] + \
                "%05d" % self.id
        bcode = barcode.get('code39',bcode_string)
        filename = bcode.save(bcode.get_fullcode())

        code = Barcode(student=self,code=bcode.get_fullcode(),
            code_loc=filename)
        code.save()

        # move image to correct directory
        loc = 'img/barcodes/' + filename
        dst = os.path.join(STATIC_ROOT, loc)
        os.rename(filename,dst)

        return code.code

    #def save(self):

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name

class Contact(CommonInfo):
    def __unicode__(self):
        return self.first_name + ' ' + self.last_name

class Relationship(models.Model):
    MOTHER = 'M'
    FATHER = 'F'
    EMERGENCY = 'E'
    OTHER = 'O'
    RELATIONSHIP_CHIOCES = (
        (MOTHER, 'Mother'),
        (FATHER, 'Father'),
        (EMERGENCY, 'Emergency'),
        (OTHER, 'Other'),
    )
    student = models.ForeignKey(Student)
    contact = models.ForeignKey(Contact)
    relationship = models.CharField(max_length=1, 
                                    choices=RELATIONSHIP_CHIOCES,
                                    default=OTHER)

    def __unicode__(self):
        return self.relationship + ' - ' + self.student.first_name + ' ' + \
                self.student.last_name

# Email models #
class Email(models.Model):
    PRIMARY = 'P'
    HOME = 'H'
    WORK = 'W'
    OTHER = 'O'
    EMAIL_TYPE_CHIOCES = (
        (PRIMARY, 'Primary'),
        (HOME, 'Home'),
        (WORK, 'Work'),
        (OTHER, 'Other'),
    )
    email = models.EmailField(max_length=254)
    #email_type = models.CharField(max_length=1, 
    #                              choices=EMAIL_TYPE_CHIOCES, 
    #                              default=PRIMARY)

    class Meta:
        abstract = True

class StudentEmail(Email):
    student = models.ForeignKey(Student)

    def __unicode__(self):
        return self.student.first_name + ' ' + self.student.last_name + \
                ' - ' + self.email

class ContactEmail(Email):
    contact = models.ForeignKey(Contact)

    def __unicode__(self):
        return self.contact.first_name + ' ' + self.contact.last_name + \
                ' - ' + self.email

# Phone models #
class Phone(models.Model):
    PRIMARY = 'P'
    HOME = 'H'
    WORK = 'W'
    CELL = 'C'
    OTHER = 'O'
    PHONE_TYPE_CHOICES = (
        (PRIMARY, 'Primary'),
        (HOME, 'Home'),
        (WORK, 'Work'),
        (CELL, 'Cell'),
        (OTHER, 'Other'),
    )
    phone = models.CharField(max_length=14)
    phone_type = models.CharField(max_length=1, 
                                  choices=PHONE_TYPE_CHOICES, 
                                  default=CELL)

    class Meta:
        abstract = True

class StudentPhone(Phone):
    student = models.ForeignKey(Student)

    def __unicode__(self):
        return self.student.first_name + ' ' + self.student.last_name + \
                ' - ' + self.phone + ' ' + self.phone_type

class ContactPhone(Phone):
    contact = models.ForeignKey(Contact)

    def __unicode__(self):
        return self.contact.first_name + ' ' + self.contact.last_name + \
                ' - ' + self.phone + ' ' + self.phone_type

# Hold Harmless #
# sparring, ground fighting, and any future
class HoldHarmless(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = "Hold Harmless"

    def __unicode__(self):
        return self.name
    
class HoldHarmlessStudent(models.Model):
    hold_harmless = models.ForeignKey(HoldHarmless)
    student = models.ForeignKey(Student)
    date = models.DateField(default=date.today())

# Barcode $
# Barcodes to make cards for regular class, SWAT/STORM, candidate, etc
class Barcode(models.Model):
    CARD_TYPE_CHOICES = (
            (1,'Class'),
            (2,'Candidate'),
            (3,'SWAT'),
            (4,'Leadership'),
            (5,'AAU'),
            )
    student = models.ForeignKey(Student)
    code = models.CharField(max_length=100,null=True, blank=True)
    code_loc = models.CharField(max_length=100,null=True, blank=True)
    card_type = models.IntegerField(choices=CARD_TYPE_CHOICES, default=1)

    def __unicode__(self):
        return self.code

# Sessions/Seminar #
# Fitness, Bo, Ground, Sparring, CPR, leadership, demo, etc
class Session(models.Model):
    session_name = models.CharField(max_length=300, unique=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    rate = models.DecimalField(max_digits=8, decimal_places=2,
                               null=True, blank=True)
   
    def __unicode__(self):
        return self.session_name

class SessionMember(models.Model):
    session = models.ForeignKey(Session)
    student = models.ForeignKey(Student)
    receive_email = models.BooleanField(default=True)
    paid = models.BooleanField(default=False)

    def __unicode__(self):
        return self.session.session_name + ' - ' + self.student.first_name + \
                ' ' + self.student.last_name

class SessionAttendance(models.Model):
    session_member = models.ForeignKey(SessionMember)
    date = models.DateField(default=date.today())

    def __unicode__(self):
        return self.session_member.session.session_name + ' - ' + \
                self.session_member.student.first_name + ' ' + \
                self.session_member.student.last_name + ' - ' + \
                self.date.strftime('%B %d, %Y')

# Group #
class GroupCategory(models.Model):
    group_category = models.CharField(max_length=100,
                                      unique=True)

    def __unicode__(self):
        return self.group_category

    class Meta:
        verbose_name = "Group Category"
        verbose_name_plural = "Group Categories"
class Group(models.Model):
    GROUP_CHOICES = (
        ('STF', 'Staff'),
        ('BBC', 'Black Belt Club'),
        ('MSC', 'Master\'s Club'),
        ('INS', 'Instructor'),
        ('LDS', 'Leadership'),
        ('AAU', 'AAU'),
    )
    group = models.CharField(max_length=100)
    group_category = models.ForeignKey(GroupCategory)

    def __unicode__(self):
        return self.group

class GroupJoin(models.Model):
    group_category = models.ForeignKey(GroupCategory)
    group = models.ForeignKey(Group)
    student = models.ForeignKey(Student)
    join_date = models.DateField(default=date.today())
    receive_email = models.BooleanField(default=True)

    class Meta:
        abstract = True

class BBCGroup(GroupJoin):
    goals = models.TextField(blank=True)
    #black_belt_group = models.DateField()
    rate = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = "BBC Group"
        verbose_name_plural = "BBC Groups"

class MCGroup(GroupJoin):
    goals = models.TextField(blank=True)
    #advanced_degree_group = models.DateField()
    rate = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = "MC Group"
        verbose_name_plural = "MC Groups"

class AAUGroup(GroupJoin):
    aau_rank = models.ForeignKey('AAURank')
    #aau_group = models.DateField()

    class Meta:
        verbose_name = "AAU Group"
        verbose_name_plural = "AAU Groups"

class InstructorGroup(GroupJoin):
    INSTRUCTOR_RANK_CHOICES = (
        ('CGN','ChoGyoNim'),
        ('BSBN', 'BuSaBumNim'),
        ('SBN', 'SaBumNim'),
        ('BKJN', 'BuKwanJangNim'),
        ('KJN', 'KwanJangNim'),
    )
    #instructor_rank = models.CharField(max_length=4,
    #                                   choices=INSTRUCTOR_RANK_CHOICES,
    #                                   default='CGN')
    def __unicode__(self):
        return self.student.first_name \
                + ' ' + self.student.last_name

class LeadershipGroup(GroupJoin):
    LEADERSHIP_LEVEL_CHOICES = (
        ('1', 'Leadership 1'),
        ('2', 'Leadership 2'),
        ('3', 'Leadership 3'),
        ('G', 'Graduate'),
    )

    #leadership_level = models.CharField(max_length=1,
    #                                    choices=LEADERSHIP_LEVEL_CHOICES,
    #                                    default='1')
    def __unicode__(self):
        return self.student.first_name \
                + ' ' + self.student.last_name

# Status #
class Status(models.Model):
    STATUS_CHOICES = (
        ('INT', 'Intro'),
        ('SUM', 'Summer'),
        ('ACT', 'Active'),
        ('OHO', 'On Hold'),
        ('IHO', 'Indef Hold'),
        ('IAC', 'Inactive'),
        ('STF', 'Staff'),
        ('ARC', 'Archived'),
    )
    #status = models.CharField(max_length=3, 
    #                          choices=STATUS_CHOICES, 
    #                          default='ACT',
    #                          unique=True)
    status = models.CharField(max_length=20,
                              unique=True)

    def __unicode__(self):
        return self.status

    class Meta:
        verbose_name_plural = 'Status'

class StatusStudent(models.Model):
    student = models.ForeignKey(Student)
    status = models.ForeignKey(Status)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    rate = models.DecimalField(max_digits=8, decimal_places=2,
                               null=True, blank=True)
    def __unicode__(self):
        return self.status.status

    class Meta:
        verbose_name_plural = "Student Status"
    

# is this part of status? 
#class SpecialProgram(models.Model):
#    student = models.ForeignKey(Student)
#    start_date = models.DateField()
#    end_date = models.DateField(null=True, blank=True)
#    rate = models.DecimalField(max_digits=8, decimal_places=2,
#                               null=True, blank=True)
#    program_name = models.CharField(max_length=50)

# Class #
class Class(models.Model):
    CLASS_TIME_CHOICES = (
        ('SJ3T', 'SupJr 3:30 T/Th'),
        ('SJ5M', 'SupJr 5:45 M/W'),
        ('SJ5T', 'SupJr 5:45 T/Th'),
        ('BJ4T', 'BegJr 4:15 T/Th'),
        ('BJ6M', 'BegJr 6:30 M/W'),
        ('BJ6T', 'BegJr 6:30 T/Th'),
        ('IJ4M', 'IntJr 4:15 M/W'),
        ('IJ5T', 'IntJr 5:45 T/Th'),
        ('IJ7T', 'IntJr 7:15 T/Th'),
        ('AJ4M', 'AdvJr 4:15 M/W'),
        ('AJ5T', 'AdvJr 5:00 T/Th'),
        ('AJ5M', 'AdvJr 5:45 M/W'),
        ('BBJM', 'BBJr 5:00 M/W'),
        ('BBJT', 'BBJr 5:00 T/Th'),
        ('BS7T', 'BegSr 7:15 T/Th'),
        ('IS7T', 'IntSr 7:15 T/Th'),
        ('AS7T', 'AdvSr 7:15 T/Th'),
        ('BBSM', 'BBSr 8:00 M/W'),
        ('BBST', 'BBSr 8:00 T/Th'),
    )
    #class_time = models.CharField(max_length=4, choices=CLASS_TIME_CHOICES,
    #                              unique=True)
    class_time = models.CharField(max_length=50,
                                  unique=True)

    def __unicode__(self):
        return self.class_time

# Rank #
class Rank(models.Model):
    RANK_CHOICES = (
        ('SJWB','Super Jr White Belt'),
        ('SJWS','Super Jr White Stripe'),
        ('WOB','White Orange Belt'),
        ('WOS','White Orange Stripe'),
        ('OB','Orange Belt'),
        ('OS','Orange Stripe'),
        ('OGB','Orange Gold Belt'),
        ('OGS','Orange Gold Stripe'),
        ('JOS','Jr Orange Stripe'),
        ('WB','White Belt'),
        ('WS','White Stripe'),
        ('GB','Gold Belt'),
        ('GS','Gold Stripe'),
        ('EB','Green Belt'),
        ('ES','Green Stripe'),
        ('PB','Purple Belt'),
        ('PS','Purple Stripe'),
        ('BB','Blue Belt'),
        ('BS','Blue Stripe'),
        ('RB','Red Belt'),
        ('RS','Red Stripe'),
        ('R2','Red II'),
        ('R3','Red III'),
        ('LB','Pluma Belt'),
        ('LS','Pluma Stripe'),
        ('L2','Pluma II'),
        ('J1D','Jr 1st Degree'),
        ('J1D1S','Jr 1st Degree, 1st Step'),
        ('J1D2S','Jr 1st Degree, 2nd Step'),
        ('J1D3S','Jr 1st Degree, 3rd Step'),
        ('J1D4S','Jr 1st Degree, 4th Step'),
        ('J1D5S','Jr 1st Degree, 5th Step'),
        ('J2DS1D','Jr 2nd Degree, Sr 1st Degree'),
        ('J2DS1D1S','Jr 2nd Degree, Sr 1st Degree, 1st Step Trans'),
        ('J2DS1D2S','Jr 2nd Degree, Sr 1st Degree, 2nd Step Trans'),
        ('S1D','Sr 1st Degree'),
        ('S1D1S','Sr 1st Degree, 1st Step'),
        ('S1D2S','Sr 1st Degree, 2nd Step'),
        ('S1D3S','Sr 1st Degree, 3rd Step'),
        ('S2D','Sr 2nd Degree'),
        ('S2D1S','Sr 2nd Degree, 1st Step'),
        ('S2D2S','Sr 2nd Degree, 2nd Step'),
        ('S2D3S','Sr 2nd Degree, 3rd Step'),
        ('S2D4S','Sr 2nd Degree, 4th Step'),
        ('S2D5S','Sr 2nd Degree, 5th Step'),
        ('S3D','Sr 3rd Degree'),
        ('S3D1S','Sr 3rd Degree, 1st Step'),
        ('S3D2S','Sr 3rd Degree, 2nd Step'),
        ('S3D3S','Sr 3rd Degree, 3rd Step'),
        ('S3D4S','Sr 3rd Degree, 4th Step'),
        ('S3D5S','Sr 3rd Degree, 5th Step'),
        ('S3D6S','Sr 3rd Degree, 6th Step'),
        ('S3D7S','Sr 3rd Degree, 7th Step'),
        ('S4D','Sr 4th Degree'),

    )
    #rank = models.CharField(max_length=8, choices=RANK_CHOICES,
    #                        default='WB', unique=True)
    rank = models.CharField(max_length=60, unique=True)

    def get_next_rank(self):
        pass

    def __unicode__(self):
        return self.rank

class AAURank(models.Model):
    AAU_RANK_CHOICES = (
        ('A0S','AAU 0th Step'),
        ('A1S','AAU 1st Step'),
        ('A2S','AAU 2nd Step'),
        ('A1D','AAU 1st Dan'),
        ('A1D1S','AAU 1st Dan, 1st Step'),
        ('A2D','AAU 2nd Dan'),
        ('A2D1S','AAU 2nd Dan, 1st Step'),
        ('A2D2S','AAU 2nd Dan, 2nd Step'),
        ('A2D3S','AAU 2nd Dan, 3rd Step'),
        ('A3D','AAU 3rd Dan'),
        ('A4D','AAU 4th Dan'),
        ('A5D','AAU 5th Dan'),
        ('A6D','AAU 6th Dan'),
        ('A7D','AAU 7th Dan'),
    )
    #aau_rank = models.CharField(max_length=5, choices=AAU_RANK_CHOICES,
    #                            default='AOS', unique=True)
    aau_rank = models.CharField(max_length=60, unique=True)

    def __unicode__(self):
        return self.aau_rank

# Tip and Test
class TestGroup(models.Model):
    TEST_TYPE = (
        ('M','Monthly'),
        ('B','Black Belt Test'),
        ('S','Step Test'),
        ('K','MakeUp Test'),
        ('O','Other'),
    )
    description = models.CharField(max_length=200, unique=True)
    test_type = models.CharField(max_length=1, choices=TEST_TYPE,
                                 default='M')
    test_date = models.DateField()

    def __unicode__(self):
        return self.description

class Test(models.Model):
    student = models.ForeignKey(Student)
    instructor = models.ForeignKey(InstructorGroup, null=True, blank=True)
    test_group = models.ForeignKey(TestGroup)
    test_rank = models.ForeignKey(Rank,
                                  verbose_name="Testing For") 
    passed = models.BooleanField(default=False)
    # notes = models.TextField() -- do i need this if it is included in score?
    average = models.DecimalField(max_digits=4,decimal_places=2,
                                  blank=True, null=True)

    def __unicode__(self):
        return self.test_group.description + ' - ' + self.test_rank.rank

class TestScore(models.Model):
    test = models.ForeignKey(Test)
    field = models.CharField(max_length=100)
    score = models.CharField(max_length=5,blank=True)
    notes = models.TextField(blank=True)

class RTGroup(models.Model):
    test_score = models.ForeignKey(TestScore)
    instructor = models.ForeignKey(InstructorGroup, null=True,blank=True,
                                   verbose_name="Sign Off Instructor")
    sign_off = models.BooleanField(default=False)
    sign_off_date = models.DateField(null=True,
                                     blank=True)

    class Meta:
        verbose_name = "RT Group"
        verbose_name_plural = "RT Groups"

class TippingGroup(models.Model):
    description = models.CharField(max_length=200, unique=True)
    date = models.DateField()
    
    def __unicode__(self):
        return self.description
    
class TippingStudent(models.Model):
    student = models.ForeignKey(Student)
    tipping_group = models.ForeignKey(TippingGroup)
    rank = models.ForeignKey(Rank)
    # test = models.ForeignKey(Test)

    def __unicode__(self):
        return self.tipping_group.description + ' - ' + \
                self.rank.rank

class Tip(models.Model):
    TIP_COLOR_CHOICES = (
        ('G','Green'),
        ('B','Blue'),
        ('R','Red'),
        ('W','White'),
        ('Y','Yellow'),
    )
    instructor = models.ForeignKey(InstructorGroup)
    tip_date = models.DateField(default=date.today())
    tipped = models.BooleanField(default=False)
    tip_color = models.CharField(max_length=1, choices=TIP_COLOR_CHOICES)
    tipping_student = models.ForeignKey(TippingStudent)
    notes = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.tip_color + ' - ' + \
                self.tipping_student.tipping_group.description + \
                ' - ' + self.tipping_student.student.first_name + ' ' + \
                self.tipping_student.student.last_name + ' - ' + \
                str(self.tipped)

# Attendance
class Attendance(models.Model):
    ATTENDANCE_CHOICES = (
        ('A','A'),
        ('B','B'),
        ('C','Candidate'),
        ('S','Saturday'),
        ('U','AAU'),
        ('T','Test'),
        ('W','SWAT'),
        ('L','Leadership'),
    )

    attendance_type = models.CharField(max_length=1,
                                       choices=ATTENDANCE_CHOICES)
    attendance_date = models.DateField(default=date.today())
    attendance_time = models.TimeField(auto_now_add=True)
    student = models.ForeignKey(Student)

    class Meta:
        verbose_name_plural = "Attendance"

    def __unicode__(self):
        return self.student.first_name + ' ' + self.student.last_name + ' - ' + \
                self.attendance_type + ' - ' + \
                self.attendance_date.strftime('%B %d, %Y')

# Fitness #
class PresidentialRequirements(models.Model):
    GENDER_CHOICES = (
        ('M','Male'),
        ('F','Female'),
    )
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    pushups = models.IntegerField()
    situps = models.IntegerField()
    mile_time = models.IntegerField()
    bike_time = models.IntegerField(blank=True,null=True)

    class Meta:
        verbose_name = "Presidential Fitness Requirements"
        verbose_name_plural = "Presidential Fitness Requirements"

class Fitness(models.Model):
    student = models.ForeignKey(Student)
    weight = models.DecimalField(max_digits=5, decimal_places=2,
                                 blank=True, null=True)
    pushups = models.IntegerField(blank=True, null=True)
    situps = models.IntegerField(blank=True, null=True)
    mile_time = models.IntegerField(blank=True, null=True) # need to translate this to MM:SS format
    bike_time = models.IntegerField(blank=True, null=True) # need to translate this to MM:SS format
    pushup_percent = models.DecimalField(max_digits=5, decimal_places=2,
                                         blank=True, null=True)
    situps_percent = models.DecimalField(max_digits=5, decimal_places=2,
                                         blank=True, null=True)
    mile_percent = models.DecimalField(max_digits=5, decimal_places=2,
                                       blank=True, null=True)
    bike_percent = models.DecimalField(max_digits=5, decimal_places=2,
                                       blank=True, null=True)
    bodyfat = models.IntegerField(blank=True, null=True) # only show up if over 18
    date = models.DateField(auto_now_add=True, null=True, blank=True)
    test = models.ForeignKey(Test, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Fitness"

# Billing #
class Tuition(models.Model):
    student = models.ForeignKey(Student)
    bill_name = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    paid = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Tuition"
