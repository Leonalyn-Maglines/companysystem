from django.db import models


class Company(models.Model):
	hcompany_name = models.TextField(max_length=15, default='')
	hdate_establish = models.TextField(max_length=10, default='')
	hcompany_description = models.TextField(max_length=60, default='')
	hmission = models.TextField(max_length=80,default='')
	hvision = models.TextField(max_length=80,default='')
	htcompany = models.TextField(max_length=80,default='')
	class meta:
		db_table = "company"

class Branch(models.Model):
	bcompany_branch = models.TextField(max_length=15, default='')
	bcompany_address = models.TextField(max_length=20, default='')
	bcontact_number = models.CharField(default='',max_length=11)
	bemail = models.TextField(default='',max_length=30)
	bphone_number = models.CharField(default='',max_length=11)
	bemail = models.EmailField(default='',max_length=40)
	bcompany = models.ForeignKey(Company, default=None, on_delete=models.CASCADE)
	
	class meta:
		db_table = "branch"

class Employee(models.Model):
	qfull_name = models.TextField(max_length=120, default='')
	qbirthday = models.TextField(max_length=10, default='')
	qage= models.IntegerField( default='')
	qaddress= models.TextField(max_length=20, default='')
	gcollege = models.TextField(max_length=20, default='')
	gsecondary_level = models.TextField(max_length=20, default='')
	gprimary_level = models.TextField(max_length=20, default='')
	gstatus = models.TextField(default='')
	qbranch= models.ForeignKey(Branch, default=None, on_delete=models.CASCADE)
	
	class meta:
		db_table = "employee"

class Background(models.Model):
	gwork_experience = models.TextField(max_length=50,default='')
	gseminars_attended = models.TextField(max_length=50,default='')
	gskills = models.TextField(max_length=50, default='')
	gemployee = models.ForeignKey(Employee, default=None, on_delete=models.CASCADE)
	
	class meta:
		db_table = "background"


class Appointment_Details(models.Model):
	kcontract_details = models.TextField(max_length=20, default='')
	ktermination = models.TextField(max_length=30,default='')
	kpromotions = models.TextField(max_length=30, default='')
	position = models.TextField(max_length=20, default='')
	kemployee = models.ForeignKey(Employee, default=None, on_delete=models.CASCADE)
	
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


