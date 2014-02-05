# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Student'
        db.create_table(u'crm_student', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('address1', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('address2', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(default='Morgan Hill', max_length=100, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(default='California', max_length=50, blank=True)),
            ('zipcode', self.gf('django.db.models.fields.IntegerField')(default=95037, null=True, blank=True)),
            ('dob', self.gf('django.db.models.fields.DateField')()),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('uniform_size', self.gf('django.db.models.fields.CharField')(max_length=3, blank=True)),
            ('belt_size', self.gf('django.db.models.fields.CharField')(max_length=3, blank=True)),
            ('class_time', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.Class'], null=True, blank=True)),
            ('rank', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.Rank'], to_field='rank', null=True, blank=True)),
            ('anniv_month', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('benefits', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('limitations', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('referral', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.Student'], null=True, blank=True)),
            ('total_years', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'crm', ['Student'])

        # Adding model 'Contact'
        db.create_table(u'crm_contact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('address1', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('address2', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(default='Morgan Hill', max_length=100, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(default='California', max_length=50, blank=True)),
            ('zipcode', self.gf('django.db.models.fields.IntegerField')(default=95037, null=True, blank=True)),
        ))
        db.send_create_signal(u'crm', ['Contact'])

        # Adding model 'Relationship'
        db.create_table(u'crm_relationship', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.Student'])),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.Contact'])),
            ('relationship', self.gf('django.db.models.fields.CharField')(default='O', max_length=1)),
        ))
        db.send_create_signal(u'crm', ['Relationship'])

        # Adding model 'StudentEmail'
        db.create_table(u'crm_studentemail', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=254)),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.Student'])),
        ))
        db.send_create_signal(u'crm', ['StudentEmail'])

        # Adding model 'ContactEmail'
        db.create_table(u'crm_contactemail', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=254)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.Contact'])),
        ))
        db.send_create_signal(u'crm', ['ContactEmail'])

        # Adding model 'StudentPhone'
        db.create_table(u'crm_studentphone', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=14)),
            ('phone_type', self.gf('django.db.models.fields.CharField')(default='C', max_length=1)),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.Student'])),
        ))
        db.send_create_signal(u'crm', ['StudentPhone'])

        # Adding model 'ContactPhone'
        db.create_table(u'crm_contactphone', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=14)),
            ('phone_type', self.gf('django.db.models.fields.CharField')(default='C', max_length=1)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.Contact'])),
        ))
        db.send_create_signal(u'crm', ['ContactPhone'])

        # Adding model 'HoldHarmless'
        db.create_table(u'crm_holdharmless', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal(u'crm', ['HoldHarmless'])

        # Adding model 'HoldHarmlessStudent'
        db.create_table(u'crm_holdharmlessstudent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hold_harmless', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.HoldHarmless'])),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.Student'])),
            ('date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 2, 4, 0, 0))),
        ))
        db.send_create_signal(u'crm', ['HoldHarmlessStudent'])

        # Adding model 'Barcode'
        db.create_table(u'crm_barcode', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.Student'])),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('code_loc', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('card_type', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal(u'crm', ['Barcode'])

        # Adding model 'Session'
        db.create_table(u'crm_session', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('session_name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=300)),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('rate', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=2, blank=True)),
        ))
        db.send_create_signal(u'crm', ['Session'])

        # Adding model 'SessionMember'
        db.create_table(u'crm_sessionmember', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('session', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.Session'])),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.Student'])),
            ('receive_email', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('paid', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'crm', ['SessionMember'])

        # Adding model 'SessionAttendance'
        db.create_table(u'crm_sessionattendance', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('session_member', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.SessionMember'])),
            ('date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 2, 4, 0, 0))),
        ))
        db.send_create_signal(u'crm', ['SessionAttendance'])

        # Adding model 'GroupCategory'
        db.create_table(u'crm_groupcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('group_category', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
        ))
        db.send_create_signal(u'crm', ['GroupCategory'])

        # Adding model 'Group'
        db.create_table(u'crm_group', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('group', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('group_category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.GroupCategory'])),
        ))
        db.send_create_signal(u'crm', ['Group'])

        # Adding model 'BBCGroup'
        db.create_table(u'crm_bbcgroup', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('group_category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.GroupCategory'])),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.Group'])),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.Student'])),
            ('join_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 2, 4, 0, 0))),
            ('receive_email', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('goals', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('rate', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
        ))
        db.send_create_signal(u'crm', ['BBCGroup'])

        # Adding model 'MCGroup'
        db.create_table(u'crm_mcgroup', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('group_category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.GroupCategory'])),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.Group'])),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.Student'])),
            ('join_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 2, 4, 0, 0))),
            ('receive_email', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('goals', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('rate', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
        ))
        db.send_create_signal(u'crm', ['MCGroup'])

        # Adding model 'AAUGroup'
        db.create_table(u'crm_aaugroup', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('group_category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.GroupCategory'])),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.Group'])),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.Student'])),
            ('join_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 2, 4, 0, 0))),
            ('receive_email', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('aau_rank', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.AAURank'])),
        ))
        db.send_create_signal(u'crm', ['AAUGroup'])

        # Adding model 'InstructorGroup'
        db.create_table(u'crm_instructorgroup', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('group_category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.GroupCategory'])),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.Group'])),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.Student'])),
            ('join_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 2, 4, 0, 0))),
            ('receive_email', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'crm', ['InstructorGroup'])

        # Adding model 'LeadershipGroup'
        db.create_table(u'crm_leadershipgroup', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('group_category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.GroupCategory'])),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.Group'])),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.Student'])),
            ('join_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 2, 4, 0, 0))),
            ('receive_email', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'crm', ['LeadershipGroup'])

        # Adding model 'Status'
        db.create_table(u'crm_status', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('status', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
        ))
        db.send_create_signal(u'crm', ['Status'])

        # Adding model 'StatusStudent'
        db.create_table(u'crm_statusstudent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.Student'])),
            ('status', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.Status'])),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('rate', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=2, blank=True)),
        ))
        db.send_create_signal(u'crm', ['StatusStudent'])

        # Adding model 'Class'
        db.create_table(u'crm_class', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('class_time', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
        ))
        db.send_create_signal(u'crm', ['Class'])

        # Adding model 'Rank'
        db.create_table(u'crm_rank', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rank', self.gf('django.db.models.fields.CharField')(unique=True, max_length=60)),
        ))
        db.send_create_signal(u'crm', ['Rank'])

        # Adding model 'AAURank'
        db.create_table(u'crm_aaurank', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('aau_rank', self.gf('django.db.models.fields.CharField')(unique=True, max_length=60)),
        ))
        db.send_create_signal(u'crm', ['AAURank'])

        # Adding model 'TestGroup'
        db.create_table(u'crm_testgroup', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
            ('test_type', self.gf('django.db.models.fields.CharField')(default='M', max_length=1)),
            ('test_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'crm', ['TestGroup'])

        # Adding model 'Test'
        db.create_table(u'crm_test', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.Student'])),
            ('instructor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.InstructorGroup'], null=True, blank=True)),
            ('test_group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.TestGroup'])),
            ('test_rank', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.Rank'])),
            ('passed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('average', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
        ))
        db.send_create_signal(u'crm', ['Test'])

        # Adding model 'TestScore'
        db.create_table(u'crm_testscore', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('test', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.Test'])),
            ('field', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('score', self.gf('django.db.models.fields.CharField')(max_length=5, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'crm', ['TestScore'])

        # Adding model 'RTGroup'
        db.create_table(u'crm_rtgroup', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('test_score', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.TestScore'])),
            ('instructor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.InstructorGroup'], null=True, blank=True)),
            ('sign_off', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('sign_off_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'crm', ['RTGroup'])

        # Adding model 'TippingGroup'
        db.create_table(u'crm_tippinggroup', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
            ('date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'crm', ['TippingGroup'])

        # Adding model 'TippingStudent'
        db.create_table(u'crm_tippingstudent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.Student'])),
            ('tipping_group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.TippingGroup'])),
            ('rank', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.Rank'])),
        ))
        db.send_create_signal(u'crm', ['TippingStudent'])

        # Adding model 'Tip'
        db.create_table(u'crm_tip', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('instructor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.InstructorGroup'])),
            ('tip_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 2, 4, 0, 0))),
            ('tipped', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('tip_color', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('tipping_student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.TippingStudent'])),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'crm', ['Tip'])

        # Adding model 'Attendance'
        db.create_table(u'crm_attendance', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('attendance_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('attendance_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 2, 4, 0, 0))),
            ('attendance_time', self.gf('django.db.models.fields.TimeField')(auto_now_add=True, blank=True)),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.Student'])),
        ))
        db.send_create_signal(u'crm', ['Attendance'])

        # Adding model 'PresidentialRequirements'
        db.create_table(u'crm_presidentialrequirements', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('age', self.gf('django.db.models.fields.IntegerField')()),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('pushups', self.gf('django.db.models.fields.IntegerField')()),
            ('situps', self.gf('django.db.models.fields.IntegerField')()),
            ('mile_time', self.gf('django.db.models.fields.IntegerField')()),
            ('bike_time', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'crm', ['PresidentialRequirements'])

        # Adding model 'Fitness'
        db.create_table(u'crm_fitness', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.Student'])),
            ('weight', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True)),
            ('pushups', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('situps', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('mile_time', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('bike_time', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('pushup_percent', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True)),
            ('situps_percent', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True)),
            ('mile_percent', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True)),
            ('bike_percent', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True)),
            ('bodyfat', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, null=True, blank=True)),
            ('test', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.Test'], null=True, blank=True)),
        ))
        db.send_create_signal(u'crm', ['Fitness'])

        # Adding model 'Tuition'
        db.create_table(u'crm_tuition', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.Student'])),
            ('bill_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
            ('paid', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'crm', ['Tuition'])


    def backwards(self, orm):
        # Deleting model 'Student'
        db.delete_table(u'crm_student')

        # Deleting model 'Contact'
        db.delete_table(u'crm_contact')

        # Deleting model 'Relationship'
        db.delete_table(u'crm_relationship')

        # Deleting model 'StudentEmail'
        db.delete_table(u'crm_studentemail')

        # Deleting model 'ContactEmail'
        db.delete_table(u'crm_contactemail')

        # Deleting model 'StudentPhone'
        db.delete_table(u'crm_studentphone')

        # Deleting model 'ContactPhone'
        db.delete_table(u'crm_contactphone')

        # Deleting model 'HoldHarmless'
        db.delete_table(u'crm_holdharmless')

        # Deleting model 'HoldHarmlessStudent'
        db.delete_table(u'crm_holdharmlessstudent')

        # Deleting model 'Barcode'
        db.delete_table(u'crm_barcode')

        # Deleting model 'Session'
        db.delete_table(u'crm_session')

        # Deleting model 'SessionMember'
        db.delete_table(u'crm_sessionmember')

        # Deleting model 'SessionAttendance'
        db.delete_table(u'crm_sessionattendance')

        # Deleting model 'GroupCategory'
        db.delete_table(u'crm_groupcategory')

        # Deleting model 'Group'
        db.delete_table(u'crm_group')

        # Deleting model 'BBCGroup'
        db.delete_table(u'crm_bbcgroup')

        # Deleting model 'MCGroup'
        db.delete_table(u'crm_mcgroup')

        # Deleting model 'AAUGroup'
        db.delete_table(u'crm_aaugroup')

        # Deleting model 'InstructorGroup'
        db.delete_table(u'crm_instructorgroup')

        # Deleting model 'LeadershipGroup'
        db.delete_table(u'crm_leadershipgroup')

        # Deleting model 'Status'
        db.delete_table(u'crm_status')

        # Deleting model 'StatusStudent'
        db.delete_table(u'crm_statusstudent')

        # Deleting model 'Class'
        db.delete_table(u'crm_class')

        # Deleting model 'Rank'
        db.delete_table(u'crm_rank')

        # Deleting model 'AAURank'
        db.delete_table(u'crm_aaurank')

        # Deleting model 'TestGroup'
        db.delete_table(u'crm_testgroup')

        # Deleting model 'Test'
        db.delete_table(u'crm_test')

        # Deleting model 'TestScore'
        db.delete_table(u'crm_testscore')

        # Deleting model 'RTGroup'
        db.delete_table(u'crm_rtgroup')

        # Deleting model 'TippingGroup'
        db.delete_table(u'crm_tippinggroup')

        # Deleting model 'TippingStudent'
        db.delete_table(u'crm_tippingstudent')

        # Deleting model 'Tip'
        db.delete_table(u'crm_tip')

        # Deleting model 'Attendance'
        db.delete_table(u'crm_attendance')

        # Deleting model 'PresidentialRequirements'
        db.delete_table(u'crm_presidentialrequirements')

        # Deleting model 'Fitness'
        db.delete_table(u'crm_fitness')

        # Deleting model 'Tuition'
        db.delete_table(u'crm_tuition')


    models = {
        u'crm.aaugroup': {
            'Meta': {'object_name': 'AAUGroup'},
            'aau_rank': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.AAURank']"}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.Group']"}),
            'group_category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.GroupCategory']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'join_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 2, 4, 0, 0)'}),
            'receive_email': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.Student']"})
        },
        u'crm.aaurank': {
            'Meta': {'object_name': 'AAURank'},
            'aau_rank': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'crm.attendance': {
            'Meta': {'object_name': 'Attendance'},
            'attendance_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 2, 4, 0, 0)'}),
            'attendance_time': ('django.db.models.fields.TimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'attendance_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.Student']"})
        },
        u'crm.barcode': {
            'Meta': {'object_name': 'Barcode'},
            'card_type': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'code_loc': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.Student']"})
        },
        u'crm.bbcgroup': {
            'Meta': {'object_name': 'BBCGroup'},
            'goals': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.Group']"}),
            'group_category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.GroupCategory']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'join_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 2, 4, 0, 0)'}),
            'rate': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'receive_email': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.Student']"})
        },
        u'crm.class': {
            'Meta': {'object_name': 'Class'},
            'class_time': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'crm.contact': {
            'Meta': {'object_name': 'Contact'},
            'address1': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'default': "'Morgan Hill'", 'max_length': '100', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'state': ('django.db.models.fields.CharField', [], {'default': "'California'", 'max_length': '50', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.IntegerField', [], {'default': '95037', 'null': 'True', 'blank': 'True'})
        },
        u'crm.contactemail': {
            'Meta': {'object_name': 'ContactEmail'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.Contact']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'crm.contactphone': {
            'Meta': {'object_name': 'ContactPhone'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.Contact']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '14'}),
            'phone_type': ('django.db.models.fields.CharField', [], {'default': "'C'", 'max_length': '1'})
        },
        u'crm.fitness': {
            'Meta': {'object_name': 'Fitness'},
            'bike_percent': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'bike_time': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'bodyfat': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mile_percent': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'mile_time': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pushup_percent': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'pushups': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'situps': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'situps_percent': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.Student']"}),
            'test': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.Test']", 'null': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'})
        },
        u'crm.group': {
            'Meta': {'object_name': 'Group'},
            'group': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'group_category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.GroupCategory']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'crm.groupcategory': {
            'Meta': {'object_name': 'GroupCategory'},
            'group_category': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'crm.holdharmless': {
            'Meta': {'object_name': 'HoldHarmless'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'crm.holdharmlessstudent': {
            'Meta': {'object_name': 'HoldHarmlessStudent'},
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 2, 4, 0, 0)'}),
            'hold_harmless': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.HoldHarmless']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.Student']"})
        },
        u'crm.instructorgroup': {
            'Meta': {'object_name': 'InstructorGroup'},
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.Group']"}),
            'group_category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.GroupCategory']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'join_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 2, 4, 0, 0)'}),
            'receive_email': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.Student']"})
        },
        u'crm.leadershipgroup': {
            'Meta': {'object_name': 'LeadershipGroup'},
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.Group']"}),
            'group_category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.GroupCategory']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'join_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 2, 4, 0, 0)'}),
            'receive_email': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.Student']"})
        },
        u'crm.mcgroup': {
            'Meta': {'object_name': 'MCGroup'},
            'goals': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.Group']"}),
            'group_category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.GroupCategory']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'join_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 2, 4, 0, 0)'}),
            'rate': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'receive_email': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.Student']"})
        },
        u'crm.presidentialrequirements': {
            'Meta': {'object_name': 'PresidentialRequirements'},
            'age': ('django.db.models.fields.IntegerField', [], {}),
            'bike_time': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mile_time': ('django.db.models.fields.IntegerField', [], {}),
            'pushups': ('django.db.models.fields.IntegerField', [], {}),
            'situps': ('django.db.models.fields.IntegerField', [], {})
        },
        u'crm.rank': {
            'Meta': {'object_name': 'Rank'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rank': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'})
        },
        u'crm.relationship': {
            'Meta': {'object_name': 'Relationship'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.Contact']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'relationship': ('django.db.models.fields.CharField', [], {'default': "'O'", 'max_length': '1'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.Student']"})
        },
        u'crm.rtgroup': {
            'Meta': {'object_name': 'RTGroup'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instructor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.InstructorGroup']", 'null': 'True', 'blank': 'True'}),
            'sign_off': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sign_off_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'test_score': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.TestScore']"})
        },
        u'crm.session': {
            'Meta': {'object_name': 'Session'},
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'session_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '300'}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        },
        u'crm.sessionattendance': {
            'Meta': {'object_name': 'SessionAttendance'},
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 2, 4, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'session_member': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.SessionMember']"})
        },
        u'crm.sessionmember': {
            'Meta': {'object_name': 'SessionMember'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'paid': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'receive_email': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'session': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.Session']"}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.Student']"})
        },
        u'crm.status': {
            'Meta': {'object_name': 'Status'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'})
        },
        u'crm.statusstudent': {
            'Meta': {'object_name': 'StatusStudent'},
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.Status']"}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.Student']"})
        },
        u'crm.student': {
            'Meta': {'object_name': 'Student'},
            'address1': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'anniv_month': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'belt_size': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'}),
            'benefits': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'default': "'Morgan Hill'", 'max_length': '100', 'blank': 'True'}),
            'class_time': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.Class']", 'null': 'True', 'blank': 'True'}),
            'dob': ('django.db.models.fields.DateField', [], {}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'limitations': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'rank': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.Rank']", 'to_field': "'rank'", 'null': 'True', 'blank': 'True'}),
            'referral': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.Student']", 'null': 'True', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'state': ('django.db.models.fields.CharField', [], {'default': "'California'", 'max_length': '50', 'blank': 'True'}),
            'total_years': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'uniform_size': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.IntegerField', [], {'default': '95037', 'null': 'True', 'blank': 'True'})
        },
        u'crm.studentemail': {
            'Meta': {'object_name': 'StudentEmail'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.Student']"})
        },
        u'crm.studentphone': {
            'Meta': {'object_name': 'StudentPhone'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '14'}),
            'phone_type': ('django.db.models.fields.CharField', [], {'default': "'C'", 'max_length': '1'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.Student']"})
        },
        u'crm.test': {
            'Meta': {'object_name': 'Test'},
            'average': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instructor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.InstructorGroup']", 'null': 'True', 'blank': 'True'}),
            'passed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.Student']"}),
            'test_group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.TestGroup']"}),
            'test_rank': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.Rank']"})
        },
        u'crm.testgroup': {
            'Meta': {'object_name': 'TestGroup'},
            'description': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'test_date': ('django.db.models.fields.DateField', [], {}),
            'test_type': ('django.db.models.fields.CharField', [], {'default': "'M'", 'max_length': '1'})
        },
        u'crm.testscore': {
            'Meta': {'object_name': 'TestScore'},
            'field': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'score': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            'test': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.Test']"})
        },
        u'crm.tip': {
            'Meta': {'object_name': 'Tip'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instructor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.InstructorGroup']"}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'tip_color': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'tip_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 2, 4, 0, 0)'}),
            'tipped': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tipping_student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.TippingStudent']"})
        },
        u'crm.tippinggroup': {
            'Meta': {'object_name': 'TippingGroup'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'crm.tippingstudent': {
            'Meta': {'object_name': 'TippingStudent'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rank': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.Rank']"}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.Student']"}),
            'tipping_group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.TippingGroup']"})
        },
        u'crm.tuition': {
            'Meta': {'object_name': 'Tuition'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'bill_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'paid': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.Student']"})
        }
    }

    complete_apps = ['crm']