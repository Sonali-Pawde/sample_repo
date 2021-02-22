from django.shortcuts import render,redirect

# Create your views here.
from .models import Realtor

def index(request):
	realtors = Realtor.objects.all()
	context = {
		'realtors':realtors
	}
	return render(request, 'realtors/realtors.html', context)

def realtor(request,id):
	realtor = Realtor.objects.get(id=id)
	context = {
		'realtor':realtor
	}
	return render(request, 'realtors/realtor.html', context)

from .forms import RealtorForm

def realtor_add(request):
	if request.method == 'POST':
		form = RealtorForm(request.POST, request.FILES)
		if form.is_valid():
			name = request.POST['name']
			photo = request.FILES['photo']
			description = request.POST['description']
			email = request.POST['email']
			phone = request.POST['phone']
			r_obj = Realtor(name=name,photo=photo,description=description,email=email,phone=phone)
			r_obj.save()
			return redirect('realtors')
	else:
		form = RealtorForm()
		return render(request,'realtors/realtor_form.html',{'form':form})

def realtor_update(request,id):
	realtor = Realtor.objects.get(id=id)
	if request.method == 'POST':
		form = RealtorForm(request.POST, request.FILES)
		if form.is_valid():
			realtor.name = request.POST['name']
			realtor.photo = request.FILES['photo']
			realtor.description = request.POST['description']
			realtor.email = request.POST['email']
			realtor.phone = request.POST['phone']
			realtor.save()
			

			return redirect('realtors')
	else:


		initial = {
							'name' : realtor.name,
							'description' : realtor.description,
							'email' : realtor.email,
							'phone': realtor.phone,
							'photo':realtor.photo,
						}
		form = RealtorForm(initial=initial)
		return render(request, 'realtors/realtor_form.html', {'form': form, 'edit': True})


def realtor_delete(request,id):
	realtor = Realtor.objects.get(id=id)
	realtor.delete()
	return redirect('realtors')