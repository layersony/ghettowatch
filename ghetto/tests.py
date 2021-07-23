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

  def test_save_location(self):
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

  def test_deletehood(self):
    self.hood2 = Neighborhood.objects.create(name='Embakasi', location=self.location, policehelpline='00022233211', hospitalhelpline='0092133313', occupants=8)
    self.assertEqual(len(Neighborhood.objects.all()),2)
    Neighborhood.delete_neigborhood(self.hood.id)
    self.assertEqual(len(Neighborhood.objects.all()),1)

  def test_findneighborhood(self):
    searchterm = 'Embakasi'
    self.hood2 = Neighborhood.objects.create(name='Embakasi', location=self.location, policehelpline='00022233211', hospitalhelpline='0092133313', occupants=8)
    results = Neighborhood.find_neigborhood(searchterm)
    self.assertTrue(len(results), 1)

  def test_updateneighbor(self):
    self.hood2 = Neighborhood.objects.create(name='Embakasi', location=self.location, policehelpline='00022233211', hospitalhelpline='0092133313', occupants=8)
    updated = Neighborhood.update_neighborhood(self.hood2.id, name='kajiado')
    self.assertEqual(updated.name, 'kajiado')

class TestProfile(TestCase):
  def setUp(self):
    self.newuser = User(username = "maingi")
    self.newuser.save()
    self.location = Location.objects.create(location='Machakos')
    self.hood = Neighborhood.objects.create(name='Kisumu Ndogo', location=self.location, policehelpline= 2, hospitalhelpline=4, occupants=8)
    self.newprofile = Profile.objects.create(profilePic='test.jpg', bio='i am amazing', phone=2, location=self.location, neighborhood=self.hood )

  def tearDown(self):
    Profile.objects.all().delete()
    User.objects.all().delete()
    Neighborhood.objects.all().delete()
    Location.objects.all().delete

  def test_isinstance(self):
    self.assertTrue(isinstance(self.newprofile, Profile))

