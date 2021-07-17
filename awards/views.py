from awards.models import Profile, Project, Review
from awards.forms import ProfileForm, SignUpForm, UserUpdateForm
from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):

    profiles = Profile.objects.all()
    projects = Project.objects.all()
    reviews = Review.objects.all()

    context ={"profiles":profiles,"projects":projects,"reviews":reviews}

    return render(request,'index.html',context)


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
def profile(request):
    if request.method == 'POST':

        userForm = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileForm(
            request.POST, request.FILES, instance=request.user)

        if  profile_form.is_valid():
            profile_form.save()

            return redirect('home')

    else:
        
        profile_form = ProfileForm(instance=request.user)
        user_form = UserUpdateForm(instance=request.user)

        params = {
            'user_form':user_form,
            'profile_form': profile_form

        }

    return render(request, 'registration/profile.html', params)