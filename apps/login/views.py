from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

def redirects(request):
    return redirect('/main')


def index(request):
    return render(request, 'login/index.html')


def register(request):
    if request.method == "POST":
        response = User.objects.registation_validator(request.POST, "register")
        if response['status'] == False:
            for error in response['errors']:
                messages.error(request, error)
            return redirect('/main')
        else:
            request.session['user_id'] = response['user'].id
            request.session['user_name'] = response['user'].first_name
            return redirect('/appointments')
    else:
        return render(request, 'login/register.html')


def login(request):
    if request.method == "POST":
        response = User.objects.login_validator(request.POST)
        if response['status'] == False:
            for error in response['errors']:
                messages.error(request, error)
            return redirect('/main')
        else:
            request.session['user_id'] = response['user'].id
            request.session['user_name'] = response['user'].first_name
            return redirect('/appointments')
    else:
        return render(request, 'login/signin.html')


def logout(request):
    del request.session['user_id']
    del request.session['user_name']
    return redirect('/main')


# def success(request):
#     if request.method == "POST":
#         try:
#             request.session['user_id']
#         except KeyError:
#             return redirect('/')
#         context = {'user': User.objects.get(id=request.session['user_id'])}
#         return render(request, 'login/dashboard.html', context)
#     else:
#         return redirect('/')

# def dashboard(request):
#     context = {"user": User.objects.all()}
#     return render(request, 'login/dashboard.html', context)

# def new(request):
#     return render(request, 'login/new.html')

# def edit(request, id):
#     context = {"user": User.objects.get(id=id)}
#     return render(request, 'login/edit.html', context)


# def show(request, id):
#     context = {"user": User.objects.get(id=id)}
#     return render(request, 'login/show.html', context)


# def create(request):
#     errors = User.objects.basic_validator(request.POST)
#     if len(errors):
#         for tag, error in errors.iteritems():
#             messages.error(request, error, extra_tags=tag)
#         return redirect('/users/new')
#     else:
#         user1 = User.objects.create(
#             first_name=request.POST['first_name'],
#             last_name=request.POST['last_name'],
#             email=request.POST['email'],
#         )
#         return redirect('/users/{}'.format(user1.id))


# def destroy(request, id):
#     User.objects.get(id=id).delete()
#     return redirect('/users')


# def update(request, id):
#     errors = User.objects.basic_validator(request.POST)
#     if len(errors):
#         for tag, error in errors.iteritems():
#             messages.error(request, error, extra_tags=tag)
#         return redirect('/users/{}/edit'.format(id))
#     else:
#         if request.method == 'POST':
#             user = User.objects.get(id=id)
#             user.first_name = request.POST['first_name']
#             user.last_name = request.POST['last_name']
#             user.email = request.POST['email']
#             user.save()
#         return redirect('/users/{}'.format(user.id))