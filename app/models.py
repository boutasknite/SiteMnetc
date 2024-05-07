from django.db import models


class Thrust(models.Model):
    Name = models.CharField(max_length=100)
    Description = models.CharField(max_length=500)
    Image = models.ImageField(upload_to='thrusts/')

    def __str__(self):
        return self.Name


class Member(models.Model):
    First_Name = models.CharField(max_length=100)
    Second_Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=200, blank=True, null=True)
    Phone_Number = models.CharField(max_length=100,blank=True, null=True)
    Affiliation = models.CharField(max_length=100, blank=True, null=True)
    Research_Area = models.CharField(max_length=100, blank=True, null=True)
    Position = models.CharField(max_length=100, blank=True, null=True)
    CV = models.FileField(null=True, blank=True, upload_to='CV/')
    Motivation = models.TextField(default="", blank=True)
    Contribution = models.TextField(default="", blank=True)
    References = models.TextField(default="", blank=True)
    Biography = models.TextField(default="")
    Location = models.CharField(max_length=100)
    Image = models.ImageField(upload_to='Members_Photos/')

    def __str__(self):
        return f"{self.First_Name} {self.Second_Name}"


class Demand(models.Model):
    First_Name = models.CharField(max_length=100)
    Second_Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=200)
    Phone_Number = models.CharField(max_length=100)
    Affiliation = models.CharField(max_length=100)
    Research_Area = models.CharField(max_length=100)
    Position = models.CharField(max_length=100)
    CV = models.FileField( upload_to='CV/')
    Motivation = models.TextField(default="")
    Contribution = models.TextField(default="")
    References = models.TextField(default="")

    def __str__(self):
        return f"{self.First_Name} {self.Second_Name}"


