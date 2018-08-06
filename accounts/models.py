from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class UserProfile(models.Model):
    gender = {
        ('Men','Nam'),
        ('Women','Nữ')
    }
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='user_profile')
    avatar = models.ImageField(upload_to='accounts',null=True,default='accounts/default.png')
    address =  models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=20)
    birth_day = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=100,choices=gender)

    def __str__(self):
        return self.user.username
    def __unicode__(self):
        return self.user.username
    def get_birth_day(self):
        birth_day = ''
        if self.birth_day:
            birth_day = self.birth_day.strftime('%d / %m / %Y')
        return birth_day

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
post_save.connect(create_user_profile,sender=User)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.UserProfile.save()
