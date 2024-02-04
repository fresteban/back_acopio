from django.db import models

class Center(models.Model):
    id_center = models.AutoField(primary_key=True)
    center_name = models.CharField(max_length=30)
    center_available = models.BooleanField()


class Address(models.Model):
    id_address = models.AutoField(primary_key=True)
    address_region = models.CharField(max_length=30)
    address_locality = models.CharField(max_length=30)
    address_street = models.CharField(max_length=30)
    address_number = models.IntegerField()
    center_address = models.ForeignKey('Center', on_delete=models.CASCADE, null=True)

class Donation(models.Model):
    id_donation = models.AutoField(primary_key=True)
    donation_type = models.CharField(max_length=30)
    donation_name = models.CharField(max_length=30)
    donor = models.ForeignKey('Donor', on_delete=models.CASCADE)
    center_donation = models.ForeignKey('Center', on_delete=models.CASCADE, null=True)

class Donor(models.Model):
    id_Donor = models.AutoField(primary_key=True)
    donor_name = models.CharField(max_length=30)
    donor_rut = models.CharField(max_length=30)
    donor_email = models.CharField(max_length=30)
    donor_phone = models.CharField(max_length=30)