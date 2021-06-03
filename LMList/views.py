from django.shortcuts import render, redirect
from django.http import HttpResponse
from LMList.models import Branch, Company

def view_list(request, companyid):
    company_ = Company.objects.get(id=companyid)
    return render(request, 'COMPANY.html', {'companys': company_})

def home_page(request):
    branchs = Branch.objects.all()
    return render(request, 'BRANCH.html',{'branchs' : branchs})

def new_list(request):
    New_Company = Company.objects.create()
    Company.objects.create(hcompany_name =request.POST['Cname'],hdate_establish=request.POST['Destablish'],hcompany_description=request.POST['Cdescription'],hmission=request.POST['mission'],hvission=request.POST['vision'],company_=company_)
    return redirect(f'/LMList/{New_Company.id}/')

def add_item(request, companyid):
    company_ = Company.objects.get(id=companyid)
    Branch.objects.create(bcompany_branch=request.POST['location'],bcompany_address =request.POST['cdescription'],bcontact_number =request.POST['Cnumber'],company_=company_)
    return redirect(f'/LMList/{company.id}/')


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

	company = Company(hcompany_name='iQor', hcompany_address='Quezon City Maginhawa Street')
	company.save()
	res += 'Updating Company entry <br>'

	company = Company.object.get(hcompany_name = 'iQor')
	company.hcompany_address = "Quezon City Maginhawa Street"
	company.save()
	res = ""

	qs = Company.objects.filter(hcompany_name = 'Iqor')
	res += "Found : %s results <br>" %len(qs)

	qs = Company.object.order_by('hcompany_name')
	for x in qs:
		res += x.company_name + x.company_address +'<br>'
























