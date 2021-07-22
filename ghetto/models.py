from django.db import models

class Neighborhood(models.Models):
  name = models.CharField(max_length=200)
  location = models.CharField(max_length=200)
  policehelpline = models.IntegerField(null=False, blank=False)
  hospitalhelpline = models.IntegerField(null=False, blank=False)
  occupants = models.IntegerField(default=0)

  def __str__(self):
    return self.name

  