from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Models.py file contains definitions of data models. They represent
# database tables and each model class corresponds to a table in the database 

class Profile(models.Model): 
    """
    defining table columns with their attributes
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # inherits from Model which is our database system
    # OneToOneField means that means each instance of one model is associated with exactly one instance of another model and viceversa
    # therefore this Profile data model will be asscoiated with User data model  in our database
    # so a user can only have one profile photo while one profile photo can belong to only one user
    image = models.ImageField(default='range.jpeg', upload_to='profile_pics')
    # ImageField is created to hold image urls, the default profile photo is set to a set pic i.e for me is range.jpeg pic
    # upload_to is where the images are to be saved for this case to profile_pics is a folder that will be created
    # when a user updates profile pic. Then the image will be saved here

    def __str__(self):
        """
        Returns: logged in username 
        """
        return f"{self.user.username}'s Profile"
    
    def save(self):
        """
        this method saves the data from our instance
        """
        super().save()
        # this overrides our parent's model execution to ensure updated inputs will still be saved

        img = Image.open(self.image.path) 
        # reading the size of the image

        if img.height > 300 or img.width > 300: #checks if its size is greater than 300 by 300 
            output_size = (300, 300) 
            # if so then resize to 300 by 300
            img.thumbnail(output_size)
            # pass the output size to thumbnail function  to resiize without bringin up distortions
            img.save(self.image.path) 
            # save the resized image