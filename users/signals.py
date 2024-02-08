from django.db.models.signals import post_save # signals a post_save when a  user is created
from django.contrib.auth.models import User # The sender, its what is going to send the signal
from django.dispatch import receiver # Recieves the signal and performs some tasks
from .models import Profile # Our user profile that will be used to create profiles


@receiver(post_save, sender=User)
# sender  - the user sends the signal
#  post_save - the signal which occurs when a user is saved
# @receiver - receives the signal and creates a profile(create_profile function)

def create_profile(sender, instance, created, **kwargs):
    """
    if a user has been successfully created , then create a profile of the user's instance
    """
    if created:
        profile = Profile(user = instance)
        profile.save()


@receiver(post_save, sender=User)
# sender  - the user sends the signal
#  post_save - the signal which occurs when a user is saved
# @receiver - receives the signal and creates a profile(create_profile function)

def save_profile(sender, instance, **kwargs):
    """
        Saves the created profile
    """
    if hasattr(instance, 'profile'):
        instance.profile.save()