# from django.contrib import admin
# from django.urls import path
# from .views import home


# urlpatterns = [
#     path('', home, name='home')
# ]

# ---------------------------------------------------------------------------------

from django.contrib import admin
from django.urls import path
from .views import home, create_patient, patientcreateview, patientprofileview, patientdeleteview, PatientUpdateView


urlpatterns = [
    # path('login/', login_view, name='login'),
    path('', home, name='home'),
    path('cp/', create_patient, name='create_patient'),
    # path('upload/<str:id>/', upload.as_view(), name='upload'),
    path('createpatient/', patientcreateview.as_view(), name='patient_createview'),   # .as_view tells us that its a class based 
    # path('create/', patientcreateview.as_view(), name='patient_createview'),   # .as_view tells us that its a class based 
    path('update/<str:id>/', PatientUpdateView.as_view(), name='patient_update'),
    path('detail/<str:id>/', patientprofileview.as_view(), name='patient_detail'), #instead of <int:pk> i have used <str:id> which will show the patient detail when id is been put.
    path('delete/<str:id>/', patientdeleteview.as_view(), name='patient_delete'), 

]