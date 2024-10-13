# from django.shortcuts import render

# from django.http import HttpResponse

# # Create your views here.

# def home(request):
#     return HttpResponse('helloworld')

# -----------------------------------------------------------------------------------------------------



from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic import UpdateView
from django.http import Http404, HttpResponseRedirect
# from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy, reverse
from django.views.generic import DeleteView

# from .forms import PatientForm
from .forms import PatientUpdateForm

#models
from .models import patient

# Create your views here.

# doctor_data = None

# def index(request):
#     data = doctor.objects.all()
#     shopkeeper_data = {
#         "username": data[0].username, 
#         "password": data[0].password, 
#     }
        
#     if request.POST:
#         print(request.POST)
#         username = request.POST['UserName']
#         password = request.POST['password']
#         if username == doctor_data['username'] and password == doctor_data['password']:
#             return redirect('/doctor')
            
        
#     return render(request ,"clinic\Login.html")



def create_patient(request):
    if request.method == 'POST':
        form = PatientUpdateForm(request.POST)
        if form.is_valid():
            print("Form is valid!")
            patient = form.save()
            print("Model instance saved:", patient)
            return redirect('create_patient')
            # return redirect('patient_list')
    else:
        form = PatientUpdateForm()
    return redirect(request, 'clinic/patient_createview.html', {'form': form})
    # return reverse(request, 'clinic/home.html', {'form': form})



def home(request):
    template_name='clinic/home.html'
    context= {
        'patient':patient.objects.all(),
    }
    return render(request,
                  template_name= template_name,
                  context= context)

class patientcreateview(CreateView):
    model = patient
    fields = '__all__'
    template_name = 'clinic/patient_createview.html'
    # context_object_name ='patient'

    def form_valid(self, form):
        print("Form is valid!")
        self.object = form.save()
        print("Model instance saved:", self.object)
        return super().form_valid(form)
    
    def form_invalid(self, form):
        print("Form is invalid")
        print(form.errors)
        return super().form_invalid(form)
    

    def get_success_url(self):
        # print("Getting success URL...")
        return reverse('patient_detail', kwargs={'id': str(self.object.id)})   # and if i would have used pk then  kwargs = {'pk': self.object.pk}
    

class patientprofileview(DetailView):
    model = patient
    template_name = 'clinic/patient_detail.html'    #'clinic/patient_createview.html'
    context_object_name ='patient'
    slug_field = 'id'

    def get_object(self, queryset=None):
        id = self.kwargs.get('id')
        return self.model.objects.get(id=id)
    


class PatientUpdateView(UpdateView):
    model = patient
    form_class = PatientUpdateForm
    template_name = 'clinic/patient_update.html'  # Template for update form
    context_object_name = 'patient'  # Name to use in the template for the patient object
    # success_url = reverse_lazy('patient_detail')  # Specify the URL to redirect to after successful update

    def form_valid(self, form):
        print("Form is valid!")
        self.object = form.save()
        print("Model instance updated:", self.object)
        return super().form_valid(form)

    def get_success_url(self):
        print("Getting success URL...")
        # Assuming 'patient_detail' is the name of your patient detail view
        return reverse_lazy('patient_detail', kwargs={'id': self.object.id})


    def get_object(self, queryset=None):
        id = self.kwargs.get('id')
        print("Getting object with id:", id)
        try:
            patient = self.model.objects.get(id=id)
        except self.model.DoesNotExist:
            raise Http404("Patient does not exist")
        return patient
        

def my_view(request):       #This is for update view redirection
    # Your view logic here
    id = request.kwargs.get('id')  # Replace with the actual patient ID
    return HttpResponseRedirect(reverse('patient_detail', kwargs={'id': id}))

    

class patientdeleteview(DeleteView):
    model = patient
    template_name = 'clinic/patient_delete.html'  # Template for confirmation
    success_url = reverse_lazy('home')   # URL to redirect after deletion

    def get_object(self, queryset=None):
        id = self.kwargs.get('id')
        return self.model.objects.get(id=id)

