from django.urls import path
from customer import views

urlpatterns = [
    path('home/', views.home, name='customer_home'),
    path('vendor_requests_list', views.VendorApproveList.as_view(), name='vendor_approve_list'),
    path('vender_approve/<int:pk>', views.vendor_accept, name='vendor_approve'),
    path('vender_reject/<int:pk>', views.vendor_reject, name='vendor_reject'),
    path('vendor_approved_list', views.VendorApprovedList.as_view(), name='vendor_approved_list'),
    path('vendor_rejected_list', views.VendorRejectedList.as_view(), name='vendor_rejected_list'),
    path('addsla/', views.addsla, name='addsla'),
    path('sla_list', views.SlaList.as_view(), name='sla_list'),
    path('addkpi/', views.addkpi, name='add_kpi'),
    path('kpi_list', views.KPIList.as_view(), name='kpi_list'),
]
