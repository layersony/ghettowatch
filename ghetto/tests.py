from django.test import TestCase
from .models import Business, Location, Profile, Neighborhood, Postii
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
    self.hood = Neighborhood.objects.create(name='Kisumu Ndogo', location=self.location, policehelpline=2, hospitalhelpline=2, occupants=8)


  def tearDown(self):
    Location.objects.all().delete()
    Neighborhood.objects.all().delete()

  def test_isinstance(self):
    self.assertTrue(isinstance(self.hood, Neighborhood))

  def test_deletehood(self):
    self.hood2 = Neighborhood.objects.create(name='Embakasi', location=self.location, policehelpline= 2, hospitalhelpline=4, occupants=8)
    self.assertEqual(len(Neighborhood.objects.all()),2)
    Neighborhood.delete_neigborhood(self.hood.id)
    self.assertEqual(len(Neighborhood.objects.all()),1)

  def test_findneighborhood(self):
    searchterm = 'Embakasi'
    self.hood2 = Neighborhood.objects.create(name='Embakasi', location=self.location, policehelpline= 2, hospitalhelpline=4, occupants=8)
    results = Neighborhood.find_neigborhood(searchterm)
    self.assertTrue(len(results), 1)

  def test_updateneighbor(self):
    self.hood2 = Neighborhood.objects.create(name='Embakasi', location=self.location, policehelpline= 2, hospitalhelpline=4, occupants=8)
    Neighborhood.update_neighborhood(self.hood2.id, name='kajiado')
    updated = Neighborhood.objects.get(id = self.hood2.id)
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

class TestBusiness(TestCase):
  def setUp(self):
    self.location = Location.objects.create(location='Machakos')
    self.newuser = User.objects.create(username = 'layersony')
    self.hood = Neighborhood.objects.create(name='Kisumu Ndogo', location=self.location, policehelpline=2, hospitalhelpline=2, occupants=8)
    self.business = Business.objects.create(businessname = 'trial1', description='description for trial1', email='sammaingi5@gmail.com', username=self.newuser, neighborhood=self.hood)

  def tearDown(self):
    User.objects.all().delete()
    Neighborhood.objects.all().delete()
    Business.objects.all().delete()

  def test_isinstance(self):
    self.assertTrue(isinstance(self.business, Business))  

  def test_save_business(self):
    self.business2 = Business.objects.create(businessname = 'trial2', description='description for trial2', email='sammaingi5@gmail.com', username=self.newuser, neighborhood=self.hood)
    self.assertEqual(len(Business.objects.all()), 2)


  def test_delete_business(self):
    self.business2 = Business.objects.create(businessname = 'trial2', description='description for trial2', email='sammaingi5@gmail.com', username=self.newuser, neighborhood=self.hood)
    self.assertEqual(len(Business.objects.all()), 2)
    Business.delete_business(self.business2.id)
    self.assertEqual(len(Business.objects.all()), 1)

  def test_searchbusiness(self):
    self.business2 = Business.objects.create(businessname = 'trial2', description='description for trial2', email='sammaingi5@gmail.com', username=self.newuser, neighborhood=self.hood)
    searchterm = 'trial2'
    searchresults = Business.searchbusiness(searchterm)
    self.assertEqual(len(searchresults), 1)


class Post(TestCase):
  def setUp(self):
    self.location = Location.objects.create(location='Machakos')
    self.hood = Neighborhood.objects.create(name='Kisumu Ndogo', location=self.location, policehelpline='00022233211', hospitalhelpline='0092133313', occupants=8)
    self.post = Postii.objects.create(posttitle='theives found', story='wezi wa tatu walipatikana', neighborhood=self.hood)

  def tearDown(self):
    Location.objects.all().delete()
    User.objects.all().delete()
    Neighborhood.objects.all().delete()
    Postii.objects.all().delete

  def test_isinstance(self):
    self.assertTrue(isinstance(self.post, Postii))

  def test_save_post(self):
    self.post2 = Postii.objects.create(posttitle='wezi walipatikana ', story='thieves were found', neighborhood=self.hood)
    self.assertEqual(len(Postii.objects.all()), 2)

  def test_delete_post(self):
    self.post2 = Postii.objects.create(posttitle='wezi walipatikana ', story='thieves were found', neighborhood=self.hood)
    self.assertEqual(len(Postii.objects.all()), 2)
    Postii.delete_post(self.post2.id)
    self.assertEqual(len(Postii.objects.all()), 1)