# study_buddy

# `Steps to initiate django:`
1. go to the projects directory in your local system and then RUN the command `ls` in your git bash terminal it will show you all the files in that directory.
2. Run the command `cd Document` to safe all the files in that folder.
3. Run the command `ls` to show the all the lists of the files.
4. Run the command `mkdir data` to make a folder named as data and again run the `ls` command to show all the list of the files.
5. Run the `cd data` command to change the directory and again run the `ls` command to show the list of files.
6. Run the command `git clone https://github.com/Ayeshashabbir01/study_buddy.git` and paste the url of our project to clone the repository.
7. Run the command `ls` to show the repository.
8. Run the command `cd study_buddy/` to go to the study_buddy .
9. Run the command `code .` to open in the visual studio code.
10. Run the command `python -m venv myenv` to create the virtual environment in the name of myenv.
11. Run the command `source myenv/Scripts/activate` to activate the envionment.
12. Run the command `python -m django version` to check the version of the django .
13. Run the command `pip install django` to install the django in the environment and again check the version of django.
14. Run the command ` django-admin startproject core ` and create name core project in the studdy_buddy repository.
15. Run the command `cd core` to go to the core and also run the ls command to show the all files in the core folder.
16. Run the command `python manage.py startapp base` to create the new application in the django project.
17. Run the command `python manage.py runserver` to run the server application.
18. Run the command `cd../` to one back to the folder.And run the `ls -a ` command to show all the files including the .gitignore.
19. Run the command `git add .`to add all changes in the current directories. And `git commit`to commit the message "Steps to initiate django".
20. Run the command `git push` to push to the github.

# `API:`
>1. we will send a GET request to the django View the View will which will send a request to the database, our database will send that data back to the view, the view will serialize that data and send it back to the client.

>2. when we are sending the data, we will send the form data from the frontEnd.

`Virtual Environment`

```py
pip install virtualenv
virtualenv venv
source env/Scripts/activate
```
To activate the virtual environment.

` Building base app`
```py
 python manage.py runserver
 python manage.py startapp base
 ```
configure your base app in the settings.py.

```py 
# settings.py
INSTALLED_APPS = [
 # ......
     'base.apps.BaseConfig',
]
```

 Go to the app and create the urls file to handle all the route just for these app.
 
```py
 #// studybud/base/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('room/', views.room, name="room"),
]
```
so we have two views and two urls.


```py
# /studybud/urls.py
urlpatterns = [
    # .....
    path('', include('base.urls')),
]
```

# `Templates:`
1. create templates,and update the django that we have a templates .
```py 
 # studybud/settings.py/TEMPLATES
 TEMPLATES = [
    BASE_DIR / 'templates'
 ],
 ```
2. create four files in these templates folder `home.html`,`room.html`,`main.html`, `navbar.html`.

```py
#// studybud/templates/home.html
{% extends "main.html" %}

 {% block content  %} 

 <h1>Home Template</h1>

<div>
    <div>
        {% for room in rooms %}
            <div>
                <h5>{{room.id}} -- <a href="{% url 'room' room.id %}">{{room.name}}</a></h5>
            </div>
            
        {% endfor %}
    </div>
    
</div>

 {% endblock content %}
 ```
```py
# //studybud/templates/room.html
{% include 'navbar.html' %}

{% block content %}

<h1>{{room.name}}</h1>

{% endblock content %}
```
In navbar.html, we can use different tags to create different styles.
```py 
# // studybud/templates/navbar.html
<a href="/">
    <h1>LOGO</h1>
</a>

<hr>
```
In main.html, we can encapsulates all the templates in our projects.

```py
# // studybud/templates/main.html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>StudyBud</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!--link rel='stylesheet' type='text/css' media='screen' href='main.css'-->
    
</head>
<body>
    {% include "navbar.html" %}
    
    {% block content %}
    
    {% endblock content %}
</body>
</html>
```
To organize our project, create a `templates` folder inside the `ourapp` directory. Inside `templates`, create a `base` subfolder. Move `home.html` and `room.html` into the `base` subfolder. This structure separates specific templates from those used throughout the app.

```py
#// studybud/base/views.py
from django.shortcuts import render
rooms = [
    {'id': 1, 'name': 'lets learn python!'},
    {'id': 2, 'name': 'Design with me.'},
    {'id': 3, 'name': 'Frontend developer.'},
]

def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request,pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room': room}
    return render(request, 'base/room.html', context)
```

```py
# // studybud/base/urls.py
urlpatterns = [
    path('', views.home, name="home"),
    path('room/<str:pk>/', views.room, name="room"),
]
```
In home.html we can add the link here. to show the room id and its name.
```py 
# studybud/templates/main.html
{% extends "main.html" %}

 {% block content  %} 

 <h1>Home Template</h1>

<div>
    <div>
        {% for room in rooms %}
            <div>
             # adding the link here,
  <h5>{{room.id}} -- <a href="{% url 'room' room.id %}">{{room.name}}</a></h5>
               
            </div>
            
        {% endfor %}
    </div>
    
</div>

 {% endblock content %}
```
```py 
#//  studybud/base/views.py
def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room': room}
    return render(request, 'base/room.html', context)
```

```py
# //studybud/templates/base/room.html
{% include 'navbar.html' %}

{% block content %}

<h1>{{room.name}}</h1>

{% endblock content %}

```
# `Database And Admin Panel:`
```py 
# Steps to create database:
1. python manage.py  make migrations
2. python manage.py migrate
3. python manage.py createsuperuser
4. python manage.py runserver
```
go to the admin panel.


# `Modelling`
In modelling , defining the structure of our database tables using `Python classes`. Each class represents a `database table`, and each attribute of the class represents a `columns` in that table. This allows you to interact with your database using Python code .
so, we will model our data in `models.py`.
```py 
# create room in the model.py
from django.db import models

# Create your models here.
class Room(models.Model):
    # host 
    # topic 
    name = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    # participants 
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.name 
```
now we have to `migrate` our database and `Register` that room model to the admin.py.
```py
python manage.py migrate
python manage.py runserver
```
```py 
# register the model in admin.py
from django.contrib import admin
# Register your models here.
from .models import Room
admin.site.register(Room)
```
`Now add a room from admin panel`

```py
Steps:
1. Make a model
2. Register the model in the admin.py
3. migrate the database
4. run the server
5. add room in the room model from admin panel.
```
# `Now Adding more Models`
  Each model represents different data, like `users`, `posts`, or `comments`. so, we can add more models to make the code easier to maintain and update easily.
```py
# models.py
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name 

class Room(models.Model):
    host  = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    # participants 
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name 
    

class Message(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]
```
now we have to `migrate our database` and `Register` that model to the admin.py,
```py
 python manage.py makemigrations
 python manage.py migrate
```
when we can registering our model,this makes it easy to `add`, `edit`, and `delete data` directly from the admin panel.
```py
# admin.py
from django.contrib import admin

# Register your models here.

from .models import Room ,Topic , Message

admin.site.register(Room)

admin.site.register(Topic)

admin.site.register(Message)
```
# `CRUD`

CRUD stands for Create, Read, Update, and Delete, which are the four basic operations for managing data in a database.
1. we can create the `room_form.html` file inside the base app firstly we can input to the `submit button` and create a room using function in views.py.
```py
# studybud/base/room_forms.html
{% extends 'main.html' %}

{% block content %}
  <div>
    <form method="POST" action="">
      {% csrf_token %}
      {{form.as_p}}
      <input type="submit" value="Submit" />
    </form>
  </div>
{% endblock content %}
```

2. create python file `forms.py` ,import model Room and access all the fileds of that model.
```py
#studybud/base/forms.py
from django.forms import ModelForm
from .models import Room

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'

```
```py
#studybud/base/delete.html
{% extends 'main.html' %}

{% block content %}
    <form method="POST" action="">
        {% csrf_token %}
        <p>Are you sure you want to delete "{{ obj }}"?</p>
        <a href="{{ request.META.HTTP_REFERER }}">Go Back</a>
        <input type="submit" value="Confirm" />
    </form>
{% endblock content %}
```
3. In views.py we can create ,update and delete the room.
```py
#studybud/base/views.py
from django.shortcuts import render,redirect
from .models import Room,Topic
from .forms import RoomForm
from django.db.models import Q
#rooms = [
#    {'id': 1, 'name': 'lets learn python!'},
#    {'id': 2, 'name': 'Design with me.'},
#    {'id': 3, 'name': 'Frontend developer.'},
#]

def home(request):
    q = request.GET.get('q') if request.GET.get('q') is not None else ''

    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q)|
        Q(description__icontains=q)
        )
    topics= Topic.objects.all()
    room_count = rooms.count()
    context = {'rooms': rooms,'topics':topics ,'room_count':room_count}
    return render(request, 'base/home.html', context)

def room(request,pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)

def createRoom(request):
    form=RoomForm()
    if request.method == 'POST': 
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  
    context = {"form":form}
    return render(request, 'base/room_form.html', context)


def updateRoom (request, pk):
    room =Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST,instance=room)
        if form.is_valid():
            form.save()
            return redirect('home') 
        
    context = {'form': form}
    return render(request, 'base/room_form.html', context)
     

def deleteRoom(request, pk):
     room =Room.objects.get(id=pk)
     if request.method == 'POST':
        room.delete()
        return redirect('home')
     return render(request, 'base/delete.html', {'obj': room})
```
```py
#studybud/base/url.py
from django.urls import path
from.import views
urlpatterns = [
    
    
    path("",views.home, name="home"),
    path('room/<str:pk>/',views.room,name="room"),
    path('create-room/', views.createRoom, name='create-room'),
    path('update-room/<str:pk>', views.updateRoom, name='update-room'),
    path('delete-room/<str:pk>', views.deleteRoom, name='delete-room'),


]
```
Each model in models.py represents a different entity in our application. For example:
Topic represents a discussion topic.
Room represents a chat room or discussion room.
Message represents a message posted in a room.
Thats why we create different models for different purpose.

```py
# studybud/base/models.py
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    # participants 
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name  


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]
```
# `Search`
A search form has a text box and a submit button. When we enter our search words and press the button, the website processes our request and displays the results.
In search we can search the room manually by its author name, text, name of topic. 
```py
# studybud/templates/base/home.html
{% extends "main.html" %}
 {% block content  %} 

 <style>
    .home-container {
        display: grid;
        grid-template-columns: 1fr 3fr;
    }
 </style>
    

<div class='home-container'>
    <div>
        <h3>Browse Topics</h3>
        <hr>
        <div>
            <a href="{% url 'home'%}">All</a>
        </div>

        {% for topic in topics %}
        <div>
            <a href="{% url 'home' %}?q={{topic.name}}">{{topic.name}}</a>
        </div>
        {% endfor %}
    </div>
    <div>
        <h5>{{room_count}} rooms available</h5>
        <a href="{% url 'create-room' %}">Create Room</a>

    <div>
        {% for room in rooms %}
            <div>
                <a href="{% url 'update-room' room.id %}">Edit</a>
                <a href="{% url 'delete-room' room.id %}">Delete</a>
                <span>@{{room.host.username}}</span>
                <h5> -- <a href="{% url 'room' room.id %}">{{ room.name }}</a></h5>
           <small>{{room.topic.name}}</small>
                <hr>
            </div>
        {% endfor %}
    </div>
    </div>
    
    
</div>

 {% endblock content %}
 ```

 Users can manage discussion rooms by searching for rooms based on topics, names, or descriptions, as well as creating, updating, and deleting rooms. 
 ```py
 # studybud/base/views.py
 from django.shortcuts import render,redirect
from .models import Room,Topic
from .forms import RoomForm
from django.db.models import Q
#rooms = [
#    {'id': 1, 'name': 'lets learn python!'},
#    {'id': 2, 'name': 'Design with me.'},
#    {'id': 3, 'name': 'Frontend developer.'},
#]

def home(request):
    q = request.GET.get('q') if request.GET.get('q') is not None else ''

    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q)|
        Q(description__icontains=q)
        )
    topics= Topic.objects.all()
    room_count = rooms.count()
    context = {'rooms': rooms,'topics':topics ,'room_count':room_count}
    return render(request, 'base/home.html', context)

def room(request,pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)

def createRoom(request):
    form=RoomForm()
    if request.method == 'POST': 
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  
    context = {"form":form}
    return render(request, 'base/room_form.html', context)


def updateRoom (request, pk):
    room =Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST,instance=room)
        if form.is_valid():
            form.save()
            return redirect('home') 
        
    context = {'form': form}
    return render(request, 'base/room_form.html', context)
     

def deleteRoom(request, pk):
     room =Room.objects.get(id=pk)
     if request.method == 'POST':
        room.delete()
        return redirect('home')
     return render(request, 'base/delete.html', {'obj': room})
```
we can search  and count the  numbers of rooms by using GET method.
```py
# studybud/templates/navbar.html
<a href="/">
    <h1>LOGO</h1>
</a>
<form method="GET" action="{% url 'home' %}">
    <input type="text" name="q" placeholder="Search Rooms..." />
    <button type="submit">Search</button>
</form>


<hr>
```
# `User Login/logout`

`Login`
A form where users enter their username and password to access the website.
`Logout`
A button that users click to end their session and log out of the website.

 we can create the file `login_register.html` and register the user.
 ```py
# studybud/templates/base/login_register.html
{% extends 'main.html' %}
{% block content %}
<div>
<form method="POST" action="">
{% csrf_token %}
<label>Username: </label>
<input type="text" name="username" placeholder="Enter Username" />
<br>
<label>Password: </label>
<input type="password" name="password" placeholder="Enter Password" />
<br>
<input type="submit" value="Login" />
</form>
</div>
{% endblock content %}
```
now create view for this login page.

```py
#studybud/base/views.py
def loginPage(request):
    context = {}
    return render(request, 'base/login_register.html', context)
```
```py
#studybud/base/urls.py
urlpatterns = [
    path('login/',views.loginPage, name="login"),
]
```
we can create the loginpage , users can login the page and access the website and  user can also logout ,update and delete the room.
```py
# studybud/base/views.py

from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login,logout
from django.contrib import messages
from .models import Room,Topic
from .forms import RoomForm
from django.db.models import Q
#rooms = [
#    {'id': 1, 'name': 'lets learn python!'},
#    {'id': 2, 'name': 'Design with me.'},
#    {'id': 3, 'name': 'Frontend developer.'},
#]


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
          
        except User.DoesNotExist:
            messages.error(request, 'User does not exist')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Username or Password does not  exist')

    context = {}
    return render(request, 'base/login_register.html', context)
 
def logoutUser(request):
    logout(request)
    return redirect('home')


def home(request):
    q = request.GET.get('q') if request.GET.get('q') is not None else ''

    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q)|
        Q(description__icontains=q)
        )
    topics= Topic.objects.all()
    room_count = rooms.count()
    context = {'rooms': rooms,'topics':topics ,'room_count':room_count}
    return render(request, 'base/home.html', context)

def room(request,pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)

def createRoom(request):
    form=RoomForm()
    if request.method == 'POST': 
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  
    context = {"form":form}
    return render(request, 'base/room_form.html', context)


def updateRoom (request, pk):
    room =Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST,instance=room)
        if form.is_valid():
            form.save()
            return redirect('home') 
        
    context = {'form': form}
    return render(request, 'base/room_form.html', context)
     

def deleteRoom(request, pk):
     room =Room.objects.get(id=pk)
     if request.method == 'POST':
        room.delete()
        return redirect('home')
     return render(request, 'base/delete.html', {'obj': room})
``` 
and then give the urls of our views  functions to access the different pages in our website.
```py
# studybud/base/urls.py
from django.urls import path
from.import views
urlpatterns = [
    path('login/',views.loginPage, name="login"),
    path('logout/',views.logoutUser, name="logout"),
    
    path("",views.home, name="home"),
    path('room/<str:pk>/',views.room,name="room"),
    path('create-room/', views.createRoom, name='create-room'),
    path('update-room/<str:pk>', views.updateRoom, name='update-room'),
    path('delete-room/<str:pk>', views.deleteRoom, name='delete-room'),


]
```

```py
# base/templates/main.html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>StudyBud</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!--link rel='stylesheet' type='text/css' media='screen' href='main.css'-->
    
</head>
<body>
    {% include "navbar.html" %}
    
    {% if messages %}
<ul class="messages">
    {% for message in messages %}
    <li></li>{{ message }}</li>
    {% endfor %}
</ul>
{% endif %}

    {% block content %}
    
    {% endblock content %}
</body>
</html>
```
we can set a frame to search different rooms by its author name ,text, name of topic etc and also check the user authenticatons through  login and logout.
```py
# base/navbar.html
<a href="/">
    <h1>LOGO</h1>
</a>
<form method="GET" action="{% url 'home' %}">
    <input type="text" name="q" placeholder="Search Rooms..." />
    <button type="submit">Search</button>
</form>
{% if request.user.is_authenticated %}
<a href="{% url 'logout' %}">Logout</a>
{% else %}
<a href="{% url 'login'%}">Login</a>
{% endif %}

<hr>
```

# `User Registeration`
In user Registeration we can manage user login and registration. It provides forms for users to log in or sign up, handles the authentication process, and allows new users to create accounts and log in automatically.

```py
# studybud/template/base/login_register.html
{% extends 'main.html' %}
{% block content %}


{% if page == 'login' %}

<div>
<form method="POST" action="">
{% csrf_token %}
<label>Username: </label>
<input type="text" name="username" placeholder="Enter Username" />
<br>
<label>Password: </label>
<input type="password" name="password" placeholder="Enter Password" />
<br>
<input type="submit" value="Login" />
</form>

<p>havent signed up yet?</p>

<a href="{% url 'register' %}">Sign up</a>

</div>
{% else %}
<div>
    <form method="POST" action="">
        {% csrf_token %}
        {{form.as_p}}
    <input type="submit" value="Register"/>
    </form>
    <p>Already signed up yet?</p>
    <a href="{% url 'login' %}">Login</a>
</div>

{% endif %}

{% endblock content %}
```


```py
# studybud/base/views

from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate , login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Room,Topic
from .forms import RoomForm
from django.db.models import Q
#rooms = [
#    {'id': 1, 'name': 'lets learn python!'},
#    {'id': 2, 'name': 'Design with me.'},
#    {'id': 3, 'name': 'Frontend developer.'},
#]

def loginPage(request):
    page = 'login' 
    if request.user.is_authenticated:
         return redirect('home')


    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
          
        except User.DoesNotExist:
            messages.error(request, 'User does not exist')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Username or Password does not  exist')

    context = { 'page': page}
    return render(request, 'base/login_register.html', context)
 
def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    form = UserCreationForm()

    if request.method == 'Post':
        form = UserCreationForm(request.Post)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occured during registerations')
            
    return render(request, 'base/login_register.html',{'form': form })


def home(request):
    q = request.GET.get('q') if request.GET.get('q') is not None else ''

    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q)|
        Q(description__icontains=q)
        )
    topics= Topic.objects.all()
    room_count = rooms.count()
    context = {'rooms': rooms,'topics':topics ,'room_count':room_count}
    return render(request, 'base/home.html', context)

def room(request,pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)

def createRoom(request):
    form=RoomForm()
    if request.method == 'POST': 
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  
    context = {"form":form}
    return render(request, 'base/room_form.html', context)

@login_required(login_url='login')
def updateRoom (request, pk):
    room =Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.user != room.host:
        return HttpResponse('you are not allowed here!!')
    

    if request.method == 'POST':
        form = RoomForm(request.POST,instance=room)
        if form.is_valid():
            form.save()
            return redirect('home') 
        
    context = {'form': form}
    return render(request, 'base/room_form.html', context)
     

def deleteRoom(request, pk):
     room =Room.objects.get(id=pk)

     if request.user != room.host:
        return HttpResponse('you are not allowed here!!')
     
     if request.method == 'POST':
        room.delete()
        return redirect('home')
     return render(request, 'base/delete.html', {'obj': room})
```
# `Chat Room Messsges Crud:`
In the chat room messgaes we can copy ,update ,delete and read the messages, add the add the `write your message here ...` button to type the meassge in the room.
we can add the participants,different users can login and join the conversations in the room.
we can `add the users` in the room and in conversations participations.
we can also able to `delete` the user message in the room conversations and the only owner can delete the mesages.
  
```py
#studybuddy/base/templates/room.html
{% include 'navbar.html' %}

{% block content %}

<style>
    .room-container {
        display: grid;
        grid-template-columns: 3fr 1fr;
    }
</style>

<div class='room-container'>
    <div>
        <h1>{{ room.name }}</h1>
        <p>{{ room.description }}</p>
        
        <div class="comment-wrapper">
            <h3>Conversation</h3>
            <hr>
        
            {% for message in room_messages %}
                <div>
                    {% if request.user == message.user %}
                        <a href="{% url 'delete-message' message.id %}">Delete</a>
                    {% endif %}
                    <small>@{{ message.user.username }} {{ message.created|timesince }} ago</small>
                    <p>{{ message.body }}</p>
                    <hr>
                </div>
            {% empty %}
                <p>No messages yet.</p>
            {% endfor %}
        </div>
        
        {% if request.user.is_authenticated %}
        <div class='comment-form'>
            <form method='POST' action="">
                {% csrf_token %}
                <input type="text" name='body' placeholder="Write your message here..." required>
                <button type="submit">Send</button>
            </form>
        </div>
        {% endif %}
    </div>
    
    <div>
        <h3>Participants</h3>
        <hr>
        {% for user in participants %}
            <div>
                <p>@{{ user.username }}</p>
            </div>
        {% empty %}
            <p>No participants yet.</p>
        {% endfor %}
    </div>
</div>

{% endblock content %}
```

```py
#studybud/base/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)

    avatar = models.ImageField(null=True, default="avatar.svg")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]
```
# `Make Migrations`
```py
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

```py
#studybud/base/views.py
@login_required(login_url='/login')
def deleteMessage(request, pk):
    message = Message.objects.get(id=pk)

    if request.user != message.user:
        return HttpResponse('You are not allowed here!!')

    if request.method == 'POST':
        message.delete()
        return redirect('home')

    return render(request, 'base/delete.html', {'obj': message})
```

```py
#studybud/base/urls.py
urlpatterens =[
     path('delete-message/<str:pk>', views.deleteMessage, name='delete-message'),
]
```
# `Activity Feed`
we can have the `Recent Activity` ,Prompt users acn actually engage on the website to came here to acivity, see whats going on, active in the activity and can follow the peoples.
Build an `social networking features` you can only allow thefriends are doing to followings and commitings etc.
In these way friends can seeing the posts commiting and engage them.

```py
# studybud/base/template/home.html
{% extends "main.html" %}

{% block content %} 

<style>
    .home-container {
        display: grid;
        grid-template-columns: 1fr 3fr 1fr;
    }
</style>
    
<div class='home-container'>
    <!-- Sidebar for topics -->
    <div>
       {% include "base/topics_component.html" %}  
    </div>
    
    <!-- Main content area for rooms -->
    <div>
        <h5>{{ room_count }} rooms available</h5>
        <a href="{% url 'create-room' %}">Create Room</a>

       {% include "base/feed_component.html" %}
    </div>

    
    <div>
        {% include "base/activity_component.html" %}
    </div>
</div>

{% endblock content %}
```

we create the `html files` in the `templates` folder.`activity_component.html`  is for the activities in the room,`topic.html` is for the whats the topics are included ,`feed_components.html` is for the how many rooms are  now availible ,`profile.html` is for to create the users profile .

```py
#studybud/base/templates/activity_components.html
<div class="activities">
    <div class="activities__header">
      <h2>Recent Activities</h2>
    </div>
  
    {% for message in room_messages %}
    <div class="activities__box">
      <div class="activities__boxHeader roomListRoom__header">
        <a href="{% url 'user-profile' message.user.id %}" class="roomListRoom__author">
          <div class="avatar avatar--small">
            <img src="{{message.user.avatar.url}}" />
          </div>
          <p>
            {{ message.user }}
            <span>{{ message.created|timesince }}</span>
          </p>
        </a>
  
        {% if request.user == message.user %}
        <div class="roomListRoom__actions">
          <a href="{% url 'delete-message' message.id %}">
            <svg version="1.1" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32">
              <title>remove</title>
              <path
                d="M27.314 6.019l-1.333-1.333-9.98 9.981-9.981-9.981-1.333 1.333 9.981 9.981-9.981 9.98 1.333 1.333 9.981-9.98 9.98 9.98 1.333-1.333-9.98-9.98 9.98-9.981z"
              ></path>
            </svg>
          </a>
        </div>
        {% endif %}
      </div>
  
      <div class="activities__boxContent">
        <p>replied to post “<a href="{% url 'room' message.room.id %}">{{ message.room }}</a>”</p>
        <div class="activities__boxRoomContent">
          {{ message.body }}
        </div>
      </div>
    </div>
    {% endfor %}
  </div>
```
```py
#studybud/base/feed_component.html
   {% for room in rooms %}

   <div class="roomListRoom">
    <div class="roomListRoom__header">
    <a href="{% url 'user-profile' room.host.id %}" class="roomListRoom__author">
        <div class="avatar avatar--small">
          <img src="{{room.host.avatar.url}}" />
        </div>
        <span>{{room.host.username}}</span>
      </a>
      <div class="roomListRoom__actions">
        <span>{{ room.created|timesince }}</span>
      </div>
    </div>
    <div class="roomListRoom__content">
        <a href="{% url 'room' room.id %}">{{room.name}}</a>
     
    </div>
    <div class="roomListRoom__meta">
      <a href="{% url 'room' room.id %}" class="roomListRoom__joined">
        <svg version="1.1" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32">
          <title>user-group</title>
          <path
            d="M30.539 20.766c-2.69-1.547-5.75-2.427-8.92-2.662 0.649 0.291 1.303 0.575 1.918 0.928 0.715 0.412 1.288 1.005 1.71 1.694 1.507 0.419 2.956 1.003 4.298 1.774 0.281 0.162 0.456 0.487 0.456 0.85v4.65h-4v2h5c0.553 0 1-0.447 1-1v-5.65c0-1.077-0.56-2.067-1.461-2.584z"
          ></path>
          <path
            d="M22.539 20.766c-6.295-3.619-14.783-3.619-21.078 0-0.901 0.519-1.461 1.508-1.461 2.584v5.65c0 0.553 0.447 1 1 1h22c0.553 0 1-0.447 1-1v-5.651c0-1.075-0.56-2.064-1.461-2.583zM22 28h-20v-4.65c0-0.362 0.175-0.688 0.457-0.85 5.691-3.271 13.394-3.271 19.086 0 0.282 0.162 0.457 0.487 0.457 0.849v4.651z"
          ></path>
          <path
            d="M19.502 4.047c0.166-0.017 0.33-0.047 0.498-0.047 2.757 0 5 2.243 5 5s-2.243 5-5 5c-0.168 0-0.332-0.030-0.498-0.047-0.424 0.641-0.944 1.204-1.513 1.716 0.651 0.201 1.323 0.331 2.011 0.331 3.859 0 7-3.141 7-7s-3.141-7-7-7c-0.688 0-1.36 0.131-2.011 0.331 0.57 0.512 1.089 1.075 1.513 1.716z"
          ></path>
          <path
            d="M12 16c3.859 0 7-3.141 7-7s-3.141-7-7-7c-3.859 0-7 3.141-7 7s3.141 7 7 7zM12 4c2.757 0 5 2.243 5 5s-2.243 5-5 5-5-2.243-5-5c0-2.757 2.243-5 5-5z"
          ></path>
        </svg>
        {{room.participants.all.count}} Joined
      </a>
      <p class="roomListRoom__topic">{{room.topic.name}}</p>
    </div>
  </div>

  {% endfor %}
```

```py
#studybud/base/views.py
def home(request):
    q = request.GET.get('q') if request.GET.get('q') else ''
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
    )
    topics = Topic.objects.all()[:5]
    room_count = rooms.count()
    room_messages = Message.objects.filter(Q(room__topic__name__icontains=q))

    context = {'rooms': rooms, 'topics': topics, 'room_count': room_count, 'room_messages': room_messages}
    return render(request, 'base/home.html', context)


```
# `User Profile Page`
I the user profile page  we can set thet every user can have its own all `Browse Topics` ,`rooms` ,and its `Recent Activity`.for example when i click on the james profile then they have its own all `browse topics` ,and show the `number of rooms` and have the `Recent activity`. 
We can set the users `name` , `About`,also we acn edit the user profile.
```py
#studybud/base/templates/profile.html

{% extends 'main.html' %}


{% block content %}


  <main class="profile-page layout layout--3">
    <div class="container">
      <!-- Topics Start -->

      {% include 'base/topics_component.html' %}
      <!-- Topics End -->

      <!-- Room List Start -->
      <div class="roomList">
        <div class="profile">
          <div class="profile__avatar">
            <div class="avatar avatar--large active">
              <img src="https://randomuser.me/api/portraits/men/11.jpg" />
            </div>
          </div>
          <div class="profile__info">
            <h3>{{user.username}}</h3>
            <p>{{user.username}}</p>
            {% if request.user == user %}

            <a href="{% url 'update-user' %}" class="btn btn--main btn--pill">Edit Profile</a>
          {% endif %}
          </div>

          <div class="profile__about">
            <h3>About</h3>
            <p>
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Consequuntur illo tenetur
              facilis sunt nemo debitis quisquam hic atque aut? Ducimus alias placeat optio
              accusamus repudiandae quis ab ex exercitationem rem?
            </p>
          </div>
        </div>

        <div class="roomList__header">
          <div>
            <h2>Study Rooms Hosted by dennis_ivy</a>
            </h2>
          </div>
        </div>
     
        {% include 'base/feed_component.html' %}
      </div>
      <!-- Room List End -->

      <!-- Activities Start -->
      {% include 'base/activity_component.html' %}
      <!-- Activities End -->
    </div>
  </main>

 {% endblock content %}
```
```py
# studybud/base/templates/activity_components.html
<div class="activities">
    <div class="activities__header">
      <h2>Recent Activities</h2>
    </div>
  
    {% for message in room_messages %}
    <div class="activities__box">
      <div class="activities__boxHeader roomListRoom__header">
        <a href="{% url 'user-profile' message.user.id %}" class="roomListRoom__author">
          <div class="avatar avatar--small">
            <img src="{{message.user.avatar.url}}" />
          </div>
          <p>
            {{ message.user }}
            <span>{{ message.created|timesince }}</span>
          </p>
        </a>
  
        {% if request.user == message.user %}
        <div class="roomListRoom__actions">
          <a href="{% url 'delete-message' message.id %}">
            <svg version="1.1" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32">
              <title>remove</title>
              <path
                d="M27.314 6.019l-1.333-1.333-9.98 9.981-9.981-9.981-1.333 1.333 9.981 9.981-9.981 9.98 1.333 1.333 9.981-9.98 9.98 9.98 1.333-1.333-9.98-9.98 9.98-9.981z"
              ></path>
            </svg>
          </a>
        </div>
        {% endif %}
      </div>
  
      <div class="activities__boxContent">
        <p>replied to post “<a href="{% url 'room' message.room.id %}">{{ message.room }}</a>”</p>
        <div class="activities__boxRoomContent">
          {{ message.body }}
        </div>
      </div>
    </div>
    {% endfor %}
  </div>
```
# `Static Files`
we can create the static files because static files can configure the `images`, `css files` and `javascripts files`. 
so thats why we acn create the new folder inside the root directory ,named as `static` and in the static foleder we can create the another `style` folder and in the foledr create the file `main.css` and also in static  folder we can crete the `images` folder to store all the imgaes are there.
# `configure static files`
we can configure the static files in the settings.py and let django khown about the static files.

```py
#studybud/settings.py
STATIC_URL = 'static/'
MEDIA_URL = '/images/'

STATICFILES_DIRS =[
    BASE_DIR / 'static'
]

MRDIA_ROOT= BASE_DIR / 'static/images'
```
Then we can add the background colour in the home by using `main.css` file .
```py
# studybud/static/styles/main.css
body{
    background-color: aquamarine;
}
```
we can apply the static files ,images like user can add the images that they can needed in website.

```py
<!DOCTYPE html>
{% load static %}
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="shortcut icon" href="assets/favicon.ico" type="image/x-icon" />
    <link rel="stylesheet" href="{% static 'styles/style.css' %}" />
    <title>StudyBuddy - Find study partners around the world!</title>
  </head>

  <body>
   
    {% include "navbar.html" %}

    {% if messages %}
    <ul class="messages">
        {% for message in messages %}
        <li>{{ message }}</li>
        {% endfor %}
    </ul>
    {% endif %}
    
    {% block content %}
    
    {% endblock content %}

    <script src="{% static 'js/script.js' %}"></script>
  </body>
</html>
```
# `Installation Theme`
 A theme in this context includes all the static files (like `CSS, JavaScript, and images`) and `HTML templates `that define the appearance and layout of your web application.

This is the binary theme, `binary theme` is better then the handwritten code thats why we can install the theme in the github repository 

we have statndard theme with some `html and javascript` files.The theme with the css and javascript these are all set with file `paths` allready connected to that specific theme.

# `steps`

1. **Get the Theme**: Download or create the theme.
2. **Add Static Files**: Place CSS, JS, and images in the `static` directory.
3. **Copy HTML Files**: Move HTML templates to the `templates` directory.
4. **Configure Settings**: Update `settings.py` for static files and templates.
5. **Modify Base Template**: Edit `base.html` to include theme elements.
6. **Extend Templates**: Create or update templates to use `base.html`.
7. **Test the Theme**: Run the Django server to see the theme in action.


In the hme we can add the topics options,also count the no of rooms

```py
#studybud/base/template/home.html
    {% extends 'main.html' %}
    {% block content %}
    <main class="layout layout--3">
      <div class="container">
        <!-- Topics Start -->
         {% include 'base/topics_component.html' %}
        
        <!-- Topics End -->

        <!-- Room List Start -->
        <div class="roomList">
          <div class="mobile-menu">
            <form action ="{%url 'home' %}" method= "GET" class="header__search">
              <label>
                <svg version="1.1" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32">
                  <title>search</title>
                  <path
                    d="M32 30.586l-10.845-10.845c1.771-2.092 2.845-4.791 2.845-7.741 0-6.617-5.383-12-12-12s-12 5.383-12 12c0 6.617 5.383 12 12 12 2.949 0 5.649-1.074 7.741-2.845l10.845 10.845 1.414-1.414zM12 22c-5.514 0-10-4.486-10-10s4.486-10 10-10c5.514 0 10 4.486 10 10s-4.486 10-10 10z"
                  ></path>
                </svg>
                <input  name="q" placeholder="Search for posts" />
              </label>
            </form>
            <div class="mobile-menuItems">
              <a class="btn btn--main btn--pill" href="{% url 'topics' %}">Browse Topics</a>
              <a class="btn btn--main btn--pill" href="{% url 'activity' %}">Recent Activities</a>
            </div>
          </div>

          <div class="roomList__header">
            <div>
              <h2>Study Room</h2>
              <p>{{room_count}} Rooms available</p>
            </div>
            <a class="btn btn--main" href="{% url 'create-room'%}">
              <svg version="1.1" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32">
                <title>add</title>
                <path
                  d="M16.943 0.943h-1.885v14.115h-14.115v1.885h14.115v14.115h1.885v-14.115h14.115v-1.885h-14.115v-14.115z"
                ></path>
              </svg>
              Create Room
            </a>
          </div>

        {% include 'base/feed_component.html' %}

          
        
        </div>
        <!-- Room List End -->

        <!-- Activities Start -->
         {% include 'base/activity_component.html' %}
       
        <!-- Activities End -->
      </div>
    </main>
  
    {% endblock %}
```
# `steps`

1. Set Up Django Project
2. Organize Static Files
3. Create Templates Directory
4. Create `navbar.html` File
5. Update `settings.py`
6. Extend Base Template in Views
7. Enable Messages 
```py
<!DOCTYPE html>
{% load static %}
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="shortcut icon" href="assets/favicon.ico" type="image/x-icon" />
    <link rel="stylesheet" href="{% static 'styles/style.css' %}" />
    <title>StudyBuddy - Find study partners around the world!</title>
  </head>

  <body>
   
    {% include "navbar.html" %}

    {% if messages %}
    <ul class="messages">
        {% for message in messages %}
        <li>{{ message }}</li>
        {% endfor %}
    </ul>
    {% endif %}
    
    {% block content %}
    
    {% endblock content %}

    <script src="{% static 'js/script.js' %}"></script>
  </body>
</html>
```
In the navigation bar,we can remove the navigation bar, logout the page and login page is active, add logo assests etc.

```py
 {% load static %}
 <header class="header header--loggedIn">
      <div class="container">
        <a href="{% url 'home' %}" class="header__logo">
          <img src="{% static 'images/logo.svg' %}"/>
          <h1>StudyBuddy</h1>
        </a>
        <form class="header__search" method="GET" action ="{% url 'home'%}">
          <label>
            <svg version="1.1" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32">
              <title>search</title>
              <path
                d="M32 30.586l-10.845-10.845c1.771-2.092 2.845-4.791 2.845-7.741 0-6.617-5.383-12-12-12s-12 5.383-12 12c0 6.617 5.383 12 12 12 2.949 0 5.649-1.074 7.741-2.845l10.845 10.845 1.414-1.414zM12 22c-5.514 0-10-4.486-10-10s4.486-10 10-10c5.514 0 10 4.486 10 10s-4.486 10-10 10z"
              ></path>
            </svg>
            <input name="q" placeholder="Search for rooms..." />
          </label>
        </form>
        <nav class="header__menu">
         

          <!-- Logged In -->

          {% if request.user.is_authenticated %}
          <div class="header__user">
            <a href="profile.html">
              <div class="avatar avatar--medium active">
                <img src="{{request.user.avatar.url}}" />
              </div>
              <p>{{request.user.username}} <span>@{{request.user.username}}</span></p>
            </a>
            <button class="dropdown-button">
              <svg version="1.1" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32">
                <title>chevron-down</title>
                <path d="M16 21l-13-13h-3l16 16 16-16h-3l-13 13z"></path>
              </svg>
            </button>
          </div>
          {% else %}
           <!-- Not Logged In -->
           <a href="{% url 'login' %}">
            <img src="{% static 'images/avatar.svg' %}" />
            <p>Login</p>
          </a> 

          {% endif %}
          <div class="dropdown-menu">
            <a href="{% url 'update-user' %}" class="dropdown-link"
              ><svg version="1.1" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32">
                <title>tools</title>
                <path
                  d="M27.465 32c-1.211 0-2.35-0.471-3.207-1.328l-9.392-9.391c-2.369 0.898-4.898 0.951-7.355 0.15-3.274-1.074-5.869-3.67-6.943-6.942-0.879-2.682-0.734-5.45 0.419-8.004 0.135-0.299 0.408-0.512 0.731-0.572 0.32-0.051 0.654 0.045 0.887 0.277l5.394 5.395 3.586-3.586-5.394-5.395c-0.232-0.232-0.336-0.564-0.276-0.887s0.272-0.596 0.572-0.732c2.552-1.152 5.318-1.295 8.001-0.418 3.274 1.074 5.869 3.67 6.943 6.942 0.806 2.457 0.752 4.987-0.15 7.358l9.392 9.391c0.844 0.842 1.328 2.012 1.328 3.207-0 2.5-2.034 4.535-4.535 4.535zM15.101 19.102c0.26 0 0.516 0.102 0.707 0.293l9.864 9.863c0.479 0.479 1.116 0.742 1.793 0.742 1.398 0 2.535-1.137 2.535-2.535 0-0.668-0.27-1.322-0.742-1.793l-9.864-9.863c-0.294-0.295-0.376-0.74-0.204-1.119 0.943-2.090 1.061-4.357 0.341-6.555-0.863-2.631-3.034-4.801-5.665-5.666-1.713-0.561-3.468-0.609-5.145-0.164l4.986 4.988c0.391 0.391 0.391 1.023 0 1.414l-5 5c-0.188 0.188-0.441 0.293-0.707 0.293s-0.52-0.105-0.707-0.293l-4.987-4.988c-0.45 1.682-0.397 3.436 0.164 5.146 0.863 2.631 3.034 4.801 5.665 5.666 2.2 0.721 4.466 0.604 6.555-0.342 0.132-0.059 0.271-0.088 0.411-0.088z"
                ></path>
              </svg>
              Settings</a
            >
            <a href="{% url 'logout' %} " class="dropdown-link"
              ><svg version="1.1" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32">
                <title>sign-out</title>
                <path
                  d="M3 0h22c0.553 0 1 0 1 0.553l-0 3.447h-2v-2h-20v28h20v-2h2l0 3.447c0 0.553-0.447 0.553-1 0.553h-22c-0.553 0-1-0.447-1-1v-30c0-0.553 0.447-1 1-1z"
                ></path>
                <path
                  d="M21.879 21.293l1.414 1.414 6.707-6.707-6.707-6.707-1.414 1.414 4.293 4.293h-14.172v2h14.172l-4.293 4.293z"
                ></path>
              </svg>
              Logout</a
            >
          </div>
        </nav>
      </div>
    </header>
<!-- {% if request.user.is_authenticated %}
<p>Hello {{request.user}}</p>
<a href="{% url 'logout' %}">Logout</a>
{% else %}
<a href="{% url 'login'%}">Login</a>
{% endif %}-->

```
In the activity_components , we acn edit the user profile ,room messages and the time since.

```py
<div class="activities">
    <div class="activities__header">
      <h2>Recent Activities</h2>
    </div>
  
    {% for message in room_messages %}
    <div class="activities__box">
      <div class="activities__boxHeader roomListRoom__header">
        <a href="{% url 'user-profile' message.user.id %}" class="roomListRoom__author">
          <div class="avatar avatar--small">
            <img src="{{message.user.avatar.url}}" />
          </div>
          <p>
            {{ message.user }}
            <span>{{ message.created|timesince }}</span>
          </p>
        </a>
  
        {% if request.user == message.user %}
        <div class="roomListRoom__actions">
          <a href="{% url 'delete-message' message.id %}">
            <svg version="1.1" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32">
              <title>remove</title>
              <path
                d="M27.314 6.019l-1.333-1.333-9.98 9.981-9.981-9.981-1.333 1.333 9.981 9.981-9.981 9.98 1.333 1.333 9.981-9.98 9.98 9.98 1.333-1.333-9.98-9.98 9.98-9.981z"
              ></path>
            </svg>
          </a>
        </div>
        {% endif %}
      </div>
  
      <div class="activities__boxContent">
        <p>replied to post “<a href="{% url 'room' message.room.id %}">{{ message.room }}</a>”</p>
        <div class="activities__boxRoomContent">
          {{ message.body }}
        </div>
      </div>
    </div>
    {% endfor %}
  </div>
```
In the room.html we can edit the room like `delete`,`update`,set `time` ,add `topics` in the users profile and remove threads.

```py
{% extends "main.html" %}    

{% block content %}
    <main class="profile-page layout layout--2">
      <div class="container">
        <!-- Room Start -->
        <div class="room">
          <div class="room__top">
            <div class="room__topLeft">
              <a href="{% url 'home' %}">
                <svg version="1.1" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32">
                  <title>arrow-left</title>
                  <path
                    d="M13.723 2.286l-13.723 13.714 13.719 13.714 1.616-1.611-10.96-10.96h27.625v-2.286h-27.625l10.965-10.965-1.616-1.607z"
                  ></path>
                </svg>
              </a>
              <h3>Study Room</h3>
            </div>
            {% if room.host == request.user %}
            <div class="room__topRight">
              <a href="{% url 'update-room' room.id %}">
                <svg
                  enable-background="new 0 0 24 24"
                  height="32"
                  viewBox="0 0 24 24"
                  width="32"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <title>edit</title>
                  <g>
                    <path d="m23.5 22h-15c-.276 0-.5-.224-.5-.5s.224-.5.5-.5h15c.276 0 .5.224.5.5s-.224.5-.5.5z" />
                  </g>
                  <g>
                    <g>
                      <path
                        d="m2.5 22c-.131 0-.259-.052-.354-.146-.123-.123-.173-.3-.133-.468l1.09-4.625c.021-.09.067-.173.133-.239l14.143-14.143c.565-.566 1.554-.566 2.121 0l2.121 2.121c.283.283.439.66.439 1.061s-.156.778-.439 1.061l-14.142 14.141c-.065.066-.148.112-.239.133l-4.625 1.09c-.038.01-.077.014-.115.014zm1.544-4.873-.872 3.7 3.7-.872 14.042-14.041c.095-.095.146-.22.146-.354 0-.133-.052-.259-.146-.354l-2.121-2.121c-.19-.189-.518-.189-.707 0zm3.081 3.283h.01z"
                      />
                    </g>
                    <g>
                      <path
                        d="m17.889 10.146c-.128 0-.256-.049-.354-.146l-3.535-3.536c-.195-.195-.195-.512 0-.707s.512-.195.707 0l3.536 3.536c.195.195.195.512 0 .707-.098.098-.226.146-.354.146z"
                      />
                    </g>
                  </g>
                </svg>
              </a>
              <a href="{% url 'delete-room' room.id %}">
                <svg version="1.1" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32">
                  <title>remove</title>
                  <path
                    d="M27.314 6.019l-1.333-1.333-9.98 9.981-9.981-9.981-1.333 1.333 9.981 9.981-9.981 9.98 1.333 1.333 9.981-9.98 9.98 9.98 1.333-1.333-9.98-9.98 9.98-9.981z"
                  ></path>
                </svg>
              </a>
            </div>
            {% endif  %}

            <!-- <button class="action-button" data-id="120" data-delete-url="https://randomuser.me/api/3324923"
            data-edit-url="profile.html">
            <svg version="1.1" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32">
              <title>ellipsis-horizontal</title>
              <path
                d="M16 7.843c-2.156 0-3.908-1.753-3.908-3.908s1.753-3.908 3.908-3.908c2.156 0 3.908 1.753 3.908 3.908s-1.753 3.908-3.908 3.908zM16 1.98c-1.077 0-1.954 0.877-1.954 1.954s0.877 1.954 1.954 1.954c1.077 0 1.954-0.877 1.954-1.954s-0.877-1.954-1.954-1.954z">
              </path>
              <path
                d="M16 19.908c-2.156 0-3.908-1.753-3.908-3.908s1.753-3.908 3.908-3.908c2.156 0 3.908 1.753 3.908 3.908s-1.753 3.908-3.908 3.908zM16 14.046c-1.077 0-1.954 0.877-1.954 1.954s0.877 1.954 1.954 1.954c1.077 0 1.954-0.877 1.954-1.954s-0.877-1.954-1.954-1.954z">
              </path>
              <path
                d="M16 31.974c-2.156 0-3.908-1.753-3.908-3.908s1.753-3.908 3.908-3.908c2.156 0 3.908 1.753 3.908 3.908s-1.753 3.908-3.908 3.908zM16 26.111c-1.077 0-1.954 0.877-1.954 1.954s0.877 1.954 1.954 1.954c1.077 0 1.954-0.877 1.954-1.954s-0.877-1.954-1.954-1.954z">
              </path>
            </svg>
          </button> -->
          </div>
          <div class="room__box scroll">
            <div class="room__header scroll">
              <div class="room__info">
                <h3>{{room.name}}</h3>
                <span>{{room.created|timesince}} ago</span>
              </div>
              <div class="room__hosted">
                <p>Hosted By</p>
                <a href="{% url 'user-profile' room.host.id %}" class="room__author">
                  <div class="avatar avatar--small">
                    <img src="https://randomuser.me/api/portraits/men/37.jpg" />
                  </div>
                  <span>@{{room.host.username}}</span>
                </a>
              </div>
              <!--<div class="room__details">
                Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quasi, tenetur laudantium? Dicta repellendus
                rerum consectetur, voluptatem repudiandae eum ea porro cupiditate provident nulla, deserunt, ab ipsum
                corporis laboriosam deleniti molestias?
              </div> -->
              <span class="room__topics">{{room.topic}}</span>
            </div>

            <div class="room__conversation">
              <div class="threads scroll">
                {% for message in room_messages %}
                <div class="thread">
                  <div class="thread__top">
                    <div class="thread__author">
                      <a href="{% url 'user-profile' message.user.id %}" class="thread__authorInfo">
                        <div class="avatar avatar--small">
                          <img src="{{message.user.avatar.url}}" />
                        </div>
                        <span>@{{message.user.username}}</span>
                      </a>
                      <span class="thread__date">{{message.created|timesince}} ago</span>
                    </div>

                    {% if request.user == message.user %}
                    <a href="{% url 'delete-message' message.id %}" >
                    <div class="thread__delete">
                      <svg version="1.1" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32">
                        <title>remove</title>
                        <path
                          d="M27.314 6.019l-1.333-1.333-9.98 9.981-9.981-9.981-1.333 1.333 9.981 9.981-9.981 9.98 1.333 1.333 9.981-9.98 9.98 9.98 1.333-1.333-9.98-9.98 9.98-9.981z"
                        ></path>
                      </svg>
                    </div>
                    </a>
                    {% endif %}
                  </div>
                  <div class="thread__details">
                   {{message.body}}
                  </div>
                </div>
                {% endfor %}
              </div>
            </div>
          </div>
          <div class="room__message">
            <form action="" method = "POST">
              {% csrf_token %}
              <input name="body" placeholder="Write your message here..." /></form>
            </form>
            </div>
        </div>
        <!-- Room End -->

        <!--   Start -->
        <div class="participants">
          <h3 class="participants__top">Participants <span>({{participants.count}} Joined)</span></h3>
          <div class="participants__list scroll">
            {% for user in participants %}
            <a href="{% url 'user-profile' user.id %}" class="participant">
              <div class="avatar avatar--medium">
                <img src="https://randomuser.me/api/portraits/men/37.jpg" />
              </div>
              <p>
                {{user.username}}
                <span>@{{user.username}}</span>
              </p>
            </a>
            {% endfor %}
          </div>
        </div>
        <!--  End -->
      </div>
    </main>
    <script src="script.js"></script>
  {% endblock %}
```
In the room_form.html, we can create the room ,`optional room name` ,add `topics name`,add `descriptions`.

```py
{% extends 'main.html' %}

{% block content %}
  <main class="create-room layout">
    <div class="container">
      <div class="layout__box">
        <div class="layout__boxHeader">
          <div class="layout__boxTitle">
            <a href="{% url 'home' %}">
              <svg version="1.1" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32">
                <title>arrow-left</title>
                <path
                  d="M13.723 2.286l-13.723 13.714 13.719 13.714 1.616-1.611-10.96-10.96h27.625v-2.286h-27.625l10.965-10.965-1.616-1.607z">
                </path>
              </svg>
            </a>
            <h3>Create/update Study Room</h3>
          </div>
        </div>
        <div class="layout__body">
          <form class="form" action="" method="post">
            {% csrf_token %}

            <div class="form__group">
              <label for="room_topic">Enter a topic</label>
              <input required type="text" value="{{room.topic.name}}" name="topic" list="topic-list" />
              <datalist id="topic-list">
                <select  id="room-topic">
                  {% for topic in topics %}
                  <option value="{{topic.name}}">{{topic.name}}</option>
                  {% endfor %}
                </select>
              </datalist>
            </div>

            

           
            <div class="form__group">
              <label for="room_name">Room Name</label>
              {{form.name}}
            </div>

              <div class="form__group">
                <label for="room_description">Room description</label>
                {{form.description}}

              <!--<input id="room_name" name="room_name" type="text" placeholder="E.g. Mastering Python + Django" />-->
            </div>
           

            <div class="form__group">
              <label for="room_about">About</label>
              <textarea name="room_about" id="room_about" placeholder="Write about your study group..."></textarea>
            </div>
            <div class="form__action">
              <a class="btn btn--dark" href="{% url 'home' %}">Cancel</a>
              <button class="btn btn--main" type="submit">submit</button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </main>
{% endblock content %}
```
In the profile.html, we can edit the profile ,`update` the `rooms`, `topics`,`recent activity`.

```py

{% extends 'main.html' %}


{% block content %}


  <main class="profile-page layout layout--3">
    <div class="container">
      <!-- Topics Start -->

      {% include 'base/topics_component.html' %}
      <!-- Topics End -->

      <!-- Room List Start -->
      <div class="roomList">
        <div class="profile">
          <div class="profile__avatar">
            <div class="avatar avatar--large active">
              <img src="https://randomuser.me/api/portraits/men/11.jpg" />
            </div>
          </div>
          <div class="profile__info">
            <h3>{{user.username}}</h3>
            <p>{{user.username}}</p>
            {% if request.user == user %}

            <a href="{% url 'update-user' %}" class="btn btn--main btn--pill">Edit Profile</a>
          {% endif %}
          </div>

          <div class="profile__about">
            <h3>About</h3>
            <p>
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Consequuntur illo tenetur
              facilis sunt nemo debitis quisquam hic atque aut? Ducimus alias placeat optio
              accusamus repudiandae quis ab ex exercitationem rem?
            </p>
          </div>
        </div>

        <div class="roomList__header">
          <div>
            <h2>Study Rooms Hosted by dennis_ivy</a>
            </h2>
          </div>
        </div>
     
        {% include 'base/feed_component.html' %}
      </div>
      <!-- Room List End -->

      <!-- Activities Start -->
      {% include 'base/activity_component.html' %}
      <!-- Activities End -->
    </div>
  </main>

 {% endblock content %}
```
```py
# studybud/base/views.py
@login_required(login_url='/login')
def createRoom(request):
    form = RoomForm()
    topics = Topic.objects.all()

    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)

        Room.objects.create(
            host=request.user,
            topic=topic,
            name=request.POST.get('name'),
            description=request.POST.get('description'),
        )
        return redirect('home')

    context = {'form': form, 'topics': topics}
    return render(request, 'base/room_form.html', context)
```
# `Edit User Account Page`

An `"Edit User Account Page"` is a webpage where users can update their personal information, like their username, email, and password. The page includes a form that users fill out to make changes. When they submit the form, the updated information is saved in the database.

In the views.py we can update the user .
```py
@login_required(login_url='/login')
def updateuser(request):
    user = request.user
    form = UserForm(instance=user)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)  # Use `user` instead of `User`
        if form.is_valid():
            form.save()
            return redirect('user-profile', pk=user.id)

    return render(request, 'base/update-user.html', {'form': form})
```
In the update-user.html we can create a user-friendly page for editing profile information. It sets up the layout, includes a form for updating user details, and provides navigation options. The page allows users to modify their profile data securely and either submit the changes or cancel the operation.

```py
{% extends 'main.html' %}
{% block content %}


    <main class="update-account layout">
        <div class="container">
            <div class="layout__box">
                <div class="layout__boxHeader">
                    <div class="layout__boxTitle">
                        <a href="{% url 'home' %}">
                            <svg version="1.1" xmlns="http://www.w3.org/2000/svg" width="32" height="32"
                                viewBox="0 0 32 32">
                                <title>arrow-left</title>
                                <path
                                    d="M13.723 2.286l-13.723 13.714 13.719 13.714 1.616-1.611-10.96-10.96h27.625v-2.286h-27.625l10.965-10.965-1.616-1.607z">
                                </path>
                            </svg>
                        </a>
                        <h3>Edit your profile</h3>
                    </div>
                </div>
                <div class="layout__body">
                    <form class="form" action="" method ="POST" enctype="mutipart/form-data">
                       {% csrf_token %}

                       {% for field in form %}
                        <div class="form__group">
                            <label for="profile_pic">{{field.label}}</label>
                            {{field}}
                        </div>
                        {% endfor %}

                        <div class="form__action">
                            <a class="btn btn--dark" href="index.html">Cancel</a>
                            <button class="btn btn--main" type="submit">Update</button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
      </div>
    </main>
 
{% endblock content %}
```
```py
# studybud/base/models.py
class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']
```
# `Make migrations`
```py
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
In `login_register.html`, the template displays either a login or registration form based on the `page` setting. Each form includes input fields, a submit button with an icon, and a link to switch forms.

```py
{% extends 'main.html' %}

{% block content %}

<main class="auth layout">

    {% if page == 'login' %}
    <div class="container">
        <div class="layout__box">
            <div class="layout__boxHeader">
                <div class="layout__boxTitle">
                    <h3>Login</h3>
                </div>
            </div>
            <div class="layout__body">
                <h2 class="auth__tagline">Find your study partner</h2>

                <form class="form" action="" method="POST">
                    {% csrf_token %}
                    <div class="form__group">
                        <label for="username">Email</label>
                        <input id="username" name="email" type="text" placeholder="e.g. dennis_ivy" />
                    </div>
                    <div class="form__group">
                        <label for="password">Password</label>
                        <input id="password" name="password" type="password" placeholder="&bull;&bull;&bull;&bull;&bull;&bull;&bull;&bull;" />
                    </div>

                    <button class="btn btn--main" type="submit">
                        <svg version="1.1" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32">
                            <title>lock</title>
                            <path d="M27 12h-1v-2c0-5.514-4.486-10-10-10s-10 4.486-10 10v2h-1c-0.553 0-1 0.447-1 1v18c0 0.553 0.447 1 1 1h22c0.553 0 1-0.447 1-1v-18c0-0.553-0.447-1-1-1zM8 10c0-4.411 3.589-8 8-8s8 3.589 8 8v2h-16v-2zM26 30h-20v-16h20v16z"></path>
                            <path d="M15 21.694v4.306h2v-4.306c0.587-0.348 1-0.961 1-1.694 0-1.105-0.895-2-2-2s-2 0.895-2 2c0 0.732 0.413 1.345 1 1.694z"></path>
                        </svg>

                        Login
                    </button>
                </form>

                <div class="auth__action">
                    <p>Haven't signed up yet?</p>
                    <a href="{% url 'register' %}" class="btn btn--link">Sign Up</a>
                </div>
            </div>
        </div>
    </div>
    {% else %}
    <div class="container">
        <div class="layout__box">
            <div class="layout__boxHeader">
                <div class="layout__boxTitle">
                    <h3>Register</h3>
                </div>
            </div>
            <div class="layout__body">
                <h2 class="auth__tagline">Find your study partner</h2>

                <form class="form" action="" method="POST">
                    {% csrf_token %}

                    {% for field in form %}

                    <div class="form__group">
                        <label for="{{ field.id_for_label }}">{{ field.label }}</label>
                        {{ field }}
                    </div>
                    {% endfor %}

                    <button class="btn btn--main" type="submit">
                        <svg version="1.1" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32">
                            <title>lock</title>
                            <path d="M27 12h-1v-2c0-5.514-4.486-10-10-10s-10 4.486-10 10v2h-1c-0.553 0-1 0.447-1 1v18c0 0.553 0.447 1 1 1h22c0.553 0 1-0.447 1-1v-18c0-0.553-0.447-1-1-1zM8 10c0-4.411 3.589-8 8-8s8 3.589 8 8v2h-16v-2zM26 30h-20v-16h20v16z"></path>
                            <path d="M15 21.694v4.306h2v-4.306c0.587-0.348 1-0.961 1-1.694 0-1.105-0.895-2-2-2s-2 0.895-2 2c0 0.732 0.413 1.345 1 1.694z"></path>
                        </svg>

                        Register
                    </button>
                </form>

                <div class="auth__action">
                    <p>Already signed up?</p>
                    <a href="{% url 'login' %}" class="btn btn--link">Login</a>
                </div>
            </div>
        </div>
    </div>
    {% endif %}
</main>

{% endblock content %}
```
# `Django Rest FrameWork`

Django Rest Framework  helps you `build APIs` for your Django app. It makes it easy to convert data to and `from JSON`,` handle requests`, and manage `user access`. It also supports features like paging through data, `filtering results, and includes a web interface for testing your API`.

# `Now we are just using JsonResponse`

`Install djangorestframework`

```py
pip install djangorestframework
```
# settings.py
INSTALLED_APPS = [
# .....
'rest_framework',
]

```py
#studybud/base/urls.py
urlpatterens=[
      path('api/',include('base.api.urls'))
]

```py
#studybud/base/api/views
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room
from .serializers import RoomSerializer


@api_view(['GET'])
def getRoutes(request):
    routes=[
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id',

    ]
    return Response(routes)

@api_view(['GET'])
def getRooms(request):
    rooms= Room.objects.all()
    serializer=RoomSerializer(rooms,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getRoom(request,pk):
    room= Room.objects.get(id=pk)
    serializer=RoomSerializer(room,many=False)
    return Response(serializer.data)
```

```py
#studybud/base/urls.py
from django.urls import path
from . import views

urlpatterns =[
    path('',views.getRoutes),
    path('rooms/',views.getRooms),
    path('rooms/<str:pk>/',views.getRoom),

]
```
we have to Serialize our model data, because we have our database setup, we have an item in that database, we need to render this data out in JSON format.

now we want to make queries to our database and return back the real data into our API instead of that static data.

```py
#studybud/base/api/views.py
@api_view(['GET'])
def getRooms(request):
    rooms= Room.objects.all()
    serializer=RoomSerializer(rooms,many=True)
    return Response(serializer.data)
```
we have to make a file called `serializer.py` in the base folder.
```py

Note:
Serializer is going to wrap our model and then turn it into a JSON object.
```
```py
#/base/api/serializer.py 
from rest_framework.serializers import ModelSerializer
from base.models import Room

class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
```
adding serializer to getRooms

```py
#/base/api/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Room, Topic, Message, User
from .forms import RoomForm, UserForm, MyUserCreationForm
from django.db.models import Q

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or Password does not exist')

    context = {'page': page}
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'base/login_register.html', {'form': form})

def home(request):
    q = request.GET.get('q') if request.GET.get('q') else ''
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
    )
    topics = Topic.objects.all()[:5]
    room_count = rooms.count()
    room_messages = Message.objects.filter(Q(room__topic__name__icontains=q))

    context = {'rooms': rooms, 'topics': topics, 'room_count': room_count, 'room_messages': room_messages}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    room_messages = room.message_set.all()
    participants = room.participants.all()

    if request.method == 'POST':
        message = Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('room', pk=room.id)

    context = {'room': room, 'room_messages': room_messages, 'participants': participants}
    return render(request, 'base/room.html', context)

def userProfile(request, pk):
    user = User.objects.get(id=pk)
    rooms = user.room_set.all()
    room_message = user.message_set.all()
    topics = Topic.objects.all()
    context = {'user': user, 'rooms': rooms, 'room_message': room_message, 'topics': topics}
    return render(request, 'base/profile.html', context)

@login_required(login_url='/login')
def createRoom(request):
    form = RoomForm()
    topics = Topic.objects.all()

    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)

        Room.objects.create(
            host=request.user,
            topic=topic,
            name=request.POST.get('name'),
            description=request.POST.get('description'),
        )
        return redirect('home')

    context = {'form': form, 'topics': topics}
    return render(request, 'base/room_form.html', context)

@login_required(login_url='/login')
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    topics = Topic.objects.all()

    if request.user != room.host:
        return HttpResponse('You are not allowed here!!')

    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)
        
        room.name = request.POST.get('name')
        room.topic = topic
        room.description = request.POST.get('description')
        room.save()
        return redirect('home')

    context = {'form': form, 'topics': topics, 'room': room}
    return render(request, 'base/room_form.html', context)

@login_required(login_url='/login')
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)

    if request.user != room.host:
        return HttpResponse('You are not allowed here!!')

    if request.method == 'POST':
        room.delete()
        return redirect('home')

    return render(request, 'base/delete.html', {'obj': room})

@login_required(login_url='/login')
def deleteMessage(request, pk):
    message = Message.objects.get(id=pk)

    if request.user != message.user:
        return HttpResponse('You are not allowed here!!')

    if request.method == 'POST':
        message.delete()
        return redirect('home')

    return render(request, 'base/delete.html', {'obj': message})

@login_required(login_url='/login')
def updateuser(request):
    user = request.user
    form = UserForm(instance=user)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)  # Use `user` instead of `User`
        if form.is_valid():
            form.save()
            return redirect('user-profile', pk=user.id)

    return render(request, 'base/update-user.html', {'form': form})


def topicsPage(request):
    q = request.GET.get('q') if request.GET.get('q') else ''
    topics = Topic.objects.filter(name__icontains=q)
    return render(request, 'base/topics.html', {'topics': topics})

def activityPage(request):
    room_messages = Message.objects.all()
    return render(request, 'base/activity.html', {'room_messages': room_messages})
```
```py
#studybud/api/example.html
<!DOCTYPE html>
<html>
<head>
    <meta charset='utf-8'>
    <meta http-equiv='X-UA-Compatible' content='IE=edge'>
    <title>Cool Rooms</title>
    <meta name='viewport' content='width=device-width, initial-scale=1'>
</head>
<body>

 <h1>Cools Rooms</h1>

 <div id="rooms-container"></div>
</body>
<script>
    let roomsContainer = document.getElementById('rooms-container');
    let getRooms = async () => {
        let response= await fetch('http://127.0.0.1:8000/api/rooms/')
        let rooms = await response.json()

        for (let i = 0; i < rooms.length; i++) {
        let room = rooms[i];

        let row = `<div>
                <h3>${room.name}</h3>
            </div>`
            
        roomsContainer.innerHTML += row
}
    }
getRooms()


</script>
</html>
```

steps:
1. import the model in the views.py
2. make a query to the database
3. serialize your data
4. import your serializer in the views.py
5. create the serializer object in the views.py and pass the querySet
6. go to the frontEnd and start the server.
7. our Real data has been rendered in to the frontend.

# `Customizing User Model`

We can create a completely `custom user model` by defining a new model and specifying it in your settings. 

This approach gives you full control over the user model, including `changing or adding fields and methods.`

```py
Note:
Customization allows you to  user authentication and profile management to the exact needs of our project.
```
we can completely create a new model.
```py
python -m django startproject customusermodel
python manage.py startapp base
```
we can configure the base app.

# settings.py
INSTALLED_APPS = [
# .....
,
]

now we can configure the authentications of new user model in the middleware of the settings.py.

```py
#customusermodel/settings.py
AUTH_USER_MODEL= 'base.User'
```
```py
#customusermodel/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    name= models.CharField(max_length=200, null=True)
    email=models.EmailField(unique=True)
    bio= models.TextField(null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
```
`Make Migrations`

```py
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
`Create superuser`

```py
python manage.py createsuperuser
``` 

Now we can register the user in the admin pannel.

```py
#customusermodel/base/admin.py
from django.contrib import admin
# Register your models here.
from .models import User
admin.site.register(User)
```
`Now we can register the user with the email`

```py
#//base/models.py
from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name= models.CharField(max_length=200, null=True)
    email=models.EmailField(unique=True)
    bio= models.TextField(null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
```
`Make Migrations`

```py
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
Now open the original project,

`setting up Virtual Environment`

```py
 pip install virtualenv
 virtualenv venv
```
Now we can delete the db.sqlit3 database and delate the migrations files because they can create an issue when we can migrate to all though previous migrate.

Now we can import the Absteractuser in the models.py

```py
#studybud/base/models.py
 from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)

    avatar = models.ImageField(null=True, default="avatar.svg")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
```

now we can configure the authentications of new user model in the middleware of the settings.py.

```py
#customusermodel/settings.py
AUTH_USER_MODEL= 'base.User'
```
`Make Migrations`

```py 
python manage.py makemigrations
python manage.py migrate
```
now we acn create the superuser

`createsuperuser`

```py
python manage.py createsuperuser
```
`now we can register the user in the admin panel`

```py
#//base/admin.py
from django.contrib import admin

# Register your models here.

from .models import Room ,Topic , Message , User

admin.site.register(User)
admin.site.register(Room)

admin.site.register(Topic)

admin.site.register(Message)
```
we will model our data in `models.py` for the image to use in the database with python we have to `install pillow`

```py
#//base/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)

    avatar = models.ImageField(null=True, default="avatar.svg")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]
```
now we have to `migrate our database` and Register that user model to the admin.py

```py
 python manage.py makemigrations
 python manage.py migrate
```
now we can root the media that users can tell where the users profile are uploaded.

```py
STATIC_URL = 'static/'
MEDIA_URL = '/images/'

STATICFILES_DIRS =[
    BASE_DIR / 'static'
]

MRDIA_ROOT= BASE_DIR / 'static/images'
```
now we can migrate the database , 
```py
 python manage.py makemigrations
 python manage.py migrate
```
now we can add the users profile picture, add bio ,username ,password etc and completely update the user profile in the models.py.

```py
#//base/form.py
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Room, User


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'name', 'username', 'email', 'bio']
```

```py
#//base/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Room, Topic, Message, User
from .forms import RoomForm, UserForm, MyUserCreationForm
from django.db.models import Q

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or Password does not exist')

    context = {'page': page}
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'base/login_register.html', {'form': form})

def home(request):
    q = request.GET.get('q') if request.GET.get('q') else ''
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
    )
    topics = Topic.objects.all()[:5]
    room_count = rooms.count()
    room_messages = Message.objects.filter(Q(room__topic__name__icontains=q))

    context = {'rooms': rooms, 'topics': topics, 'room_count': room_count, 'room_messages': room_messages}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    room_messages = room.message_set.all()
    participants = room.participants.all()

    if request.method == 'POST':
        message = Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('room', pk=room.id)

    context = {'room': room, 'room_messages': room_messages, 'participants': participants}
    return render(request, 'base/room.html', context)

def userProfile(request, pk):
    user = User.objects.get(id=pk)
    rooms = user.room_set.all()
    room_message = user.message_set.all()
    topics = Topic.objects.all()
    context = {'user': user, 'rooms': rooms, 'room_message': room_message, 'topics': topics}
    return render(request, 'base/profile.html', context)

@login_required(login_url='/login')
def createRoom(request):
    form = RoomForm()
    topics = Topic.objects.all()

    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)

        Room.objects.create(
            host=request.user,
            topic=topic,
            name=request.POST.get('name'),
            description=request.POST.get('description'),
        )
        return redirect('home')

    context = {'form': form, 'topics': topics}
    return render(request, 'base/room_form.html', context)

@login_required(login_url='/login')
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    topics = Topic.objects.all()

    if request.user != room.host:
        return HttpResponse('You are not allowed here!!')

    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)
        
        room.name = request.POST.get('name')
        room.topic = topic
        room.description = request.POST.get('description')
        room.save()
        return redirect('home')

    context = {'form': form, 'topics': topics, 'room': room}
    return render(request, 'base/room_form.html', context)

@login_required(login_url='/login')
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)

    if request.user != room.host:
        return HttpResponse('You are not allowed here!!')

    if request.method == 'POST':
        room.delete()
        return redirect('home')

    return render(request, 'base/delete.html', {'obj': room})

@login_required(login_url='/login')
def deleteMessage(request, pk):
    message = Message.objects.get(id=pk)

    if request.user != message.user:
        return HttpResponse('You are not allowed here!!')

    if request.method == 'POST':
        message.delete()
        return redirect('home')

    return render(request, 'base/delete.html', {'obj': message})

@login_required(login_url='/login')
def updateuser(request):
    user = request.user
    form = UserForm(instance=user)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)  # Use `user` instead of `User`
        if form.is_valid():
            form.save()
            return redirect('user-profile', pk=user.id)

    return render(request, 'base/update-user.html', {'form': form})


def topicsPage(request):
    q = request.GET.get('q') if request.GET.get('q') else ''
    topics = Topic.objects.filter(name__icontains=q)
    return render(request, 'base/topics.html', {'topics': topics})

def activityPage(request):
    room_messages = Message.objects.all()
    return render(request, 'base/activity.html', {'room_messages': room_messages})
```

```py
#//base/urls.py
from django.urls import path
from.import views
urlpatterns = [
    path('login/',views.loginPage, name="login"),
    path('logout/',views.logoutUser, name="logout"),
    path('register/',views.registerPage, name="register"),

    path("",views.home, name="home"),
    path('room/<str:pk>/',views.room,name="room"),
    path('profile/<str:pk>/', views.userProfile, name="user-profile"),

    path('create-room/', views.createRoom, name='create-room'),
    path('update-room/<str:pk>', views.updateRoom, name='update-room'),
    path('delete-room/<str:pk>', views.deleteRoom, name='delete-room'),
    path('delete-message/<str:pk>', views.deleteMessage, name='delete-message'),


    path('update-user/', views.updateuser, name='update-user'),
    
    path('topics/', views.topicsPage, name='topics'),
    path('activity/', views.activityPage, name='activity'),
    
]
```




