from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from user.models import User
from customer.models import SLA, Rules, KPI
import requests


def home(request):
    response = requests.get('https://jsonplaceholder.typicode.com/posts/3')
    print(response)
    print(response.text)
    employee = response.json()
    print(employee['id'])
    return render(request, 'customer/chome.html', {
        'id': employee['id'],'title':employee['title'], 'body':employee['body']
    })


class VendorApproveList(ListView):
    model = User
    template_name = 'customer/pending_requests.html'

    def get_queryset(self):
        query = super().get_queryset()
        vendors = query.filter(is_active=0, reject=0)
        return vendors


def vendor_accept(request, pk):
    user = User.objects.get(pk=pk)
    user.is_active = 1
    user.save()
    return redirect('vendor_approve_list')


def vendor_reject(request, pk):
    user = User.objects.get(pk=pk)
    user.reject = 1
    user.save()
    return redirect('vendor_approve_list')


class VendorApprovedList(ListView):
    model = User
    template_name = 'customer/approved_vendors.html'

    def get_queryset(self):
        query = super().get_queryset()
        vendors = query.filter(is_active=1, reject=0)
        return vendors


class VendorRejectedList(ListView):
    model = User
    template_name = 'customer/rejected_vendors.html'

    def get_queryset(self):
        query = super().get_queryset()
        vendors = query.filter(is_active=0, reject=1)
        return vendors


def addsla(request):
    vendors = User.objects.filter(user_type="vendor")
    context = {"vendors": vendors}
    print(request.POST)
    if request.method == 'POST':
        name_of_vendor = request.POST['name']
        sla_number = request.POST['sla_number']
        if SLA.objects.filter(sla_number=sla_number).exists():
            context = {"error": "sla is already exists"}
            return render(request, 'customer/addsla.html', context)
        sla_name = request.POST['sla_name']
        sla = request.POST['sla']
        sla = SLA(name_of_vendor=name_of_vendor, sla_number=sla_number, sla_name=sla_name, sla=sla, status=0)
        sla.save()
        context = {'sucess': 'SLA  has been Submited Sucessfully'}
        no_of_rules = request.POST['no_of_rules']
        print(no_of_rules)
        for i in range(1, int(no_of_rules)+1):
            min = request.POST['min'+str(i)]
            max = request.POST['max'+str(i)]
            percentage = request.POST['percentage'+str(i)]
            rules = Rules(min=min, max=max, percentage=percentage, sla_number=sla_number)
            rules.save()
            print("its saving")
        return render(request, 'customer/addsla.html', context)

    return render(request, 'customer/addsla.html', context)


class SlaList(ListView):
    model = SLA
    template_name = 'customer/ viewSLA.html'

    def get_queryset(self):
        query = super().get_queryset()
        slas = query.filter(status=1)
        return slas


def addkpi(request):
    sla = SLA.objects.filter()
    context = {"sla": sla}
    if request.method == 'POST':
        sla_number = request.POST['sla_number']
        kpi_read = request.POST['kpi_read']
        next_kpi = request.POST['next_kpi']
        kpi = KPI(sla_number=sla_number, kpi_read=kpi_read, next_kpi=next_kpi)
        kpi.save()
        context = {'sucess': 'KPI  has been Submited Sucessfully'}
        return render(request, 'customer/addkpi.html', context)

    return render(request, 'customer/addkpi.html', context)


class KPIList(ListView):
    model = KPI
    template_name = 'customer/viewKPI.html'

    def get_queryset(self):
        query = super().get_queryset()
        kpis = query.filter()
        return kpis

