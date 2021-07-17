from awards.models import Profile, Project
from awards.forms import ProfileForm, SignUpForm
from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.
@login_required(login_url='/accounts/login/')
def index (request):
  return render(request,'index.html')



def registration(request):
    if request.method=="POST":
        form=SignUpForm(request.POST) 
        if form.is_valid():
           form.save()
           username = form.cleaned_data.get('username')
           user_password = form.cleaned_data.get('password1')
           user = authenticate(username=username, password=user_password)
           login(request, user)
        return redirect('login')
    else:
        form= SignUpForm()
    return render(request, 'registration/registration_form.html', {"form":form}) 

@login_required(login_url='/accounts/login/')
def profile(request, username):
    title = "Profile"
    profile = User.objects.get(username=username)
    users = User.objects.get(username=username)
    id = request.user.id
    form = ProfileForm()

    try :
        profile_info = Profile.get_by_id(profile.id)
    except:
        profile_info = Profile.filter_by_id(profile.id)


    projects = Project.get_profile_pic(profile.id)
    return render(request, 'registration/profile.html', {'title':title,'profile':profile,"projects":projects, 'profile_info':profile_info,"form":form})
