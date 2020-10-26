from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class PUser(models.Model):
    confirm_number = models.CharField(max_length=16, unique=True, verbose_name='Confirmation Number')
    name = models.CharField(max_length=100, verbose_name='Last/Family Name')
    birth = models.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2010)],
                                verbose_name='Year of Birth')
    won = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ariza topshirganlar'
        verbose_name_plural = 'Ariza topshirganlar'


class Member(models.Model):
    WHO_IS = (
        ('SPOUSE', 'SPOUSE'),
        ('CHILD', 'CHILD'),
    )
    name = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    relationship = models.CharField(max_length=20, choices=WHO_IS)

    def __str__(self):
        # return self.name + '  |  ' + self.lastname + '  |  ' + self.relationship
        return self.name + '  |  ' + self.lastname


class Winner(models.Model):
    WHO_IS = (
        ('APPLICANT', 'APPLICANT'),
        ('ATTORNEY', 'ATTORNEY'),
        ('THIRD', 'THIRD-PARTY-AGENT'),
    )
    name = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    address = models.CharField(max_length=250)
    case_number = models.CharField(max_length=16, unique=True, verbose_name='Case Number')
    confirm_number = models.CharField(max_length=16, unique=True, verbose_name='Confirmation Number')
    birth_date = models.DateField(verbose_name='Date of Birth')
    status = models.CharField(max_length=20, choices=WHO_IS)
    member = models.ManyToManyField(Member, blank=True)

    def __str__(self):
        return self.case_number

    class Meta:
        verbose_name = 'G\'oliblar'
        verbose_name_plural = 'G\'oliblar'
