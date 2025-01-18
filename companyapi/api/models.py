from django.db import models

# Create your models here.

#Company models created here

class Company(models.Model):
    company_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    about=models.TextField()
    type=models.CharField(max_length=100,choices=(('IT','IT'),
                                                  ('NON IT','NON IT'),
                                                  ('MP','MP')
                                                  ))
    added_date=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.name
#Employee Model 

class Employee(models.Model):
    name=models.CharField(max_length=100)
    email_id=models.CharField(max_length=50)
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
    about=models.TextField(max_length=100)
    position=models.CharField(max_length=50,choices=(
        ('MG','Manager'),
        ('SDE','Software Developer'),
        ('PL','Project Lead')
    ))
    
    company=models.ForeignKey(Company,on_delete=models.CASCADE)