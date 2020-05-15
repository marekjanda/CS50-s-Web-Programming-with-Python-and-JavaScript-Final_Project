from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from datetime import datetime

from .forms import SignUpForm, BlogForm, ContactForm, ProjectForm
from .models import NewsCategory, Article, Blog, Project, Message, Fund

import stripe
# Set stripe API key
stripe.api_key = 'sk_test_VGoMuLdyerBy0LFHj08fYpR200kOwbK9uY'


# Create your views here.
def index(request):
    return render(request, 'ecohub/index.html', context={'welcome': "Welcome to EcoHub!"})

def about(request):
    return render(request, 'ecohub/about.html')

# AUTHENTICATION 

def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(home)
        else:
            print("invalid form")

    form = SignUpForm
    return render(request, 'ecohub/register.html', context={"form": form})

def login_request(request):
    # If login form is posted log user in
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(home)
            else:
                messages.info(request, f"Login failed")
    
    # Else render index page            
    form = AuthenticationForm
    return render(request, 'ecohub/login.html', {"form": form})

def logout_request(request):
    logout(request)
    return redirect(index)

def home(request):
    context = {
        "message": "You have succesfully authenticated"
    }
    return render(request, 'ecohub/home.html', context)

# NEWS SECTION

def news_view(request):
    context = {
        "news": Article.objects.all(),
        "categories": NewsCategory.objects.all(),
    }    
    return render(request, 'ecohub/news.html', context=context)

def news_category(request, category_id):
    try:
        news = Article.objects.filter(news_category=category_id)  
    except Article.DoesNotExist:
        news = None
    context = {
            "news": news,
            "categories": NewsCategory.objects.all(),
    }    
    return render(request, 'ecohub/news.html', context=context)


def article_view(request, article_id):
    article = Article.objects.get(pk=article_id)
    context = {
        "article": article,
        "categories": NewsCategory.objects.all(),
    }
    return render(request, 'ecohub/article.html', context=context)

# BLOGS SECTION

def blogs_view(request):
    context = {
        "blogs": Blog.objects.all(),
        "categories": NewsCategory.objects.all()
    }    
    return render(request, 'ecohub/blogs.html', context=context)

def blog_view(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    context = {
        "blog": blog,
        "categories": NewsCategory.objects.all(),
    }
    return render(request, 'ecohub/blog.html', context=context)

def blog_category(request, category_id):
    try:
        blogs = Blog.objects.filter(category=category_id)     
    except Blog.DoesNotExist:
        blogs = None
    context = {
        "blogs": blogs,
        "categories": NewsCategory.objects.all(),
    }
    return render(request, 'ecohub/blogs.html', context=context)

def myblogs_view(request):
    author = request.user.first_name + " " + request.user.last_name
    #print(author)
    try:
        blogs = Blog.objects.filter(author=author)
    except Blog.DoesNotExist:
        context = {"blogs": None}
    context = {
        "blogs": blogs,
        "categories": NewsCategory.objects.all()
    }
    return render(request, 'ecohub/blogs.html', context=context)

def blogwriting(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            # Create new blog in the database
            # Get the form data
            category = form.cleaned_data["category"]
            title = form.cleaned_data["title"]
            abstract = form.cleaned_data["abstract"]
            content = form.cleaned_data["content"]
            
            # Compile the name of the user as author
            author = request.user.first_name + " " + request.user.last_name

            # Create new Blog object and save
            new_blog = Blog(category=category, author=author, title=title, abstract=abstract, content=content)
            new_blog.save()

            # redirect to my blogs
            return redirect(myblogs_view)
    else:    
        form = BlogForm()
        return render(request, 'ecohub/blogwriting.html', context= {"form": form, "categories": NewsCategory.objects.all()})

# PROJECT SECTION

def projects(request):
    # get all projects
    context = {
        "projects": Project.objects.all(),
        "categories": NewsCategory.objects.all()
    }
    return render(request, 'ecohub/projects.html', context=context)

def project_categories(request):
    categories = NewsCategory.objects.all()
    context = {
        "categories": categories,
    }
    return render(request, 'ecohub/projectcategories.html', context=context)

def project_category(request, category_id):
    try:
        projects = Project.objects.filter(category=category_id)     
    except Project.DoesNotExist:
        projects = None
    context = {
        "projects": projects,
        "categories": NewsCategory.objects.all()
    }
    return render(request, 'ecohub/projects.html', context=context)

def myprojects_view(request):
    owner = request.user.first_name + " " + request.user.last_name
    try:
        projects = Project.objects.filter(owner=request.user)
    except Project.DoesNotExist:
        context = {"project": None}
    context = {
        "projects": projects,
        "categories": NewsCategory.objects.all()
    }
    return render(request, 'ecohub/projects.html', context=context)

def start_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            # Get form data
            category = form.cleaned_data["category"]
            title = form.cleaned_data["title"]
            abstract = form.cleaned_data["abstract"]
            description = form.cleaned_data["description"]
            target_funds = form.cleaned_data["target_funds"]
            # Check wether attachemnet was uploaded
            if request.FILES:
                # Create new Project object with attachement
                new_project = Project(owner=request.user, category=category, title=title, abstract=abstract, description=description, target_funds=target_funds, attachment=request.FILES['attachment'])
            else:
                # Create new project without attachement
                new_project = Project(owner=request.user, category=category, title=title, abstract=abstract, description=description, target_funds=target_funds)
            # Save new project
            new_project.save()
            # Redirect user to myproject page
            return redirect(myprojects_view)
        else:
            form = ProjectForm()
            context = {
                "form": form,
                "categories": NewsCategory.objects.all(),
                "error": "Invalid form"
            }
        return render(request, 'ecohub/startproject.html', context=context)
    else:
        form = ProjectForm()
        context = {
            "form": form,
            "categories": NewsCategory.objects.all()
        }
        return render(request, 'ecohub/startproject.html', context=context)

def project_view(request, project_id):
    project = Project.objects.get(pk=project_id)
    if project.owner == request.user:
        contributions = Fund.objects.filter(project_reference=project)
    else:
        contributions = False
    context = {
        "project": project,
        "categories": NewsCategory.objects.all(),
        "contributions": contributions
    }
    return render(request, 'ecohub/project.html', context=context)

def fund_project(request, project_id):
    project = Project.objects.get(pk=project_id)
    if request.method == "POST":
        amount = request.POST["amount"]
        print(f"Received funds: {amount}")
        project.current_funds += int(amount)
        project.save()
        new_fund = Fund(project_reference=project, contributor=request.user, amount=int(amount))
        new_fund.save()
        # Define stripe Payment Intent
        intent = stripe.PaymentIntent.create(
            amount=100,
            currency='usd',
            # Verify your integration in this guide by including this parameter
            metadata={'integration_check': 'accept_a_payment'},
        )
        return redirect(project_view, project_id)
    else:
        # Define context for page rendering
        context = {
            'project': project
        }
        return render(request, 'ecohub/fundproject.html', context=context)


def contacting(request, project_id):
    project = Project.objects.get(pk=project_id)
    if request.method == "POST":
        subject = request.POST["subject"]
        message = request.POST["message"]
        # Create Message object and save to the database
        new_message = Message(project_reference=project, sender=request.user, subject=subject, message_text=message)
        new_message.save()
        print(f"{new_message} message sent")
        return render(request, 'ecohub/contactpage.html', context={"sent": True, "project": project})
    else:
        form = ContactForm()
        #Define context for page rendering
        context = {
            'sent': False,
            'project': project,
            'form': form
        }
        return render(request, 'ecohub/contactpage.html', context=context)

def messages_view(request):
    try:
        myprojects = Project.objects.filter(owner=request.user)
        all_messages = Message.objects.all()
        # Filter messages related to myprojects
        in_messages = []
        for m in all_messages:
            if m.project_reference in myprojects:
                in_messages.append(m)
        
    except Project.DoesNotExist:
        in_messages = None
    # Get messages sent by logged user
    try:
        sent_messages = Message.objects.filter(sender=request.user)
    except Message.DoesNotExist:
        sent_messages = None 
        
    context = {
        "in_messages": in_messages,
        "sent_messages": sent_messages,
    }
    return render(request, 'ecohub/messages.html', context=context)

def message_view(request, message_id):
    # Retrieve message from the database
    try:
        message = Message.objects.get(pk=message_id)
    except Message.DoesNotExist:
        message = None
    context = {
        "message": message
    }
    return render(request, 'ecohub/message.html', context=context)
    
