from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=250)
    descriptiom = models.TextField()
    city = models.CharField(max_length=250)
    address = models.TextField()
    def to_json(self):
        return {
            'id' : self.id,
            'name' : self.name,
            'descriptiom' : self.descriptiom,
            'city' : self.city,
            'address' : self.address
        }
    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}"

class Vacancy(models.Model):
    name = models.CharField(max_length=250)
    descriptiom = models.TextField()
    salary = models.FloatField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)

    def to_json(self):
        return {
            'id' : self.id,
            'name' : self.name,
            'descriptiom' : self.descriptiom,
            'salary' : self.salary,
            'company_id' : self.company_id,
            'company_name' : self.company.name
        }