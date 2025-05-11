from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, get_object_or_404
from .forms import AppointmentForm
from .models import Medicine, Appointment
from .models import Patient, Visit, TestResult
from django.db import transaction

# Create a dictionary mapping usernames to their corresponding templates
DEPARTMENT_TEMPLATES = {
    'raj': 'cardiology.html',
    'vanshika': 'neurology.html',
    'shambhavi': 'gynecology.html',
}

# Create your views here.
def about(request):
    return render(request, 'about.html')

def appointment(request):
    error = None
    success = None
    
    if request.method == 'POST':
        department = request.POST.get('department')
        doctor = request.POST.get('doctor')
        date = request.POST.get('date')
        time = request.POST.get('time')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Basic validation
        if not all([department, doctor, date, time, name, phone, email]):
            error = "Please fill in all required fields."
        else:
            # Check if the slot is available
            existing_appointment = Appointment.objects.filter(
                doctor=doctor,
                date=date,
                time=time,
                status__in=['confirmed', 'pending']
            ).exists()
            
            if existing_appointment:
                error = "This time slot is already booked. Please choose another time."
            else:
                try:
                    with transaction.atomic():
                        # Create the appointment
                        appointment = Appointment.objects.create(
                            department=department,
                            doctor=doctor,
                            date=date,
                            time=time,
                            name=name,
                            phone=phone,
                            email=email,
                            message=message,
                            status='confirmed'
                        )
                        
                        # Create or update patient record
                        patient, created = Patient.objects.get_or_create(
                            name=name,
                            defaults={
                                'phone': phone,
                                'email': email,
                                'date_of_birth': None,
                                'gender': 'Unknown',
                                'address': '',
                                'medical_history': '',
                                'allergies': '',
                                'ongoing_treatments': ''
                            }
                        )
                        
                        # Create a visit record
                        Visit.objects.create(
                            patient=patient,
                            appointment=appointment,
                            visit_date=date
                        )
                        
                        success = "Your appointment has been successfully booked."
                        return redirect('confirmation')
                        
                except Exception as e:
                    error = "An error occurred while booking your appointment. Please try again."
    
    context = {
        'error': error,
        'success': success
    }
    return render(request, 'appointment.html', context)

def cardio_dept(request):
    return render(request, 'cardio_dept.html')

def confirmation(request):
    return render(request, 'confirmation.html')

def contact(request):
    return render(request, 'contact.html')

def department(request):
    return render(request, 'department.html')

def doctor_single(request):
    return render(request, 'dontor-single.html')

def doctor(request):
    return render(request, 'doctor.html')

def gyno_dept(request):
    return render(request, 'gyno_dept.html')

def index(request):
    return render(request, 'index.html')

def neuro_dept(request):
    return render(request, 'neuro_dept.html')

def pharmacy(request):
    medicines = Medicine.objects.all()  # Fetch all medicines
    return render(request, 'pharmacy.html', {'medicines': medicines})  # Pass medicines to the template

def raj_single(request):
    return render(request, 'raj_single.html')

def service(request):
    return render(request, 'service.html')

def shambhavi_single(request):
    return render(request, 'shambhavi_single.html')

def vanshika_single(request):
    return render(request, 'vanshika_single.html')

def womenhealth(request):
    return render(request, 'womenhealth.html')

@login_required
def department_view(request, department_name):
    # Check if the user has access to the requested department
    template_name = DEPARTMENT_TEMPLATES.get(department_name)
    
    if request.user.username == department_name and template_name:
        # Fetch appointments for the respective department
        cardiology_patients = Appointment.objects.filter(department='Cardiology')
        neurology_patients = Appointment.objects.filter(department='Neurology')
        gynecology_patients = Appointment.objects.filter(department='Gynecology')

        # Depending on the department, pass the appropriate queryset to the template
        if department_name == 'raj':
            context = {'cardiology_patients': cardiology_patients}
        elif department_name == 'vanshika':
            context = {'neurology_patients': neurology_patients}
        elif department_name == 'shambhavi':
            context = {'gynecology_patients': gynecology_patients}

        return render(request, template_name, context)
    else:
        return render(request, 'access_denied.html')


def doctor_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to the doctor's specific page based on their username
            if username == 'raj':
                return redirect('cardiology')  # Use the URL pattern name
            elif username == 'vanshika':
                return redirect('neurology')  # Use the URL pattern name
            elif username == 'shambhavi':
                return redirect('gynecology')  # Use the URL pattern name
    return render(request, 'login.html')  # Render your login page

def patient_profile(request, patient_name):
    # Get patient by name
    patient = get_object_or_404(Patient, name=patient_name)
    
    # Fetch related data
    visits = patient.visits.all()
    test_results = patient.test_results.all()
    
    context = {
        'patient': patient,
        'visits': visits,
        'test_results': test_results,
    }
    return render(request, 'patient_profile.html', context)

def visit_detail(request, visit_id):
    visit = get_object_or_404(Visit, id=visit_id)
    test_results = visit.test_results.all()  # Get all test results for this visit
    
    context = {
        'visit': visit,
        'test_results': test_results,
    }
    return render(request, 'visit_detail.html', context)
