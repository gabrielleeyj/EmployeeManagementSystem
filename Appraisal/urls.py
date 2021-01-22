from django.urls import path
from Appraisal import views

urlpatterns = [
    path('getappraisal',views.getAppraisal,name='getappraisal' ),
    path('getemployeeappaisal',views.getEmployeeAppraisal,name='getemployeeappaisal'),
    path('appraisaldetail',views.appraisaldetail,name='appraisaldetail'),
    path('',views.index,name='home')
]