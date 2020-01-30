from django.shortcuts import render, redirect
from user.models import User
from django.contrib.auth import authenticate


def register(request):
    if request.method == 'POST':
        company_name = request.POST['company_name']
        email = request.POST['email']
        max_id = User.objects.last()
        username = company_name[0:3].upper()+str((max_id.id+1))
        contact_person = request.POST['contact_person']
        mobile = request.POST['mobile']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                print("Username taken")
            elif User.objects.filter(email=email).exists():
                print("Email taken")
            else:
                user = User.objects.create_user(username=username, password=password1, email=email,
                                                company_name=company_name,
                                                contact_person=contact_person, mobile=mobile, user_type="vendor")
                user.save()
                print("User Created")
                redirect('loginview')
        else:
            print("User Not created")

        return redirect('/')

    else:
        return render(request, 'user/register1.html')


def loginview(request):
    if request.method == 'POST':
        password = request.POST['password']
        email = request.POST['email']
        user = authenticate(username=email, password=password)
        if user is not None:
            if user.user_type == "vendor":
                return redirect('vendor_home')
            elif user.user_type == "customer":
                return redirect('customer_home')
        else:
            return render(request, 'user/login.html', {'error':'Invalid credentials'})
    else:
        return render(request, 'user/login.html')