from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required



def register(request):
    """
    params
    request -> this is the type of request from the web server
    """

    if request.method == 'POST': 
         form = UserRegisterForm(request.POST) # User RegisterForm is a predefined module that returns a registration form in django
                                                                                # taking the request type parameter just as in any simple form
         if form.is_valid(): # is_valid is  an inbuilt function that checks if all details were provided and returns true if so
              form.save() # inbuilt form saving funcition in django
              username = form.cleaned_data.get('username')
              messages.success(request, f'You have successfully created your account {username}. Now loign')
              return redirect('login')
    else: # GET request method
         form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
     """
     params
     request -> this is the type of request from the web server
     """
     if request.method == 'POST': # This method means that the inputs will needed to be sent to our database
            u_form = UserUpdateForm(request.POST, instance=request.user) # UserUpdateForm predefined module that provides an update form input for username
                                                                                                                             # parameters - request.POST which explains that data is required to be saved, instance=request.user -> placeholder with the current logged in user
            p_form = ProfileUpdateForm(request.POST,  request.FILES ,instance=request.user.profile) # the params ; request.FILES is also a placeholder with the current profile pic url . The url comes from the param: request.user.profile which fetches the our profile url
            
            if u_form.is_valid() and p_form.is_valid():
                 u_form.save() # save the new username
                 p_form.save() # save the new password
                 messages.success(request, "Your profile/account has been updated successfully")
                 return redirect('profile') # redirect to the profiles page after updating details


     else: # this is the GET method meaning a client wants the updating form
            u_form = UserUpdateForm(instance=request.user)
            p_form = ProfileUpdateForm(instance=request.user.profile)

          
     context = {
          'u_form': u_form,
          'p_form': p_form
     } # dictionary with our forms to be renderes in our profile webpage
     return render(request, 'users/profile.html', context)