from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    """
    defining table columns with their attributes
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='range.jpeg', upload_to='profile_pics')

    def __str__(self):
        """
        This is like alt, a message to be shown
        """
        return f"{self.user.username}'s Profile"
    
    def save(self):
        """
        this method saves the data from our instance
        """
        super().save()

        img = Image.open(self.image.path) # reading the size of the image

        if img.height > 300 or img.width > 300: #checks if its size is greater than 300 by 300 
            output_size = (300, 300) # if so then resize to 300 by 300
            img.thumbnail(output_size)
            img.save(self.image.path) # save the resized image