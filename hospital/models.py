from django.db import models

class Appointment(models.Model):
    department = models.CharField(max_length=100)
    doctor = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    message = models.TextField()
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled')
    ], default='pending')

    def __str__(self):
        return f"Appointment with {self.doctor} on {self.date} at {self.time}"
    
    @classmethod
    def check_availability(cls, doctor, date, time):
        return not cls.objects.filter(
            doctor=doctor,
            date=date,
            time=time,
            status='confirmed'
        ).exists()
    
    
class Patient(models.Model):
    name = models.CharField(max_length=200, unique=True)  # Combined name field
    date_of_birth = models.DateField(null=True, blank=True)  # Allow null and blank values
    gender = models.CharField(max_length=10, null=True, blank=True)  # Allow null and blank values
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    medical_history = models.TextField(blank=True, null=True)
    allergies = models.TextField(blank=True, null=True)
    ongoing_treatments = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name  # Use the combined name field
    
    
class Visit(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='visits')
    appointment = models.ForeignKey(Appointment, on_delete=models.SET_NULL, null=True, related_name='visits')
    visit_date = models.DateField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Visit for {self.patient.name} on {self.visit_date}"

class TestResult(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='test_results')
    visit = models.ForeignKey(Visit, on_delete=models.SET_NULL, null=True, related_name='test_results')
    test_name = models.CharField(max_length=100)
    upload_date = models.DateField(auto_now_add=True)
    result_file = models.FileField(upload_to='test_results/')

    def __str__(self):
        return f"Test Result: {self.test_name} for {self.patient.name}"

class Medicine(models.Model):
    name = models.CharField(max_length=100)
    availability = models.BooleanField(default=True)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name
