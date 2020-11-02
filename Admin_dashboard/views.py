from django.contrib.auth.models import User, auth
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib import messages
from alumni_management.models import *
from datetime import date

#for admin
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password, is_staff=True)

        if user is not None:
            auth.login(request, user)
            return redirect('Home')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('Login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('Login')


def home(request):
    return render(request, 'Admin.html')

def notice(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        description = request.POST['description']
        Date = date.today()

        notice = Notice.objects.create(Subject=subject, Description=description, IssueDate=Date)
        notice.save()
        return redirect('Notice')

    else:
        notice = Notice.objects.filter().order_by('-id')
        return render(request, 'Admin-Notice.html', {'notice':notice})


def delete_notice(request, id):
    Notice.objects.filter(id=id).delete()
    return redirect('Notice')


def gallery(request):
    if request.method == 'POST':
        img = request.FILES.get('image')        
        Date = request.POST['date']

        gallery = Gallery.objects.create(Image=img, EventDate=Date)
        gallery.save()
        return redirect('Gallery')

    else:
        gallery = Gallery.objects.filter().order_by('-id')
        return render(request, 'Admin-Gallery.html', {'gallery':gallery})


def delete_gallery(request, id):
    Gallery.objects.filter(id=id).delete()
    return redirect('Gallery')



def event(request):
    if request.method == 'POST':
        name = request.POST['name']
        img = request.FILES.get('image')
        description = request.POST['description']
        Date = request.POST['date']

        event = Event.objects.create(Image=img, EventName=name, Description=description, EventDate=Date)
        event.save()
        return redirect('Event')
    
    else:
        event = Event.objects.filter().order_by('-id')
        return render(request, 'Admin-Event.html', {'event':event})



def delete_event(request, id):
    Event.objects.filter(id=id).delete()
    return redirect('Event')


def job(request):
    if request.method == 'POST':
        name = request.POST['company-name']
        image = request.FILES.get('image')
        description = request.POST['description']
        location = request.POST['location']
        req1 = request.POST['req1']
        req2 = request.POST['req2']
        req3 = request.POST['req3']
        url = request.POST['url']

        job = Job.objects.create(Company_Name=name, Company_Image=image, Job_Description=description, location=location, Req1=req1, Req2=req2, Req3=req3, Url=url)
        job.save()
        return redirect('Job')

    else:
        job = Job.objects.filter().order_by('-id')
        return render(request, 'Admin-Job-Board.html', {'job':job})

def delete_job(request, id):
    Job.objects.filter(id=id).delete()
    return redirect('Job')


def search(request):
    if request.method == 'POST':
        year = request.POST['year']
        branch = request.POST['branch']
        Class = request.POST['class']

        Y = len(year)
        B = len(branch)
        C = len(Class)

        if Y==0 and B==0 and C==0:
            messages.error(request, 'NOT FOUND')
            return render(request, 'Admin-Search.html')
        if Y>0 and B==0 and C==0:
            user = Alumni.objects.filter(Q(Year=year))
        if Y==0 and B>0 and C==0:
            user = Alumni.objects.filter(Q(Branch=branch))
        if Y==0 and B==0 and C>0:
            user = Alumni.objects.filter(Q(Class=Class))
        if Y>0 and B>0 and C==0:
            user = Alumni.objects.filter(Q(Year=year) and Q(Branch=branch))
        if Y==0 and B>0 and C>0:
            user = Alumni.objects.filter(Q(Branch=branch) and Q(Class=Class))
        if Y>0 and B==0 and C>0:
            user = Alumni.objects.filter(Q(Year=year) and Q(Class=Class))
        if Y>0 and B>0 and C>0:
            user = Alumni.objects.filter(Q(Year=year) and Q(Branch=branch) and Q(Class=Class))

        if user is None:
            messages.error(request, 'NOT FOUND')
            year = Alumni.objects.all().distinct("Year")
            return render(request, 'Admin-Search.html', {'year':year})
        
        elif user.exists():
            year = Alumni.objects.all().distinct("Year")
            return render(request, 'Admin-Search.html', {'search' : user, 'year':year})
            user.clear()

        else:
            year = Alumni.objects.all().distinct("Year")
            messages.error(request, 'NOT FOUND')
            return render(request, 'Admin-Search.html', {'year':year})

    else:
        #year = Alumni.objects.values_list("Year").distinct()
        year = Alumni.objects.all().distinct("Year")
        return render(request, 'Admin-Search.html', {'year':year})


def delete_alumni(request, id):
    Alumni.objects.filter(Scholar_no=id).delete()
    user = User.objects.filter(id=id)
    user.delete()
    return redirect('Search')

def view_profile(request, id):
    alu = Alumni.objects.filter(Scholar_no=id)
    year = Alumni.objects.all().distinct("Year")
    return render(request, 'Admin-View-Profile.html', {'alumni':alu, 'year':year})