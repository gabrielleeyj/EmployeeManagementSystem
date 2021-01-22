from django.db import models
from Department.models import Department
from Jobs.models import Jobs
# Create your models here.

class Employee(models.Model):
    employee_ID = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=15,verbose_name='first name')
    last_name = models.CharField(max_length=15,verbose_name='last name')
    email = models.CharField(max_length=30,verbose_name='email')
    contact = models.CharField(max_length=20,verbose_name='contact')
    adress = models.TextField()
    manager_ID = models.ForeignKey("Appraisal.manager",on_delete=models.CASCADE)
    job_ID = models.ForeignKey(Jobs,on_delete=models.CASCADE)
    department_ID = models.ForeignKey(Department,on_delete=models.CASCADE)
    hire_date=models.DateField(verbose_name='hire date')
    is_activte=models.BooleanField(verbose_name='is active',default=True)

    def __str__(self):
        return (str(self.employee_ID))+'  -  '+(self.first_name+' '+self.last_name)

    class Meta:
        verbose_name='Employee'
        verbose_name_plural='Employees'