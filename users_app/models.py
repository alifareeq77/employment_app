from form_app.models import Form
from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import CustomUserManager
from .languages import LANGUAGES


class CustomUser(AbstractUser):
    username = None
    first_name = None
    last_name = None
    email = models.EmailField(verbose_name="Email", null=True, unique=True)
    is_completed = models.BooleanField(default=False)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


# after creating the basic user and verifying the email we check for payment
class GenderChoices(models.TextChoices):
    Female = ("F", 'Female')
    Male = ('M', 'Male')


class EthnicityChoices(models.TextChoices):
    ARAB = ('ar', 'iraqi-arab')
    KURDISH = ('kr', 'iraqi-kurdish')
    IRAQI_OTHER = ('io', 'iraqi-other')
    OTHER = ('o', 'other')


class CurrentJobLevelChoices(models.TextChoices):
    ENTRY_LEVEL = 'EN', 'Entry Level'
    MID_LEVEL = 'MI', 'Mid Level'
    SENIOR_LEVEL = 'SE', 'Senior Level'
    EXECUTIVE_LEVEL = 'EX', 'Executive Level'


class EducationalQualification(models.TextChoices):
    HIGH_SCHOOL = 'High School', 'High School'
    DIPLOMA = 'Diploma', 'Diploma'
    BACHELORS_DEGREE = 'Bachelor\'s Degree', 'Bachelor\'s Degree'
    MASTERS_DEGREE = 'Master\'s Degree', 'Master\'s Degree'
    DOCTORATE = 'Doctorate', 'Doctorate'


class EmploymentIndustry(models.TextChoices):
    IT = 'Information Technology', 'Information Technology'
    FINANCE = 'Finance', 'Finance'
    HEALTHCARE = 'Healthcare', 'Healthcare'
    EDUCATION = 'Education', 'Education'
    MANUFACTURING = 'Manufacturing', 'Manufacturing'
    RETAIL = 'Retail', 'Retail'
    OTHER = 'Other', 'Other'


class CityChoices(models.TextChoices):
    AL_ANBAR = 'AN'
    BABYLON = 'BB'
    BAGHDAD = 'BG'
    BASRA = 'BA'
    DHI_QAR = 'DQ'
    AL_QADISIYYAH = 'QA'
    DIYALA = 'DI'
    DUHOK = 'DA'
    ERBIL = 'AR'
    KARBLA = 'KA'
    KIRKUK = 'KI'
    MAYSAN = 'MA'
    MUTHANNA = 'MU'
    NAJAF = 'NA'
    NINEVEH = 'NI'
    SALADIN = 'SD'
    SULAYMANIUAH = 'SU'
    WASIT = 'WA'


class Appliers(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    gender = models.CharField(max_length=2, choices=GenderChoices.choices, null=False)
    DOB = models.DateField()
    native_language_spoken = models.CharField(null=False, max_length=8, choices=LANGUAGES)
    advanced_languages_spoken = models.CharField(null=True, max_length=8, choices=LANGUAGES)
    intermediate_languages_spoken = models.CharField(null=True, max_length=8, choices=LANGUAGES)
    basic_languages_spoken = models.CharField(null=False, max_length=8, choices=LANGUAGES)
    ethnicity = models.CharField(max_length=5, choices=EthnicityChoices.choices)
    current_job_level = models.CharField(max_length=5, choices=CurrentJobLevelChoices.choices)
    current_employment_industry = models.CharField(max_length=50, choices=EmploymentIndustry.choices, )
    highest_education = models.CharField(max_length=20, choices=EducationalQualification.choices, )
    years_of_experience = models.IntegerField()
    location_of_working = models.CharField(max_length=4, choices=CityChoices.choices)
    linked_in_account = models.URLField(blank=True,null=True)

    def __str__(self):
        return self.first_name


class Owner(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return self.user.email
