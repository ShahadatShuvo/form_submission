from django.db import models


# Create your models here.

class GuardianInfo(models.Model):
    BLOOD_CHOICES= (
        (1, 'A(+ve)'),
        (2, 'A(-ve)'),
        (3, 'B(+ve)'),
        (4, 'B(-ve)'),
        (5, 'AB(+ve)'),
        (6, 'AB(-ve)'),
        (7, 'O(+ve)'),
        (8, 'O(-ve)'),
    )
    GENDER_CHOICES = (
        (1, 'Male'),
        (2, 'Female'),
        (3, 'Both'),
    )
    MARITAL_CHOICES = (
        (1, 'Married'),
        (2, 'Unmarried'),
        (3, 'Divorced'),
        (4, 'Widow'),
        (5, 'Widower'),
    )


    student_reg_no = models.IntegerField(default=0, null=True)
    student_name = models.CharField(max_length=30)
    fathers_name = models.CharField(max_length=30)
    mothers_name = models.CharField(max_length=30)
    applicant_gender = models.PositiveIntegerField(
        ('Applicant Gender'), choices=GENDER_CHOICES, null=True
    )
    marital_status = models.PositiveIntegerField(
        ('Applicant Marital Status'), choices=MARITAL_CHOICES, null=True
    )
    blood_group = models.PositiveIntegerField(
        ('Blood Group'), choices=BLOOD_CHOICES, null=True
    )
    nationality = models.CharField(max_length=10, null=True)
    religion = models.CharField(max_length=10, null=True)
    relation_with_student = models.CharField(max_length=30, null=True)
    guardianship_type = models.CharField(max_length=20, null=True)
    annual_income = models.IntegerField(default=0, null=True)
    profession = models.CharField(max_length=20, null=True)
    phone_number_home = models.CharField(default=0, max_length=11, null=True)
    phone_number_office = models.CharField(default=0, max_length=11, null=True)
    present_address = models.CharField(max_length=30, null=True)
    permanent_address = models.CharField(max_length=30, null=True)
    office_address = models.CharField(max_length=30, null=True)


