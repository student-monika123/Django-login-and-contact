from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from blog.models import ContactUs
from django.core.mail import EmailMessage 
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def homepage(request):
    # return HttpResponse("this is my first blog....")
    # zx="data form from vies"

  
    return render(request, "home.html")#{"data":zx })

def aboutus(request):
    # return HttpResponse("this is my about page....")
    # table =[f"2 x {i} ={2*i}" for i in range(1,11)]
    return render(request,"aboutus.html")#{"mytable":table}) 

def contact(request):
    return render(request,"contact.html")

def services(request):
    return render(request,"services.html")

def servicesus(request):
    # ORM 
    my_data = ContactUs.objects.all().order_by("-id")

    context = {"records" : my_data}
    return render(request, "services.html", context)



def savethisdaa(request):
    if request.method == "POST":
        fullname = request.POST.get("fname")
        # fullname = request.POST["fname"]
        
        email = request.POST.get("email")
        phonenumer = request.POST.get("number")
        message = request.POST.get("msg")
        imx = request.FILES.get("imgg")
        print(imx), "sssssss"


        Myemailmessage = f'''This is user contact us from data
                            User Name: {fullname}
                            User Email: {email}
                            Phone Number: {phonenumer}
                            Message : {message}
                            THANK YOU :) '''
        # mail = EmailMessage("This Email Comming from Django", Myemailmessage, "mbhatia78071@gmail.com", ["mbhatia78071@gmail.com", "8628897753m@gmail.com"])
        # mail.send()



        mydata = ContactUs(username = fullname, useremail = email, phone_number = phonenumer, message = message, myimages = imx)
        mydata.save()

        messages.success(request, "Data save successfully")

        # return redirect("contact")
        return redirect("services")

    # return HttpResponse(f"data saved sucessfully.....! {fullname}, {email} {phonenumer}, {message}")



def deletethisdata(request,myid):
    # data= ContactUs.objects.all()
    data = ContactUs.objects.get(id=myid)

    messages.success(request, "Data Delete successfully")
    data.delete()
    # return HttpResponse(f"data deleted...{myid}")
    return redirect("services")



def updatethisdata(request,xyz):
    data = ContactUs.objects.get(id=xyz)
    return render(request,"contact-update.html",{"yourdata": data})


def updatedata(request, hey):
    if request.method == "POST":
        fullname = request.POST.get("fname")
        # fullname = request.POST["fname"]
        
        email = request.POST.get("email")
        phonenumer = request.POST.get("number")
        message = request.POST.get("msg")
        mydata = ContactUs.objects.get(id=hey)
        
        mydata.username = fullname
        mydata.useremail = email
        mydata.phone_number = phonenumer
        mydata.message = message
        mydata.save()

    return redirect ("services")



def searchhing(request):
    mysearchelement = request.GET['q']
    data= ContactUs.objects.filter(username=mysearchelement) or ContactUs.objects.filter(phone_number=mysearchelement)
    return render(request,"services.html",{"records": data})



def signup(request):
    if request.method == "POST":
        Username= request.POST.get("Username")
        email= request.POST.get("email")
        Password= request.POST.get("password")
        FullName= request.POST.get("FullName")
        saveuser= User.objects.create_user(username=Username, email=email, password=Password, first_name=FullName)
        messages.success(request, "SignUp successfully done...!")
        saveuser.save()

    return render(request,"signup.html")


def loginhere(request):
    if request.method == "POST":
        name= request.POST.get("username")
        password= request.POST.get("password")
        usercheck= authenticate(username=name,password=password)
        # print(usercheck,"check")
        if usercheck is not None:
            login(request,usercheck)
            messages.success(request, "Login successfully done...!")
        else:
            messages.warning(request, "Please enter valid username")
    return render(request,"login.html")


def logouthere(request):
    logout(request)
    return redirect("login")