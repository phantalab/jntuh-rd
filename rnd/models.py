from django.db import models

# Create your models here.
class PrePHD(models.Model):
    Student_roll_number = models.CharField(max_length=20)
    Subject_name = models.CharField(max_length=100)
    Registration_month =  models.DateField()
    Marks_obtained = models.FloatField()

class Research_Methodology(models.Model):
    Student_roll_number = models.CharField(max_length=20)
    Date = models.DateField()
    TYPE_SELECT_1 = (
        ('0', 'No'),
        ('1', 'Yes'),
    )
    Satisfaction = models.CharField(max_length=11,choices=TYPE_SELECT_1)
    TYPE_SELECT_2 = (
        ('0', 'No'),
        ('1', 'Yes'),
    )
    Completed = models.CharField(max_length=11,choices=TYPE_SELECT_2)

class RRM(models.Model):
    Student_roll_number = models.CharField(max_length=20)
    RRM_number = models.CharField(max_length=20)
    Date_of_registration = models.DateField()
    TYPE_SELECT_1 = (
    ('0', 'No'),
    ('1', 'Yes'),
    )
    Satisfaction = models.CharField(max_length=11,choices=TYPE_SELECT_1)
    Marks_obtained = models.FloatField()

class Colloquium(models.Model):
    Student_roll_number = models.CharField(max_length=20)
    Submission_date = models.DateField()
    TYPE_SELECT_1 = (
    ('0', 'No'),
    ('1', 'Yes'),
    )
    Satisfaction = models.CharField(max_length=11,choices=TYPE_SELECT_1)

class Revise_and_Resubmission(models.Model):
    Student_roll_number = models.CharField(max_length=20)
    Submission_date_of_revised_thesis = models.DateField()
    Date_communicated_to_DE = models.DateField()



class Plagarism(models.Model):
    Student_roll_number = models.CharField(max_length=20)
    Date = models.DateField()
    File_upload = models.FileField()

class Thesis_Submission(models.Model):
    Student_roll_number = models.CharField(max_length=20)
    Student_submission_date = models.DateField()
    Submission_date_to_DE = models.DateField()
    Reviewing_reports_by_DE = models.DateField()
    Date_of_communication_to_student = models.DateField()

class Viva_Voca(models.Model):
    Student_roll_number = models.CharField(max_length=20)
    DE_intimation_date = models.DateField()
    Final_dates = models.DateField()


class Extension_period(models.Model):
    Student_roll_number = models.CharField(max_length=20)
    Date = models.DateField()
    TYPE_SELECT = (
        ('0', 'Permission Granted'),
        ('1', 'Permission Denied'),
    )
    Permission = models.CharField(max_length=11,choices=TYPE_SELECT)

class Change_of_supervisor_or_co_supervisor(models.Model):
    Student_roll_number = models.CharField(max_length=20)
    Application_date = models.DateField()


