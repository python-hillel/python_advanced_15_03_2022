from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    birthday = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', default='default.png')

    class Meta:
        db_table = 'profile'

    def __str__(self):
        return ''


@receiver(post_save, sender=User)
def create_new_profile(sender, instance, created, **kwargs):
    if created:
        p = Profile(user=instance)
        p.save()
