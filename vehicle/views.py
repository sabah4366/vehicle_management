from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import VehicleForm
from account.models import User
from .models import Vehicle

# Create your views here.
#user access views logic are used in templates


@login_required(login_url='signin')
def home(request):
    vehicles=Vehicle.objects.all()

    return render(request,'vehicle/home.html',{'vehicles':vehicles})



@login_required(login_url='signin')
def vehicle_create(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = VehicleForm()
    return render(request, 'vehicle/vehicle_create.html', {'form': form})



@login_required(login_url='signin')
def vehicle_update(request,pk):
    vehicle=get_object_or_404(Vehicle,pk=pk)
    
    if request.method == "POST":
        form=VehicleForm(request.POST,instance=vehicle)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = VehicleForm(instance=vehicle)
    return render(request,'vehicle/vehicle_update.html',{'form': form, 'vehicle': vehicle})


@login_required(login_url='signin')
def delete_vehicle(request,pk):
    vehicle=get_object_or_404(Vehicle,pk=pk)
    vehicle.delete()
    return redirect('home')


