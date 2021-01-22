from django.contrib import admin
from .models import Jobs
# Register your models here.
@admin.register(Jobs)
class JobsAdmin(admin.ModelAdmin):
    list_display = ('job_ID','job_title')