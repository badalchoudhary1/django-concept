from django.db import models
from django import forms
from django.core import validators

def start_with(value):
    if value[0] !='s':
        raise forms.ValidationError("value not start with s")
def validate_mail(value):
    if "@gmail.com" in value:
        return value
    else:
        raise forms.ValidationError("this field accepts mail id of google only")
def mobile_no(value):
    mobile=str(value)
    if len(mobile) !=10:
        raise forms.ValidationError("mobile number should 10 digit")
# Create your models here.
class Employee(models.Model):
    eid=models.CharField(max_length=20)
    ename=models.CharField(max_length=100,validators=[start_with])
    eemail=models.EmailField(validators=[validate_mail])
    econtact=models.CharField(max_length=15,validators=[mobile_no])

    class Meta:
        db_table="employee"


class WangUser(models.Model):
    username=models.CharField(max_length=32,unique=True)
    password=models.CharField(max_length=32)
    email=models.CharField(max_length=32)