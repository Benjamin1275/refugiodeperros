from django.db import models
from django.urls import reverse


class Shelter(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    id = models.BigAutoField(primary_key=True)  # Tipo de campo para bd, se utiliza
    # como primary key y nos ayuda a almacenar un numero y permite que la pk pueda
    # almacenar numeros más grandes

    def __str__(self):
        return self.name


class Dog(models.Model):
    shelter = models.ForeignKey(Shelter, on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    description = models.TextField()
    intake_date = models.DateTimeField(auto_now_add=True)
    id = models.BigAutoField(primary_key=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('dog_detail', args=[str(self.id)])