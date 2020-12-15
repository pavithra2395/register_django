from django.shortcuts import render,redirect
import pymongo
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.

client = pymongo.MongoClient('localhost:27017')
db = client.trial_1
col = db.user
user_data = {"username":"pavithra", "name":"pavithra.p@lincode.us", "password":"lincode@548",
             "username":"meghana", "name":"meghana.naik@lincode.us", "password":"lincode@500",
             "username":"arushi", "name":"arushi.a@lincode.us", "password":"lincode@504",
             "username":"manju", "name":"manju.R@lincode.us", "password":"lincode@506",
             "username":"pooja", "name":"pooja.R@lincode.us", "password":"lincode@5078"}
result = col.insert_one(user_data)

# get= list(db.user.find({}))

def welcome(request):
    return render(request,'lc.html')



def register(request):

    if request.method == 'POST':
        # first_name = request.POST['first_name']
        # last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['psw']
        # password1 = request.POST['psw-repeat']


        #
        # if User.objects.filter(username=username).exists():
        #     messages.info(request, "user already exists")
        #     return redirect('register')
        #
        # elif User.objects.filter(email=email).exists():
        #     messages.info(request, "email taken")
        #     return redirect('register')
        #
        # else:
        if email.endswith('@lincode.us'):
            user = User.objects.create_user(username=username, email=email,password=password)
            user.save();
            return redirect('http://127.0.0.1:8000/register_app/welcome/')
            # return redirect('http://127.0.0.1:8000/loginpage/')
        else:
            messages.error(request,'something Went wrong')
            return redirect('http://127.0.0.1:8000/register_app/register/')
                # messages.info(request, 'user created')
            # return redirect('login')

    #
    # else:
    #
    #     return render(request, "register.html")

    return render(request,"register.html")

def login(request):

    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.error(request,'invalid credentials')
            return redirect(login)
    else:
        return render(request,'Hello.html')