from django.test import TestCase
from .models import Location, Post, Profile, Neighborhood
from django.contrib.auth.models import User

class TestLocation(TestCase):
  def setUp(self):
    self.location = Location.objects.create(location='Machakos')

  def tearDown(self):
    Location.objects.all().delete()

  def test_isinstance(self):
    self.assertTrue(isinstance(self.location, Location))

  def save_location(self):
    self.location2 = Location.objects.create(location='Nairobi')
    self.assertEqual(len(Location.objects.all()), 2)

class TestNeighborhodd(TestCase):
  def setUp(self):
    self.location = Location.objects.create(location='Machakos')
    self.hood = Neighborhood.objects.create(name='Kisumu Ndogo', location=self.location, policehelpline='00022233211', hospitalhelpline='0092133313', occupants=8)


  def tearDown(self):
    Location.objects.all().delete()
    Neighborhood.objects.all().delete()

  def test_isinstance(self):
    self.assertTrue(isinstance(self.hood, Neighborhood))
