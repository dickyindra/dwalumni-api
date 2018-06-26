from django.db import models
from django.contrib.auth.models import User
import datetime

class Major(models.Model):
    class Meta:
        db_table = "major"

    name = models.CharField(max_length=45)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='major_created_by'
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='major_updated_by'
    )

class Education(models.Model):
    class Meta:
        db_table = "education"

    name = models.CharField(max_length=50)
    logo = models.CharField(max_length=255)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='education_created_by'
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='education_updated_by'
    )

class EducationMajor(models.Model):
    class Meta:
        db_table = "education_major"

    major = models.ForeignKey(
        Major,
        on_delete=models.CASCADE
    )
    education = models.ForeignKey(
        Education,
        on_delete=models.CASCADE
    )

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='education_major_created_by'
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='education_major_updated_by'
    )

class UserEducation(models.Model):
    class Meta:
        db_table = "user_education"

    YEAR_CHOICES = [(r, str(r)) for r in range(1984, datetime.date.today().year+1)]

    education = models.ForeignKey(
        Education,
        on_delete=models.CASCADE
    )
    degeree = models.CharField(max_length=2)
    begining_year = models.IntegerField(('year'), choices=YEAR_CHOICES)
    end_year = models.IntegerField(('year'), choices=YEAR_CHOICES)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='user_education_created_by'
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='user_education_updated_by'
    )
