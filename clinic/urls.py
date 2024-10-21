from django.contrib import admin
from django.urls import path
from .views import home, create_patient, patientcreateview, patientprofileview, patientdeleteview, PatientUpdateView
from django.contrib.auth.views import LoginView  # Import Django's built-in LoginView

urlpatterns = [
    path('', LoginView.as_view(template_name='registration/login.html')),  # Set the login view as the homepage
    path('dashboard/', home, name='home'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),  # Optional: Keep the login URL
    path('cp/', create_patient, name='create_patient'),
    # path('upload/<str:id>/', upload.as_view(), name='upload'),
    path('createpatient/', patientcreateview.as_view(), name='patient_createview'),   # .as_view tells us that its a class based 
    # path('create/', patientcreateview.as_view(), name='patient_createview'),   # .as_view tells us that its a class based 
    path('update/<str:id>/', PatientUpdateView.as_view(), name='patient_update'),
    path('detail/<str:id>/', patientprofileview.as_view(), name='patient_detail'), #instead of <int:pk> i have used <str:id> which will show the patient detail when id is been put.
    path('delete/<str:id>/', patientdeleteview.as_view(), name='patient_delete'), 

]