from django.shortcuts import render
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# models
from myapp.models import Contact,Blogs




def index(request):
   return render(request,'index.html')
def about(request):
   return render(request,'about.html')

def contact(request):
    if request.method=="POST":
       name=request.POST['name']
       Email=request.POST['email']
       phone=request.POST['phone']
       Content =request.POST['content']
       if len(name)<2 or len(Email)<3 or len(phone)<10 or len(Content)<4:
             messages.error(request, "fill the form correctly")
       else:
            contact=Contact(name=name, Email=Email, phone=phone, Content=Content)
            contact.save()
            messages.info(request,"Thanks For Reaching Us! We will get back you soon....😊")
            return redirect('/contact')            
    return render(request, "contact.html")

def services(request):
   return render(request,'services.html')



# login api authentication
def handlelogin(request):
    if request.method=="POST":
        uname=request.POST.get("username")
        pass1=request.POST.get("pass1")
        myuser=authenticate(username=uname,password=pass1)
        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login Success")
            return redirect('/')
        else:
            messages.error(request,"Invalid Credentails")
            return redirect('/login')
    return render(request,'login.html')
 
   
def  handlesignup(request):
    if request.method=="POST":
        uname=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("pass1")
        confirmpassword=request.POST.get("pass2")
        if password!=confirmpassword:
            messages.warning(request,"Password is Incorrect")
            return redirect('/signup/')

        if len(uname)<5:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('/signup/')
        try:
            if User.objects.get(username=uname):
                messages.info(request,"UserName Is Taken")
                return redirect('/signup/')
        except:
            pass
        try:
            if User.objects.get(email=email):
                messages.info(request,"Email Is Taken")
                return redirect('/signup/')
        except:
            pass
    
        myuser=User.objects.create_user(uname,email,password)
        myuser.save()
        messages.success(request,"Signup Success Please login!")
        return redirect('/login/')
    return render(request,'signup.html')

def handlelogout(request):
   logout(request)
   messages.info(request,"Logout Success")
   return redirect('/')

# blog 


def bloghome(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Hey just login and Use my website")
        return redirect('/login')
    allPosts=Blogs.objects.all()
    context={'allPosts':allPosts}
    # return render(request,'blog.html',context)
    return render(request,'blog.html',context)

def blogposts(request,slug):
    post = Blogs.objects.filter(slug =slug)[0]
    context ={"post":post}
    return render (request,"blogpost.html",context)
   

def search(request):
    query=request.GET['search']
    if len(query)>100:
        allPosts=Blogs.objects.none()
    else:
        allPostsTitle=Blogs.objects.filter(title__icontains=query)
        allPostsDescription=Blogs.objects.filter(description__icontains=query)
        allPosts=allPostsTitle.union(allPostsDescription)
    if allPosts.count()==0:
        messages.warning(request,"No Search Results")
    params={'allPosts':allPosts,'query':query}

    return render(request,'search.html',params)