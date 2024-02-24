from django.contrib import admin
from .models import Profile

# Registering the Profile model 
# after run the command python3 manage.py makemigrations
# python3 manage.py migrate
admin.site.register(Profile)