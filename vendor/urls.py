from django.urls import path
from vendor import views

urlpatterns = [
    path('home/', views.home, name='vendor_home'),
    path('sla_requests_list', views.SlaApproveList.as_view(), name='sla_approve_list'),
    path('sla_approve/<int:pk>', views.sla_accept, name='sla_approve'),
    path('sla_reject/<int:pk>', views.sla_reject, name='sla_reject'),
    path('sla_approved_list', views.SlaApprovedList.as_view(), name='sla_approved_list'),
    path('sla_rejected_list', views.SlaRejectedList.as_view(), name='sla_rejected_list'),
]
