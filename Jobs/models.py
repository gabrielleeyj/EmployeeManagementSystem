from django.db import models

# Create your models here.

class Jobs(models.Model):
    job_ID=models.AutoField(primary_key=True)
    job_title=models.CharField(max_length=20,verbose_name='Job Title')

    def __str__(self):
        return (str(self.job_ID))+"  -   "+(self.job_title)

    class Meta:
        verbose_name='Job'
        verbose_name_plural='Jobs'