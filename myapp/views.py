from django.shortcuts import render, redirect
from .models import TrafficViolations
from django.contrib import messages
from .forms import TrafficViolationsForm
from django.http import HttpResponse



# Create your views here.
def index(request):
    return render(request, "myapp/index.html", {})


def navbar(request):
    return render(request, "myapp/navbar.html", {})


def userreg(request):
    return render(request, "myapp/userreg.html", {})


def insertuser(request):
    vuviolation_id = request.POST.get('tuviolation_id', '')
    vudriver_id = request.POST.get('tudriver_id', '')
    vuvehicle_id = request.POST.get('tuvehicle_id', '')
    vucamera_id = request.POST.get('tucamera_id', '')
    vuviolation_type = request.POST.get('tuviolation_type', '')
    vufine_amount = request.POST.get('tufine_amount', '')
    vuviolation_date = request.POST.get('tuviolation_date', '')
    vuviolation_time = request.POST.get('tuviolation_time', '')
    vupenalty_points = request.POST.get('tupenalty_points', '')
    vulocation = request.POST.get('tulocation', '')
    us = TrafficViolations(violation_id= vuviolation_id, driver_id=vudriver_id,vehicle_id=vuvehicle_id,camera_id=vucamera_id,violation_type= vuviolation_type, fine_amount =vufine_amount, violation_date= vuviolation_date, violation_time= vuviolation_time,penalty_points=vupenalty_points, location = vulocation);
    us.save();
    return render(request, 'myapp/index.html', {})


def insertuser1(request):
    if request.method == 'POST':
        form = TrafficViolationsForm(request.POST)
        if form.is_valid():
            form.save()  # Saves the traffic violation to the database
            messages.success(request, "Traffic violation recorded successfully!")
            return redirect('index')  # Redirect to avoid resubmission on page refresh
        else:
            messages.error(request, "There was an error in your submission. Please correct the errors below.")
    else:
        form = TrafficViolationsForm()  # Initialize an empty form for GET request
    return render(request, 'myapp/traffic_violation_form.html', {'form': form})


def viewusers(request):
    user=TrafficViolations.objects.all()
    return render(request,"myapp/viewusers.html",{"userdata":user})

def deleteprofile(request, id):
    print(f"Received violation ID: {id}")
    us=TrafficViolations.objects.filter(violation_id=id)
    us.delete()
    return redirect("/viewusers")

def editprofile(request, id):
    user=TrafficViolations.objects.get(violation_id=id)
    return render(request,"myapp/editprofile.html",{"user":user})


def updateprofile(request, id):
    newviolation_id = request.POST['violation_id']
    newviolation_type = request.POST['violation_type']
    newfine_amount = request.POST['fine_amount']
    newviolation_date = request.POST['violation_date']
    newviolation_time = request.POST['violation_time']
    newlocation = request.POST['location']

    user=TrafficViolations.objects.get(violation_id=id)
    user.violation_id = newviolation_id
    user.violation_type = newviolation_type
    user.fine_amount = newfine_amount
    user.violation_date = newviolation_date
    user.violation_time = newviolation_time
    user.location = newlocation
    user.save()
    return redirect("/viewusers")


def traffic_violations_view(request):
    # Query to retrieve all traffic violations over $100 fine amount
    violations = TrafficViolations.objects.filter(fine_amount__gt=1000).select_related('driver', 'vehicle', 'camera')

    # Formatting data for the template
    violation_data = [
        {
            'violation_id': violation.violation_id,
            'violation_type': violation.violation_type,
            'fine_amount': violation.fine_amount
        }
        for violation in violations
    ]

    return render(request, 'myapp/traffic_violations.html', {'violation_data': violation_data})

