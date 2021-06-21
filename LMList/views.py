from django.shortcuts import render, redirect
from django.http import HttpResponse
from LMList.models import Branch, Company, Employee, Background, Appointment_Details

def home_page(request):
    companys = Company.objects.all()
    return render(request, 'homepage.html',{'companys' : companys})

def view_list(request, companyid):
    company_ = Company.objects.get(id=companyid)
    return render(request, 'BRANCH.html', {'company': company_})

def form_list(request ):
    return render(request, 'COMPANYY.html' )

def contact_list(request ):
    return render(request, 'CONTACT.html' )

def next_list(request ):
    return render(request, 'BRANCH.html' )

def third_list(request ):
    return render(request, 'EMPLOYEE.html' )

def fourth_list(request ):
    return render(request, '4-5model.html' )

def fifth_list(request ):
  	return render(request, 'about.html' )

def service_list(request ):
  	return render(request, 'services.html' )

def works_list(request ):
  	return render(request, 'howworks.html' )

def homepage_list(request ):
  	return render(request, 'homepage.html' )

def confirmation_list(request ):
  	return render(request, 'LAST.html' )



def new_list(request):
    New_Company = Company.objects.create()
    Company.objects.create(hcompany_name =request.POST['Cname'],hdate_establish=request.POST['Destablish'],hcompany_description=request.POST['Cdescription'],hmission=request.POST['mission'],hvission=request.POST['vision'])
    return redirect(f'/LMList/{New_Company.id}/')

def add_item(request, companyid):
    company_ = Company.objects.get(id=companyid)
    Branch.objects.create(bcompany_branch=request.POST['location'],bcompany_address =request.POST['cdescription'],bcontact_number =request.POST['Cnumber'],company_=company_)
    return redirect(f'/LMList/{company_.id}/')


def dataManipulation(request):
	company = Company(hcompany_name='Cnumber', hdate_establish='Quezon City Maginhawa Street')
	company.save()

	objects = Company.object.all()
	result = 'Printing all Company model : <br>'
	for x in objects:
		res += x.hcompany_name+'<br>'

	CompanyName = Company.objects.get(id = '17')
	res += 'Printing one Company entry <br>'
	res += CompanyName.hcompany_address

	res += '<br> Deleting an Company entry <br>'
	CompanyName.delete()

	company = Company(hcompany_name='iQor', bcompany_address="3rd Floor SM City Dasmariñas, Governor's Dr, Barangay Sampaloc 1, Dasmariñas, 4114 Cavite")
	company.save()
	res += 'Updating Company entry <br>'

	company = Company.object.get(hcompany_name = 'iQor')
	company.hcompany_address = "3rd Floor SM City Dasmariñas, Governor's Dr, Barangay Sampaloc 1, Dasmariñas, 4114 Cavite"
	company.save()
	res = ""

	qs = Company.objects.filter(hcompany_name = 'Iqor')
	res += "Found : %s results <br>" %len(qs)

	qs = Company.object.order_by('hcompany_name')
	for x in qs:
		res += x.company_name + x.company_address +'<br>'
























