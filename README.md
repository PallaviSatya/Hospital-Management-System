# Hospital Management System 🚑

A comprehensive healthcare management solution built with Django, designed to streamline hospital operations and enhance patient care.

## 🏥 Core Features

### Appointment Management
- **Smart Booking System**
  - Multi-department support
  - Real-time availability checking
  - Automated time slot management
  - Instant confirmations
  - Rescheduling capability

### Medical Records System
- **Patient Records**
  - Digital health records
  - Medical history tracking
  - Visit documentation
  - Test results management
  - Prescription records

### Department Management
- **Specialized Departments**
  - Department-specific dashboards
  - Resource allocation
  - Staff scheduling
  - Service management
  - Equipment tracking

### Hospital Operations
- **Pharmacy Management**
  - Digital inventory system
  - Medication tracking
  - Prescription processing
  - Stock alerts
  - Billing integration

- **Communication System**
  - Automated notifications
  - SMS/Email alerts
  - Emergency contact system
  - Internal messaging
  - Support ticketing

- **Analytics & Reporting**
  - Patient statistics
  - Department performance
  - Resource utilization
  - Treatment outcomes
  - Financial reports

##  Technologies Used

- **Backend**: Django 5.1.2
- **Frontend**: Bootstrap, jQuery
- **Database**: SQLite3
- **UI Components**: IcoFont, Slick Carousel
- **Deployment**: PythonAnywhere

## 📱 Screenshots

### Home Page
![Home Page](Hope_Hospitals/public/home%20-%201.png)
*Modern and intuitive interface for users*

### Appointment Management
![Appointment System](Hope_Hospitals/public/appointment.png)
*Streamlined appointment booking process*

### System Administration
![Admin Dashboard](Hope_Hospitals/public/admin-1.png)
*Comprehensive management dashboard*

### Healthcare Provider Interface
![Provider Dashboard](Hope_Hospitals/public/individual-doctor-panel.png)
*Healthcare provider workspace*

### Medical Records
![Medical Records](Hope_Hospitals/public/careful-report-analysis.png)
*Digital medical records system*

### Test Results Management
![Test Results](Hope_Hospitals/public/test-results.png)
*Laboratory results tracking system*

## 🛠️ Installation & Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Hospital-Management-System.git
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

## 🔐 Environment Variables

Create a `.env` file in the root directory with:
```
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```





## 🤝 Contributing

Feel free to make changes and improvements

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

