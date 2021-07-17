from awards.models import Profile, Project, Review
from awards.forms import ProfileForm, SignUpForm
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
def profile(request, username):
    title = "Profile"
    profile = User.objects.get(username=username)
    users = User.objects.get(username=username)
    form = ProfileForm()

   


    return render(request, 'registration/profile.html', {'title':title,'profile':profile,"projects":users,"form":form})
