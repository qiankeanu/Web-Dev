from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

class Status(models.TextChoices):
    ACTIVE_SEARCHING="AS","Activly Searching workspace, currently unemployed"
    SEARCHING="S","Not activly searching job,currently employed"
    NOT_READY="NR","Ready to look for job offer,not searching job,currently employed"
    NOT_INTERESTED="NI","employed,notsearching for job,not interested in job offers"

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    surname=models.CharField(max_length=255)
    middle_name=models.CharField(max_length=255)
    given_name=models.CharField(max_length=255)
    birthday=models.DateField(
        auto_now_add=False,
        blank=True
    )
    phone_number=PhoneNumberField(blank=True)
    photo=models.ImageField(
        upload_to='img',
        blank=True)
    status=models.CharField(
        choices=Status.choices,
        max_length=2)
    def get_full_name(self):
        return f"{self.given_name} {self.middle_name} {self.surname}"
    def __str__(self):
        return self.get_full_name()
