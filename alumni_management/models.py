from django.db import models

# Create your models here.

class Alumni(models.Model):
    Firstname = models.CharField(max_length=20, null=True, default="")
    Lastname = models.CharField(max_length=20, null=True, default="")    
    Img = models.ImageField(upload_to='', blank=True)
    Date_Of_Birth = models.DateField(null=True)
    Email = models.EmailField(null=True, default="")
    Course = models.TextField(null=True, default="")
    Branch = models.TextField(null=True, default="")
    Section = models.TextField(null=True, default="")    
    Enrollment_no = models.TextField(max_length=20, null=True, default="")
    Scholar_no = models.IntegerField(default="", null=True)
    Year = models.TextField(null=True, default="")
    Address = models.TextField(null=True, default="")
    City = models.TextField(null=True, default="")
    State = models.TextField(null=True, default="")
    Mobile_no = models.TextField(null=True, default="")
    

    class meta:
        verbose_name = 'Alumni'
        verbose_name_plural = 'Alumni'

    def __str__(self):
        return self.Firstname+"_"+self.Lastname




class Notice(models.Model):
    Subject = models.CharField(blank=True, default="", max_length=50)
    Description = models.TextField(blank=True, default="")
    IssueDate = models.DateField(null=True)

    class meta:
        verbose_name = 'Notice'
        verbose_name_plural = 'Notices'

    def __str__(self):
        return self.Subject




class Event(models.Model):
    Image = models.ImageField(upload_to='media/Events')
    Name = models.CharField(blank=True, default="", max_length=25)
    Description = models.TextField(blank=True, default="")
    Venue = models.TextField(blank=True, default="")
    Time = models.TimeField(blank=True)
    Date = models.DateField(null=True)

    class meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    def __str__(self):
        return self.Name




class Gallery(models.Model):
    Image = models.ImageField(upload_to='media/Gallery')

    class meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'




class Job(models.Model):
    Company_Image = models.ImageField(upload_to='media/Jobs')
    Company_Name = models.CharField(blank=True, default="", max_length=50)
    Job_Title = models.CharField(blank=True, default="", max_length=50)
    Job_Description = models.TextField(blank=True, default="")
    Job_Prerequisite = models.TextField(blank=True, default="")    
    location = models.TextField(blank=True, default="")
    Experience = models.TextField(blank=True, default="")
    Salary = models.TextField(blank=True, default="")
    Apply_Process = models.TextField(blank=True, default="")

    class meta:
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'




class Email_From_Alumni(models.Model):
    User_id = models.IntegerField( null=True)
    Email = models.EmailField(blank=True, default="")
    Subject = models.TextField(blank=True, default="")
    Message = models.TextField(blank=True, default="")
    Date = models.DateField(null=True)

    class meta:
        verbose_name = 'Email'
        verbose_name_plural = 'Emails'




class Feedback(models.Model):
    User_id = models.IntegerField( null=True)
    Email = models.EmailField(blank=True, default="")
    Feedback = models.TextField(blank=True, default="")
    Date = models.DateField(null=True)

    class meta:
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedbacks'




class Email_To_Alumni(models.Model):
    Subject = models.TextField(blank=True, default="")
    Message = models.TextField(blank=True, default="")
    File = models.FileField(upload_to='Email/files', blank=True, null=True)
    Date = models.DateField(null=True)

    class meta:
        verbose_name = 'Email'
        verbose_name_plural = 'Emails'