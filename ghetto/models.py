from django.db import models

class Neighborhood(models.Models):
  name = models.CharField(max_length=200)
  location = models.CharField(max_length=200)
  policehelpline = models.IntegerField(null=False, blank=False)
  hospitalhelpline = models.IntegerField(null=False, blank=False)
  occupants = models.IntegerField(default=0)

  def __str__(self):
    return self.name

class Profile(models.Model):
  username = models.OneToOneField(User, on_delete=models.CASCADE)
  bio = models.TextField()
  phone = models.IntegerField()
  profilePic = models.ImageField(upload_to='userProfile/', default='userProfile/test.png')
  location = models.ForeignKey(Location, on_delete=models.SET_NULL)
  neighborhood = models.ForeignKey(Neighborhood, on_delete=models.SET_NULL, null=False, blank=False)

  @receiver(post_save, sender=User)
  def create_user_profile(sender, instance, created, **kwargs):
      if created:
          Profile.objects.create(user=instance)


  @receiver(post_save, sender=User)
  def save_user_profile(sender, instance, **kwargs):
      instance.profile.save()