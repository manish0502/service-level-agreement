from django.db import models


class SLA(models.Model):
    name_of_vendor = models.CharField(max_length=255)
    sla_number = models.CharField(max_length=255, unique=True)
    sla_name = models.CharField(max_length=255)
    sla = models.CharField(max_length=255)
    status = models.IntegerField()


class KPI(models.Model):
    sla_number = models.CharField(max_length=255)
    kpi_read = models.IntegerField()
    next_kpi = models.CharField(max_length=255)


class Rules(models.Model):
    sla_number = models.CharField(max_length=255)
    min = models.DecimalField(max_digits=5, decimal_places=2)
    max = models.DecimalField(max_digits=5, decimal_places=2)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)

