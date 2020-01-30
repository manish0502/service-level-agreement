from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from user.models import User
from customer.models import SLA, Rules, KPI


def home(request):
    return render(request, 'vendor/vhome.html')

class SlaApproveList(ListView):
    model = SLA
    template_name = 'vendor/sla_pending_requests.html'

    def get_queryset(self):
        query = super().get_queryset()
        slas = query.filter(status=0)
        return slas

def sla_accept(request, pk):
    user = SLA.objects.get(pk=pk)
    user.status = 1
    user.save()
    return redirect('sla_approve_list')


def sla_reject(request, pk):
    user = SLA.objects.get(pk=pk)
    user.status = 2
    user.save()
    return redirect('sla_approve_list')
class SlaApprovedList(ListView):
    model = SLA
    template_name = 'vendor/approved_sla.html'

    def get_queryset(self):
        query = super().get_queryset()
        slas = query.filter()
        return slas


class SlaRejectedList(ListView):
    model = SLA
    template_name = 'vendor/rejected_sla.html'

    def get_queryset(self):
        query = super().get_queryset()
        slas = query.filter()
        return slas