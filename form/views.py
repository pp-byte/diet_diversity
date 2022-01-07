from django.shortcuts import render,redirect
from .forms import chk, chkform

from .models import table,new_item
from .forms import AddressForm
from django.contrib.auth import login, authenticate ,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import auth,User
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from .forms import CreateUserForm
from .forms import  UploadWellPictureForm
from .models import UploadWellPictureModel,Profile
import re
import random

import http.client

from django.conf import settings
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
import base64
import time
from django.http import HttpResponse
from django.core.mail import send_mail
import math, random

# def include(request):
#     if request.method=="POST":
#         print("this is post")
#     return render(request,'base.html')

def about(request):
    if request.method=="POST":
        print("this is post")
    return render(request,'about.html')



def language(request):
    if request.method=="POST":
       print("this is post")
    return render(request,'language.html')

# def hindi(request):
#     if request.method=="POST":
#        print("this is post")
#     return render(request,'hindi.html')

def index(request):
    form=chkform()
    data=request
    print(data.GET.keys())
    print(data.POST.keys())
    if request.method=="POST":
        form = chkform(request.POST)
        if form.is_valid():
            # form.save()
            print("this is post")
        # print(data.POST['op'])
       # print(request.POST['tab'])
        # if request.POST.get('submit'):
        #    print(request.POST.get('table'))
        recipe_name=request.POST['recipe_name']
        daily_freq=request.POST['daily_freq']
        weekly_freq=request.POST['weekly_freq']
        monthly_freq=request.POST['monthly_freq']
        quan=request.POST['quan']
        unit=request.POST['unit']
        consistency=request.POST['consistency']
        remark=request.POST['remark']
        Tabular=table(recipe_name=recipe_name,daily_freq=daily_freq,weekly_freq=weekly_freq,monthly_freq=monthly_freq,unit=unit,quan=quan,consistency=consistency,remark=remark)
        Tabular.save()
        # if request.POST.get('submit'):
        #    print(request.POST.get('Tabular'))
        # else:
        # # print(Recipe_List)
        #    print(Tabular)
            # Tabular.save()
    form=chkform()
    return render(request,'index.html',{'form':form})

# def login_request(request):
# 	if request.method == "POST":
# 		form = AuthenticationForm(request, data=request.POST)
# 		if form.is_valid():
# 			email = form.cleaned_data.get('email')
# 			password = form.cleaned_data.get('password')
# 			user = authenticate(email=email, password=password)
# 			if user is not None:
# 				login(request, user)
# 				messages.info(request, f"You are now logged in as {email}.")
# 				return redirect("/")
# 			else:
# 				messages.error(request,"Invalid email or password.")
# 		else:
# 			messages.error(request,"Invalid email or password.")
# 	form = AddressForm()
# 	return render(request=request, template_name="login.html", context={"form":form})


# def register_request(request):
#     form = CreateUserForm()
#     if request.method == 'POST':
#         form = CreateUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             user = form.cleaned_data.get('email')
#             messages.success(request, "Account was created for " + user)
#             return redirect('login')
#     context = {'form':form}
#     return render(request, "register.html", context)

def new_recipe(request):
    form=chk()
    data=request
    print(data.GET.keys())
    print(data.POST.keys())
    if request.method=="POST":
        form = chkform(request.POST)
        if form.is_valid():
            # form.save()
            print("this is post")
        # print(data.POST['op'])
       # print(request.POST['tab'])
        # if request.POST.get('submit'):
        #    print(request.POST.get('table'))
        recipe_name=request.POST['recipe_name']
        daily_freq=request.POST['daily_freq']
        weekly_freq=request.POST['weekly_freq']
        monthly_freq=request.POST['monthly_freq']
        quan=request.POST['quan']
        unit=request.POST['unit']
        consistency=request.POST['consistency']
        remark=request.POST['remark']
        Item=new_item(recipe_name=recipe_name,daily_freq=daily_freq,weekly_freq=weekly_freq,monthly_freq=monthly_freq,unit=unit,quan=quan,consistency=consistency,remark=remark)
        Item.save()
        # print("this is post")
    form=chk()
    # if request.method == "POST":
    return render(request,'new_recipe.html', context={"form":form})

# def login_request(request):
# 	if request.method == "POST":
# 		form = AuthenticationForm(request, data=request.POST)
# 		if form.is_valid():
# 			username = form.cleaned_data.get('username')
# 			password = form.cleaned_data.get('password')
# 			user = authenticate(username=username, password=password)
# 			if user is not None:
# 				login(request, user)
# 				messages.info(request, f"You are now logged in as {username}.")
# 				return redirect("/")
# 			else:
# 				messages.error(request,"Invalid username or password.")
# 		else:
# 			messages.error(request,"Invalid username or password.")
# 	form = AuthenticationForm()
# 	return render(request=request, template_name="login.html", context={"login_form":form})

def logout(request):
    auth.logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('/')


def captwellpic(request):
    form = UploadWellPictureForm()
    global datauri
    if request.is_ajax():
        datauri = request.POST['picture']
    
    if request.method == 'POST' and not request.is_ajax():
        form = UploadWellPictureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        name = request.POST.get('name')
        well_nm = request.POST.get('well_nm')
        try:
            imgstr = re.search(r'base64,(.*)', datauri).group(1)
            data = ContentFile(base64.b64decode(imgstr))
            myfile = "WellPics/profile-"+time.strftime("%Y%m%d-%H%M%S")+".png"
            fs = FileSystemStorage()
            filename = fs.save(myfile, data)
            picLocation = UploadWellPictureModel.objects.create(picture=filename, name=name,well_nm=well_nm)
            picLocation.save()
            datauri= False
            del datauri
        except NameError:
            print("Image is not captured")
    else:
        form = UploadWellPictureForm()
    return render(request,'capture.html',{})

def uploadwellpic(request):
    if request.method == 'POST':
        form = UploadWellPictureForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            instance.user = request.user
            instance.save()
            messages.success(request, "Registration successful." )
            print("data is saved.")
            return redirect('/captwellpic')
    else:
        form = UploadWellPictureForm()
    return render(request,'upload.html',{})


# def generateOTP() :
#     digits = "0123456789"
#     OTP = ""
#     for i in range(4) :
#         OTP += digits[math.floor(random.random() * 10)]
#     return OTP

# def send(request):
#     email=request.GET.get("email")
#     o=generateOTP()
#     htmlgen = '<p>Your OTP is <strong>'+o+'</strong></p>'
#     send_mail('OTP request',o,'<gmail id>',[email],fail_silently=False,html_message=htmlgen)
#     return HttpResponse(o)

# def otp(request):
#     return render(request, "otp.html")



def send_otp(mobile , otp):
    print("FUNCTION CALLED")
    conn = http.client.HTTPSConnection("api.msg91.com")
    # authkey = settings.authKey
    headers = { 'content-type': "application/json" }
    # payload = "{\"Value1\":\"Param1\",\"Value2\":\"Param2\",\"Value3\":\"Param3\"}"
    # conn.request("GET", "/api/v5/otp?template_id=&mobile=&authkey=mobile",headers)
    url = "http://control.msg91.com/api/sendotp.php?otp="+otp+"&message="+"Your otp is "+otp +"&mobile="+mobile+"&authkey="+mobile+"&country=91"
    conn.request("GET", url , headers=headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))
    return None



def login_attempt(request):
    if request.method == 'POST':
        mobile = request.POST.get('mobile')
        
        user = Profile.objects.filter(mobile = mobile).first()
        
        if user is None:
            context = {'message' : 'User not found' , 'class' : 'danger' }
            return render(request,'logins.html' , context)
        
        otp = str(random.randint(1000 , 9999))
        user.otp = otp
        user.save()
        # send_otp(mobile , otp)
        request.session['mobile'] = mobile
        return redirect('/login_otp')        
    return render(request,'logins.html')


def login_otp(request):
    mobile = request.session['mobile']
    context = {'mobile':mobile}
    if request.method == 'POST':
        otp = request.POST.get('otp')
        profile = Profile.objects.filter(mobile=mobile).first()
        
        if otp == profile.otp:
            user = User.objects.get(id = profile.user.id)
            login(request , user)
            return redirect('/')
        else:
            context = {'message' : 'Wrong OTP' , 'class' : 'danger','mobile':mobile }
            return render(request,'login_otp.html' , context)
    
    return render(request,'login_otp.html' , context)
    
    

def register_otp(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        username = request.POST.get('username')
        mobile = request.POST.get('mobile')
        
        check_user = User.objects.filter(password=password).first()
        check_profile = Profile.objects.filter(mobile = mobile).first()
        
        if check_user or check_profile:
            context = {'message' : 'User already exists' , 'class' : 'danger' }
            return render(request,'register_otp.html' , context)
            
        user = User(password=password, username = username)
        user.save()
        otp = str(random.randint(1000 , 9999))
        profile = Profile(user = user , mobile=mobile , otp = otp) 
        profile.save()
        # send_otp(mobile, otp)
        request.session['mobile'] = mobile
        return redirect('otps')
    return render(request,'register_otp.html')

def otps(request):
    mobile = request.session['mobile']
    context = {'mobile':mobile}
    if request.method == 'POST':
        otp = request.POST.get('otp')
        profile = Profile.objects.filter(mobile=mobile).first()
        if otp == profile.otp:
            return redirect('/')
        else:
            print('Wrong')
            
            context = {'message' : 'Wrong OTP' , 'class' : 'danger','mobile':mobile }
            return render(request,'otps.html' , context)
            
        
    return render(request,'otps.html' , context)