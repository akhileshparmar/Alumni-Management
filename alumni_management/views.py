from datetime import datetime

from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.core.files.storage import FileSystemStorage
from django.core.mail import EmailMessage, send_mail, send_mass_mail
from django.db.models import Q
from django.shortcuts import redirect, render

from Alumni_Tracking_System.settings import EMAIL_HOST_USER

from .models import *

fs = FileSystemStorage()




def home(request):
    event = Event.objects.filter().order_by('-id')[:3]
    notice = Notice.objects.filter().order_by('-id')[:2]
    
    return render(request, 'Index.html', {'event':event, 'notice':notice})

def About(request):
    return render(request, 'About.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password, is_active=True)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('/Login')

    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        img = request.FILES.get('image')
        email = request.POST['email']        
        password = request.POST['password']
        course = request.POST['course']
        branch = request.POST['branch']
        section = request.POST['section']
        enrollment = request.POST['enrollment']
        scholar = request.POST['scholar']
        year = request.POST['year']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        mobile = request.POST['mobile']        
        dob = request.POST['dob']        

        #datetime = datetime.now()

        if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Exists')
                return redirect('/Register')
        elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('/Register')
        elif User.objects.filter(id=scholar).exists():
                messages.info(request, 'Scholar no. Taken')
                return redirect('/Register')
        else:
            #alumni = Alumni
            alu = Alumni.objects.create(Firstname=firstname, Lastname=lastname, Img=img, Date_Of_Birth=dob, Email=email,Course=course, Branch=branch,  Section=section, Enrollment_no=enrollment, Scholar_no=scholar, Year=year, Address=address, City=city, State=state, Mobile_no=mobile)
            user = User.objects.create_user(is_active=False,username=username, password=password, email=email, first_name=firstname, last_name=lastname, id=scholar)
            alu.save()
            user.save()
            messages.info(request, 'Your Registration request has been sent to the Admin, You can login after Admin accept your request, please check after 1 working day')
            return redirect('/Register')

        
    else:
        return render(request, 'Register.html')

def email(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            email = request.user.email
            user_id = request.user.id
            
        subject = request.POST['subject']
        message = request.POST['message']
        date = datetime.today()
        EFA = Email_From_Alumni.objects.create(User_id=user_id, Email=email,Subject=subject,Message=message,Date=date)
        EFA.save()
        messages.info(request, 'Email sent')
        return redirect('/Email')
        
    else:
        return render(request, 'Email.html')

def feedback(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            email = request.user.email
            user_id = request.user.id
        feedback = request.POST['feedback']
        date = datetime.today()
        feedback = Feedback.objects.create(User_id=user_id,Email=email,Feedback=feedback,Date=date)
        feedback.save()
        messages.info(request, 'Feedback sent')
        return redirect('/Feedback')

    else:
        return render(request, 'Feedback.html')

def notices(request):
    notice = Notice.objects.filter().order_by('-id')
    return render(request, 'Notices.html', {'notice':notice})

def events(request):
    event = Event.objects.filter().order_by('-id')
    return render(request, 'Events.html', {'event':event})

def event_info(request, id):
    event = Event.objects.filter(id=id)
    return render(request, 'Events-info.html', {'event':event})

def job_board(request):
    job = Job.objects.filter().order_by('-id')
    return render(request, 'Job-board.html', {'job':job})    

def job_info(request, id):
    job = Job.objects.filter(id=id)
    return render(request, 'Job-info.html', {'job':job})

def gallery(request):
    gallery = Gallery.objects.filter().order_by('-id')
    return render(request, 'Gallery.html', {'gallery':gallery})

def image(request, id):
    gallery = Gallery.objects.filter(id=id)
    return render(request, 'Image.html', {'gallery':gallery})


def view_profile(request, id):
    alu = Alumni.objects.filter(Scholar_no=id)
                
    return render(request, 'View-Profile.html', {'alumni':alu})

def upload_image(request,id):
    if request.method == 'POST' and request.FILES['Image']:        
        image = request.FILES['Image']
        fs.save(image.name, image)
        Alumni.objects.filter(Scholar_no=id).update(Img=image)
        return redirect('/View-Profile/%d' % (id))

def edit_profile(request,id):
    if request.method == 'POST':        
        email = request.POST['email']
        mobile = request.POST['mobile']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']

        if len(email)!=0:
            Alumni.objects.filter(Scholar_no=id).update(Email=email)
            User.objects.filter(id=id).update(email=email)
        
        if len(mobile)!=0:
            Alumni.objects.filter(Scholar_no=id).update(Mobile_no=mobile)

        if len(address)!=0:
            Alumni.objects.filter(Scholar_no=id).update(Address=address)

        if len(city)!=0:
            Alumni.objects.filter(Scholar_no=id).update(City=city)

        if len(state)!=0:
            Alumni.objects.filter(Scholar_no=id).update(State=state)

        return redirect('/View-Profile/%d' % (id))

def update_credentials(request,id):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if len(username)!=0:
            if len(password)!=0:

                if User.objects.filter(username=username).exists():
                        messages.info(request, 'Username Exists')
                        return redirect('/View-Profile/%d' % (id))
                else:
                    User.objects.filter(id=id).update(username=username, password=password)
                    return redirect('/View-Profile/%d' % (id))
            else:
                messages.info(request, 'Check Username and password both')
                return redirect('/View-Profile/%d' % (id))

        else:
                messages.info(request, 'Check Username and password both')
                return redirect('/View-Profile/%d' % (id))        



#   ADMIN FUNCTIONS

def Admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password, is_staff=True, is_active=True)

        if user is not None:
            auth.login(request, user)
            return redirect('Admin-Home')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('/Admin')
    else:
        return render(request, 'Admin-login.html')


def Admin_logout(request):
    auth.logout(request)
    return redirect('/Admin')


def Admin_Home(request):
    return render(request, 'Admin.html')


def Admin_Notice(request): 
    mail_ids = []
    mail_ids_list = ['vermamayank5561@gmail.com','deepakchoudhary2030@gmail.com']
    mail_ids = User.objects.filter(Q(is_active=True) & Q(is_staff=False) & Q(is_superuser=False)).values_list("email").distinct("email")
    for x in mail_ids:
        mail_ids_list.extend(x)


    if request.method == 'POST':
        subject = request.POST['subject']
        description = request.POST['description']
        Date = datetime.today()

        notice = Notice.objects.create(Subject=subject, Description=description, IssueDate=Date)
        notice.save()
        send_mail(subject, description, EMAIL_HOST_USER, mail_ids_list)
        return redirect('Admin-Notice')

    else:        
        notice = Notice.objects.filter().order_by('-id')
        return render(request, 'Admin-Notice.html', {'notice':notice})


def delete_notice(request, id):
    Notice.objects.filter(id=id).delete()
    return redirect('Admin-Notice')


def Admin_Gallery(request):
    if request.method == 'POST':
        img = request.FILES.get('image')

        gallery = Gallery.objects.create(Image=img)
        gallery.save()
        return redirect('Admin-Gallery')

    else:
        gallery = Gallery.objects.filter().order_by('-id')
        return render(request, 'Admin-Gallery.html', {'gallery':gallery})


def delete_gallery(request, id):
    Gallery.objects.filter(id=id).delete()
    return redirect('Admin-Gallery')


def Admin_Email(request):
    mail_ids = []
    mail_ids_list = []
    mail_ids = User.objects.filter(Q(is_active=True) & Q(is_staff=False) & Q(is_superuser=False)).values_list("email").distinct("email")
    for x in mail_ids:
        mail_ids_list.extend(x)

    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']
        file = request.FILES.get('files')

        email = EmailMessage(subject, message, EMAIL_HOST_USER, mail_ids_list)
        email.content_subtype = 'html'

        if file:
            email.attach(file.name, file.read(), file.content_type)
            Email_To_Alumni.objects.create(Subject=subject,Message=message,Date=datetime.today(),File=file)
        else:
            Email_To_Alumni.objects.create(Subject=subject,Message=message,Date=datetime.today())

        #email.send()
        return redirect('Admin-Email')

    else:
        return render(request, 'Admin-Email.html')


def Admin_Event(request):
    mail_ids = []
    mail_ids_list = []
    mail_ids = User.objects.filter(Q(is_active=True) & Q(is_staff=False) & Q(is_superuser=False)).values_list("email").distinct("email")
    for x in mail_ids:
        mail_ids_list.extend(x)


    if request.method == 'POST':
        name = request.POST['name']
        img = request.FILES.get('image')
        description = request.POST['description']
        venue = request.POST['venue']
        date = request.POST['date']
        time = request.POST['time']

        file = request.FILES['image']
        event = Event.objects.create(Image=img, Name=name, Description=description, Venue=venue, Date=date, Time=time)
        event.save()

        message = "DESCRIPTION --> "+description+"||"+"VENUE --> "+venue+"||"+"DATE --> "+date+"||"+"Time --> "+time+"||\n"
        

        email = EmailMessage(name, message, EMAIL_HOST_USER, mail_ids_list)
        email.content_subtype = 'html'

        email.attach(file.name, file.read(), file.content_type)    
        email.send()

        return redirect('Admin-Event')
    
    else:
        event = Event.objects.filter().order_by('-id')
        return render(request, 'Admin-Event.html', {'event':event})


def delete_event(request, id):
    Event.objects.filter(id=id).delete()
    return redirect('/Admin-Event')


def Admin_Job(request):
    mail_ids = []
    mail_ids_list=[]
    mail_ids = User.objects.filter(Q(is_active=True) & Q(is_staff=False) & Q(is_superuser=False)).values_list("email").distinct("email")
    for x in mail_ids:
        mail_ids_list.extend(x)


    if request.method == 'POST':
        name = request.POST['name']
        image = request.FILES.get('image')
        title = request.POST['title']
        requirements = request.POST['requirements']
        description = request.POST['description']
        location = request.POST['location']
        salary = request.POST['salary']
        experience = request.POST['experience']
        process = request.POST['process']

        file = request.FILES['image']

        subject = "Job Alert"

        message = "COMPANY NAME --> "+name+"||"+"JOB TITLE --> "+title+"||"+"LOCATION --> "+location+"||\n"+"***FOR MORE DETAIL VISIT ALUMNI PORTAL JOB BOARD***"
        

        email = EmailMessage(subject, message, EMAIL_HOST_USER, mail_ids_list)
        email.content_subtype = 'html'

        email.attach(file.name, file.read(), file.content_type)      


        job = Job.objects.create(Company_Name=name, Company_Image=image,Job_Title= title ,Job_Prerequisite = requirements, Job_Description=description, Salary=salary, Experience=experience, location=location, Apply_Process=process)
        job.save()

        email.send()

        return redirect('/Admin-Job-Board')

    else:
        job = Job.objects.filter().order_by('-id')
        return render(request, 'Admin-Job-Board.html', {'job':job})


def delete_job(request, id):
    Job.objects.filter(id=id).delete()
    return redirect('/Admin-Job-Board')


def Admin_Search(request):
    if request.method == 'POST':
        year = request.POST['year']
        course = request.POST['course']
        branch = request.POST['branch']

        Y = len(year)
        C = len(course)
        B = len(branch)

        if Y==0 and B==0 and C==0:
            messages.error(request, 'NOT FOUND')
            return render(request, 'Admin-Search.html')
        if Y>0 and B==0 and C==0:
            user = Alumni.objects.filter(Q(Year=year)).order_by('Firstname')
        if Y==0 and B>0 and C==0:
            user = Alumni.objects.filter(Q(Branch=branch)).order_by('Firstname')
        if Y==0 and B==0 and C>0:
            user = Alumni.objects.filter(Q(Course=course)).order_by('Firstname')
        if Y>0 and B>0 and C==0:
            user = Alumni.objects.filter(Q(Branch=branch) and Q(Year=year)).order_by('Firstname')
        if Y==0 and B>0 and C>0:
            user = Alumni.objects.filter(Q(Branch=branch) and Q(Course=course)).order_by('Firstname')
        if Y>0 and B==0 and C>0:
            user = Alumni.objects.filter(Q(Year=year) and Q(Course=course)).order_by('Firstname')
        if Y>0 and B>0 and C>0:
            user = Alumni.objects.filter(Q(Year=year) and Q(Branch=branch) and Q(Course=course)).order_by('Firstname')

        if user is None:
            messages.error(request, 'NOT FOUND')
            return render(request, 'Admin-Search.html')
        
        elif user.exists():
            return render(request, 'Admin-Search.html', {'search' : user})
            user.clear()

        else:
            messages.error(request, 'NOT FOUND')
            return render(request, 'Admin-Search.html')

    else:
        return render(request, 'Admin-Search.html')


def Admin_View_Profile(request, id):
    alu = Alumni.objects.filter(Scholar_no=id)
    year = Alumni.objects.all().distinct("Year")
    return render(request, 'Admin-View-Profile.html', {'alumni':alu, 'year':year})
