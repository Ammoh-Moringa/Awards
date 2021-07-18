from django.http.response import HttpResponseRedirect
from awards.models import Profile, Project, Review
from awards.forms import ProfileForm, ProjectForm, ReviewForm, SignUpForm, UserUpdateForm
from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
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

def search_projects(request):
    if 'title' in request.GET and request.GET["title"]:

        search_term = request.GET.get("title")
        found_projects = Project.search_by_title(search_term)
        message = f"{search_term}"
        print(search_term)

        context = {"found_projects":found_projects,"message":message}

        return render(request, 'search.html',context)

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

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


@login_required(login_url='/accounts/login')
def new_project(request):
	current_user = request.user
	if request.method == 'POST':
		form = ProjectForm(request.POST,request.FILES)
		if form.is_valid():
			new_project = form.save(commit=False)
			new_project.user = current_user
			new_project.save()
			return redirect('index')
	else:
			form = ProjectForm()
	return render(request, 'project.html',{"form":form})


@login_required(login_url='/accounts/login/')
def review_project(request,project_id):
    proj = Project.project_by_id(id=project_id)
    project = get_object_or_404(Project, pk=project_id)
    current_user = request.user
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            design = form.cleaned_data['design']
            usability = form.cleaned_data['usability']
            content = form.cleaned_data['content']
            review = Review()
            review.project = project
            review.user = current_user
            review.design = design
            review.usability = usability
            review.content = content
            review.average = (review.design + review.usability + review.content)/3
            review.save()
          
            return HttpResponseRedirect(reverse('projectdetails', args=(project.id,)))
    else:
        form = ReviewForm()
    return render(request, 'reviews.html', {"user":current_user,"project":proj,"form":form})


@login_required(login_url='/accounts/login')
def project_details(request,id):
    project = Project.objects.get(id = id)
    reviews = Review.objects.order_by('-timestamp')

    context={"project":project,"reviews":reviews}
    return render(request, 'project_details.html',context)