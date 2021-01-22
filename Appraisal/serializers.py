from .models import Appraisal
from rest_framework import serializers



class AppraisalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appraisal
        fields = ['appraisal_ID', 'objective', 'year', 'department_ID','employee_ID','rating']