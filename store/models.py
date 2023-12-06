from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class District(models.Model):
    city = models.ForeignKey(City, related_name='districts', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        ordering = ['name']