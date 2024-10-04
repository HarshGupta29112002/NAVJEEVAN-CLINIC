# from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
import random
from datetime import datetime
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal
from django.db.models import ImageField
from django.urls import reverse

# PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]

def generate_unique_id():
    # Generate a random 6-digit number
    return str(random.randint(100000, 999999))

class patient(models.Model):

    # id = models.CharField(max_length=6, primary_key=True, default=generate_unique_id, editable=False, unique=True)
    id = models.CharField(max_length=6, primary_key=True, unique=True, default ='')
    date = models.DateField(default= timezone.now)
    name = models.CharField(default='', max_length=255)
    sex = models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='', max_length=1)
    age = models.CharField(default='', max_length= 100)
    weight = models.CharField(default='', max_length= 100)
    mobile_number = models.CharField(max_length=10, default='')
    Complain = models.CharField(default='', max_length=200)
    BP = models.CharField(max_length=15, blank=True, null=True, default=None)
    PR = models.CharField(max_length=3, default='' )      #(max_length = 3, db_column='PR' + suffix)    
    SPO2 = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(100)])
    Temp =models.FloatField(default=0)
    Advice = models.CharField(default='',max_length=200)
    Medicine = models.CharField(default='', max_length=200)
    Duration = models.CharField(default='', max_length=200)
    Days = models.CharField(default='', max_length=20)
    Online_payment = models.CharField(default='',max_length=255)
    Cash_payment = models.CharField(default='', max_length=255)
    Balance_amount = models.CharField(default='', max_length=255)
    Paid_amount = models.CharField(default='', max_length=255)
    Total_amount = models.CharField(default='', max_length=255)


    def save(self, *args, **kwargs):

        if not self.id:
            # Generate a 6-digit ID using the current date and a counter
            today_str = datetime.today().strftime('%y%m%d')
            existing_ids = patient.objects.filter(id__startswith=today_str).values_list('id', flat=True)
            counter = 1

            while today_str + str(counter).zfill(3) in existing_ids:
                counter += 1

            self.id = today_str + str(counter).zfill(3)

        if self.age is not None and str(self.age).strip() != '':
            # Validate and convert age to an integer
            try:
                self.age = int(self.age)
                if self.age < 0:
                    raise ValueError("Age must be a positive integer.")
            except ValueError:
                raise ValueError("Age must be a valid integer.")
        else:
            # If age is an empty string, set it to None
            self.age = None

        try:
            self.weight = float(self.weight)
            if self.weight < 0:
                raise ValueError("Weight must be a positive number.")
        except ValueError:
            raise ValueError("Weight must be a valid number.")         

        
        # Validate and format blood pressure
        if self.BP is not None and '/' in str(self.BP).strip():
            # You may want to add more sophisticated validation here
            self.BP = str(self.BP)
        else:
            raise ValueError("Blood pressure must be in the format 'systolic/diastolic'")

      

        super().save(*args, **kwargs)

    
    def __str__(self):
        return self.name
    

    def get_absolute_url(self):
        return reverse('patient_detail', kwargs={'id': self.id}) 

    # def __str__(self):
    #     return f'{self.systolic_pressure}/{self.diastolic_pressure}'


class doctor(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)