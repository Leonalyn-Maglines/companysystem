from django.db import models


class Company(models.Model):
	hcompany_name = models.TextField(default='')
	hdate_establish = models.TextField(default='')
	hcompany_description = models.TextField(default='')
	hmission = models.TextField(default='')
	hvission = models.TextField(default='')
	
	class meta:
		db_table = "company"

class Branch(models.Model):
	bcompany_branch = models.TextField(default='')
	bcompany_address = models.TextField(default='')
	bcontact_number = models.TextField(default='')
	bcompany = models.ForeignKey(Company, default=None, on_delete=models.PROTECT)
	
	class meta:
		db_table = "branch"

class Employee(models.Model):
	qfull_name = models.TextField(default='')
	qage = models.TextField(default='')
	qaddress= models.TextField(default='')
	gcollege = models.TextField(default='')
	gsecondary_level = models.TextField(default='')
	gprimary_level = models.TextField(default='')
	qbranch= models.ForeignKey(Branch, default=None, on_delete=models.PROTECT)
	
	class meta:
		db_table = "employee"

class Background(models.Model):
	gwork_experience = models.TextField(default='')
	gseminars_attended = models.TextField(default='')
	gskills = models.TextField(default='')
	gemployee = models.ForeignKey(Employee, default=None, on_delete=models.PROTECT)
	
	class meta:
		db_table = "background"


class Appointment_Details(models.Model):
	kcontract_details = models.TextField(default='')
	ktermination = models.TextField(default='')
	kpromotions = models.TextField(default='')
	position = models.TextField(default='')
	kemployee = models.ForeignKey(Employee, default=None, on_delete=models.PROTECT)
	
	class meta:
		db_table = "appoinment"



'''class List(models.Model):
    npet = models.TextField(default='')
    nname = models.TextField(default='')


class Item(models.Model):
    npet = models.TextField(default='')
    nname = models.TextField(default='')
    nAddress = models.TextField(default='')
    nBreed = models.TextField(default='')
    nDay = models.TextField(default='') 
    list = models.ForeignKey(List, default=None, on_delete=models.PROTECT)'''


