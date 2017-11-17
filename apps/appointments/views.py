from django.shortcuts import render, redirect
from ..login.models import User
from .models import Appointment
from datetime import datetime
from django.contrib import messages
import operator


def index(request):
    if 'user_id' not in request.session:
        return redirect('/')
    today = datetime.now().strftime("%Y-%m-%d")
    user = User.objects.get(id=request.session['user_id'])
    context = {'app': Appointment.objects.order_by('time').filter(user=user)}
    return render(request, 'appointments/index.html', context, today)


def edit(request, id):
    if 'user_id' not in request.session:
        return redirect('/')

    context = {'app': Appointment.objects.get(id=id)}
    return render(request, 'appointments/edit.html', context)


def update(request, id):
    response = Appointment.objects.appointment_validator(request.POST)
    if response['status'] == True:
        print "!!!!!"
        app = Appointment.objects.get(id=id)
        app.task = request.POST['task']
        # app.date = request.POST['date']
        app.time = request.POST['time']
        app.status = request.POST['status']
        app.save()
        return redirect('/appointments')
    else:
        for error in response['errors']:
            messages.error(request, error)
        return redirect('/appointments/{}'.format(id))


def add(request):
    response = Appointment.objects.appointment_validator(request.POST)
    if response['status'] == True:
        user = User.objects.get(id=request.session['user_id'])
        app = Appointment.objects.create(
            task=request.POST['task'],
            status="pending",
            time=request.POST['time'],
            date=request.POST['date'],
            user=user,
        )
        return redirect('/appointments')
    else:
        for error in response['errors']:
            messages.error(request, error)
        return redirect('/appointments')


def destroy(request, id):
    Appointment.objects.get(id=id).delete()
    return redirect('/appointments')


def logout(request):
    request.session.clear()
    return redirect('/home')
