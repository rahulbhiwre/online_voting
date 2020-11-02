from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
import pickle
from phe import paillier



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    phone_number = models.CharField(max_length=12, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    voted = models.BooleanField(default=False)

    def __str__(self):
        return '%s' % (self.user.username)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    try:
        instance.profile.save()
    except ObjectDoesNotExist:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    #User._meta.get_field('email')._unique = True


class Poll(models.Model):
    pickle_in2=open("sum.pickle","rb")

    sum_total=pickle.load(pickle_in2)

    

    
    def on_going(self,sum_total1):
        pickle_out1=open("sum.pickle", "wb")

        pickle.dump(sum_total1, pickle_out1)

        pickle_out1.close()

    def total(self):
        pickle_in1=open("pri.pickle","rb")

        private_key=pickle.load(pickle_in1)

        pickle_in2=open("sum.pickle","rb")

        sum1=pickle.load(pickle_in2)

        t=private_key.decrypt(sum1)

        return t