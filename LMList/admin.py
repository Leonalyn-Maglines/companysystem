from django.contrib import admin
from .models import Company, Branch, Employee, Background, Appointment_Details

admin.site.register(Company)
admin.site.register(Branch)
admin.site.register(Employee)
admin.site.register(Background)
admin.site.register(Appointment_Details)


# Register your models here.
