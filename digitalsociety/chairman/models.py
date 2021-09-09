from django.db import models
from django.db.models.base import Model

from django.db.models.deletion import CASCADE
import math
from django.utils import timezone

# Create your models here.
class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    otp = models.IntegerField(default=459)
    is_active = models.BooleanField(default=True)
    is_verfied = models.BooleanField(default=False)
    role = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True,blank=False)
    updated_at = models.DateTimeField(auto_now=True,blank=False)

    def __str__(self):
        return self.email

class Chairman(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20,blank=True)
    contact=models.CharField(max_length=20)
    house_no = models.CharField(max_length=20,null=True)
    vehicle_details = models.CharField(max_length=50,blank=True,null=True)
    family_members = models.CharField(max_length=100,blank=True,null=True)
    occupation = models.CharField(max_length=50,blank=True,null=True)
    job_address = models.CharField(max_length=100, blank=True,null=True)
    blood_grp = models.CharField(max_length=20,blank=True,null=True)
    birthdate = models.DateField(blank=True,null=True)
    marital_status = models.CharField(max_length=20,blank=True,null=True)

    profile_pic = models.FileField(upload_to="media\images", default="media\images\default.png")

    def __str__(self):
        return self.firstname

class Member(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20,blank=True)
    contact=models.CharField(max_length=20)
    house_no = models.CharField(max_length=20,null=True)
    vehicle_details = models.CharField(max_length=50,blank=True,null=True)
    family_members = models.CharField(max_length=100,blank=True,null=True)
    occupation = models.CharField(max_length=50,blank=True,null=True)
    job_address = models.CharField(max_length=100, blank=True,null=True)
    blood_grp = models.CharField(max_length=20,blank=True,null=True)
    birthdate = models.DateField(blank=True,null=True)
    marital_status = models.CharField(max_length=20,blank=True,null=True)

    profile_pic = models.FileField(upload_to="media\images", default="media\images\default.png")

    def __str__(self):
        return self.firstname

class NoticeBoard(models.Model):
    chairman_id = models.ForeignKey(Chairman,on_delete=models.CASCADE)
    subject = models.CharField(max_length=20)
    description = models.TextField(max_length=500)
    noticepic = models.FileField(upload_to="media\images", blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=False)
    updated_at = models.DateTimeField(auto_now=True,blank=False)

    def __str__(self):
        return self.subject

    def whenpublished(self):
            now = timezone.now()
            
            diff= now - self.created_at

            if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
                seconds= diff.seconds
                
                if seconds == 1:
                    return str(seconds) +  "second ago"
                
                else:
                    return str(seconds) + " seconds ago"

            if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
                minutes= math.floor(diff.seconds/60)

                if minutes == 1:
                    return str(minutes) + " minute ago"
                
                else:
                    return str(minutes) + " minutes ago"



            if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
                hours= math.floor(diff.seconds/3600)

                if hours == 1:
                    return str(hours) + " hour ago"

                else:
                    return str(hours) + " hours ago"

            # 1 day to 30 days
            if diff.days >= 1 and diff.days < 30:
                days = diff.days

                if days == 1 :
                    return str(days) + "day ago"

                else:
                    return str(days) + "days ago"

            if diff.days >= 30 and diff.days < 365:
                month = math.floor(diff.days/30)

                if month == 1:
                    return str(month) + "month ago"

                else:
                    return str(month) + "months ago"


            if diff.days >= 365 :
                year = math.floor(diff.day/365)

                if year == 1:
                    return str(year) + "year ago"

                else:
                    return str(year) + "years ago"

class Watchman(models.Model):
    user_id=models.ForeignKey(User,on_delete= models.CASCADE)
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20,blank=True)
    contact=models.CharField(max_length=20)
    address = models.TextField(max_length=300)
    gov_proof =models.FileField(upload_to="media\images", blank=True,null=True)
    police_varification_doc = models.FileField(upload_to="media\images", blank=True,null=True)

    profile_pic = models.FileField(upload_to="media\images", default="media\images\default.png")


    def __str__(self):
        return self.firstname

class Event(models.Model):
    chairman_id = models.ForeignKey(Chairman,on_delete=models.CASCADE)
    subject = models.CharField(max_length=20)
    description = models.TextField(max_length=500)
    eventpic = models.FileField(upload_to="media\images", blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=False)
    updated_at = models.DateTimeField(auto_now=True,blank=False)

    def __str__(self):
        return self.subject

    def whenpublished(self):
            now = timezone.now()
            
            diff= now - self.created_at

            if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
                seconds= diff.seconds
                
                if seconds == 1:
                    return str(seconds) +  "second ago"
                
                else:
                    return str(seconds) + " seconds ago"

            if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
                minutes= math.floor(diff.seconds/60)

                if minutes == 1:
                    return str(minutes) + " minute ago"
                
                else:
                    return str(minutes) + " minutes ago"



            if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
                hours= math.floor(diff.seconds/3600)

                if hours == 1:
                    return str(hours) + " hour ago"

                else:
                    return str(hours) + " hours ago"

            # 1 day to 30 days
            if diff.days >= 1 and diff.days < 30:
                days = diff.days

                if days == 1 :
                    return str(days) + "day ago"

                else:
                    return str(days) + "days ago"

            if diff.days >= 30 and diff.days < 365:
                month = math.floor(diff.days/30)

                if month == 1:
                    return str(month) + "month ago"

                else:
                    return str(month) + "months ago"


            if diff.days >= 365 :
                year = math.floor(diff.day/365)

                if year == 1:
                    return str(year) + "year ago"

                else:
                    return str(year) + "years ago"

class Complaintmember(models.Model):
    member_id = models.ForeignKey(Member,on_delete=models.CASCADE)
    subject = models.CharField(max_length=20)
    description = models.TextField(max_length=500)
    complaintpic = models.FileField(upload_to="media\images", blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=False)
    updated_at = models.DateTimeField(auto_now=True,blank=False)

    def __str__(self):
        return self.subject

    def whenpublished(self):
            now = timezone.now()
            
            diff= now - self.created_at

            if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
                seconds= diff.seconds
                
                if seconds == 1:
                    return str(seconds) +  "second ago"
                
                else:
                    return str(seconds) + " seconds ago"

            if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
                minutes= math.floor(diff.seconds/60)

                if minutes == 1:
                    return str(minutes) + " minute ago"
                
                else:
                    return str(minutes) + " minutes ago"



            if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
                hours= math.floor(diff.seconds/3600)

                if hours == 1:
                    return str(hours) + " hour ago"

                else:
                    return str(hours) + " hours ago"

            # 1 day to 30 days
            if diff.days >= 1 and diff.days < 30:
                days = diff.days

                if days == 1 :
                    return str(days) + "day ago"

                else:
                    return str(days) + "days ago"

            if diff.days >= 30 and diff.days < 365:
                month = math.floor(diff.days/30)

                if month == 1:
                    return str(month) + "month ago"

                else:
                    return str(month) + "months ago"


            if diff.days >= 365 :
                year = math.floor(diff.day/365)

                if year == 1:
                    return str(year) + "year ago"

                else:
                    return str(year) + "years ago"


            now = timezone.now()
            
            diff= now - self.created_at

            if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
                seconds= diff.seconds
                
                if seconds == 1:
                    return str(seconds) +  "second ago"
                
                else:
                    return str(seconds) + " seconds ago"

            if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
                minutes= math.floor(diff.seconds/60)

                if minutes == 1:
                    return str(minutes) + " minute ago"
                
                else:
                    return str(minutes) + " minutes ago"



            if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
                hours= math.floor(diff.seconds/3600)

                if hours == 1:
                    return str(hours) + " hour ago"

                else:
                    return str(hours) + " hours ago"

            # 1 day to 30 days
            if diff.days >= 1 and diff.days < 30:
                days = diff.days

                if days == 1 :
                    return str(days) + "day ago"

                else:
                    return str(days) + "days ago"

            if diff.days >= 30 and diff.days < 365:
                month = math.floor(diff.days/30)

                if month == 1:
                    return str(month) + "month ago"

                else:
                    return str(month) + "months ago"


            if diff.days >= 365 :
                year = math.floor(diff.day/365)

                if year == 1:
                    return str(year) + "year ago"

                else:
                    return str(year) + "years ago"


    
            now = timezone.now()
            
            diff= now - self.created_at

            if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
                seconds= diff.seconds
                
                if seconds == 1:
                    return str(seconds) +  "second ago"
                
                else:
                    return str(seconds) + " seconds ago"

            if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
                minutes= math.floor(diff.seconds/60)

                if minutes == 1:
                    return str(minutes) + " minute ago"
                
                else:
                    return str(minutes) + " minutes ago"



            if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
                hours= math.floor(diff.seconds/3600)

                if hours == 1:
                    return str(hours) + " hour ago"

                else:
                    return str(hours) + " hours ago"

            # 1 day to 30 days
            if diff.days >= 1 and diff.days < 30:
                days = diff.days

                if days == 1 :
                    return str(days) + "day ago"

                else:
                    return str(days) + "days ago"

            if diff.days >= 30 and diff.days < 365:
                month = math.floor(diff.days/30)

                if month == 1:
                    return str(month) + "month ago"

                else:
                    return str(month) + "months ago"


            if diff.days >= 365 :
                year = math.floor(diff.day/365)

                if year == 1:
                    return str(year) + "year ago"

                else:
                    return str(year) + "years ago"


            now = timezone.now()
            
            diff= now - self.created_at

            if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
                seconds= diff.seconds
                
                if seconds == 1:
                    return str(seconds) +  "second ago"
                
                else:
                    return str(seconds) + " seconds ago"

            if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
                minutes= math.floor(diff.seconds/60)

                if minutes == 1:
                    return str(minutes) + " minute ago"
                
                else:
                    return str(minutes) + " minutes ago"



            if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
                hours= math.floor(diff.seconds/3600)

                if hours == 1:
                    return str(hours) + " hour ago"

                else:
                    return str(hours) + " hours ago"

            # 1 day to 30 days
            if diff.days >= 1 and diff.days < 30:
                days = diff.days

                if days == 1 :
                    return str(days) + "day ago"

                else:
                    return str(days) + "days ago"

            if diff.days >= 30 and diff.days < 365:
                month = math.floor(diff.days/30)

                if month == 1:
                    return str(month) + "month ago"

                else:
                    return str(month) + "months ago"


            if diff.days >= 365 :
                year = math.floor(diff.day/365)

                if year == 1:
                    return str(year) + "year ago"

                else:
                    return str(year) + "years ago"

class Complaintwatchman(models.Model):
    watchman_id = models.ForeignKey(Watchman,on_delete= models.CASCADE)
    
    subject = models.CharField(max_length=20)
    description = models.TextField(max_length=500)
    complaintpic = models.FileField(upload_to="media\images", blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=False)
    updated_at = models.DateTimeField(auto_now=True,blank=False)

    def __str__(self):
        return self.subject

    def whenpublished(self):
            now = timezone.now()
            
            diff= now - self.created_at

            if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
                seconds= diff.seconds
                
                if seconds == 1:
                    return str(seconds) +  "second ago"
                
                else:
                    return str(seconds) + " seconds ago"

            if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
                minutes= math.floor(diff.seconds/60)

                if minutes == 1:
                    return str(minutes) + " minute ago"
                
                else:
                    return str(minutes) + " minutes ago"



            if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
                hours= math.floor(diff.seconds/3600)

                if hours == 1:
                    return str(hours) + " hour ago"

                else:
                    return str(hours) + " hours ago"

            # 1 day to 30 days
            if diff.days >= 1 and diff.days < 30:
                days = diff.days

                if days == 1 :
                    return str(days) + "day ago"

                else:
                    return str(days) + "days ago"

            if diff.days >= 30 and diff.days < 365:
                month = math.floor(diff.days/30)

                if month == 1:
                    return str(month) + "month ago"

                else:
                    return str(month) + "months ago"


            if diff.days >= 365 :
                year = math.floor(diff.day/365)

                if year == 1:
                    return str(year) + "year ago"

                else:
                    return str(year) + "years ago"


            now = timezone.now()
            
            diff= now - self.created_at

            if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
                seconds= diff.seconds
                
                if seconds == 1:
                    return str(seconds) +  "second ago"
                
                else:
                    return str(seconds) + " seconds ago"

            if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
                minutes= math.floor(diff.seconds/60)

                if minutes == 1:
                    return str(minutes) + " minute ago"
                
                else:
                    return str(minutes) + " minutes ago"



            if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
                hours= math.floor(diff.seconds/3600)

                if hours == 1:
                    return str(hours) + " hour ago"

                else:
                    return str(hours) + " hours ago"

            # 1 day to 30 days
            if diff.days >= 1 and diff.days < 30:
                days = diff.days

                if days == 1 :
                    return str(days) + "day ago"

                else:
                    return str(days) + "days ago"

            if diff.days >= 30 and diff.days < 365:
                month = math.floor(diff.days/30)

                if month == 1:
                    return str(month) + "month ago"

                else:
                    return str(month) + "months ago"


            if diff.days >= 365 :
                year = math.floor(diff.day/365)

                if year == 1:
                    return str(year) + "year ago"

                else:
                    return str(year) + "years ago"


    
            now = timezone.now()
            
            diff= now - self.created_at

            if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
                seconds= diff.seconds
                
                if seconds == 1:
                    return str(seconds) +  "second ago"
                
                else:
                    return str(seconds) + " seconds ago"

            if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
                minutes= math.floor(diff.seconds/60)

                if minutes == 1:
                    return str(minutes) + " minute ago"
                
                else:
                    return str(minutes) + " minutes ago"



            if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
                hours= math.floor(diff.seconds/3600)

                if hours == 1:
                    return str(hours) + " hour ago"

                else:
                    return str(hours) + " hours ago"

            # 1 day to 30 days
            if diff.days >= 1 and diff.days < 30:
                days = diff.days

                if days == 1 :
                    return str(days) + "day ago"

                else:
                    return str(days) + "days ago"

            if diff.days >= 30 and diff.days < 365:
                month = math.floor(diff.days/30)

                if month == 1:
                    return str(month) + "month ago"

                else:
                    return str(month) + "months ago"


            if diff.days >= 365 :
                year = math.floor(diff.day/365)

                if year == 1:
                    return str(year) + "year ago"

                else:
                    return str(year) + "years ago"


            now = timezone.now()
            
            diff= now - self.created_at

            if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
                seconds= diff.seconds
                
                if seconds == 1:
                    return str(seconds) +  "second ago"
                
                else:
                    return str(seconds) + " seconds ago"

            if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
                minutes= math.floor(diff.seconds/60)

                if minutes == 1:
                    return str(minutes) + " minute ago"
                
                else:
                    return str(minutes) + " minutes ago"



            if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
                hours= math.floor(diff.seconds/3600)

                if hours == 1:
                    return str(hours) + " hour ago"

                else:
                    return str(hours) + " hours ago"

            # 1 day to 30 days
            if diff.days >= 1 and diff.days < 30:
                days = diff.days

                if days == 1 :
                    return str(days) + "day ago"

                else:
                    return str(days) + "days ago"

            if diff.days >= 30 and diff.days < 365:
                month = math.floor(diff.days/30)

                if month == 1:
                    return str(month) + "month ago"

                else:
                    return str(month) + "months ago"


            if diff.days >= 365 :
                year = math.floor(diff.day/365)

                if year == 1:
                    return str(year) + "year ago"

                else:
                    return str(year) + "years ago"

class Visitors(models.Model):
    watchman_id = models.ForeignKey(Watchman,on_delete= models.CASCADE)
    member_name = models.CharField(max_length=30)
    
    # visitor 
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30,blank=True)
    contact = models.CharField(max_length=30)
    date = models.DateField()
    time = models.TimeField()

class Transaction(models.Model):
    made_by = models.ForeignKey(Member,related_name='transactions',on_delete=models.CASCADE)
    made_on = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    order_id = models.CharField(unique=True,max_length=100,null=True,blank=True)
    checksum = models.CharField(max_length=100,null=True,blank=True)

    def save(self,*args,**kwargs):
        if self.order_id is None and self.made_on and self.id:
            self.order_id = self.made_on.strftime('PAY2ME%Y%m%dODR')+str(self.id)
        return super().save(*args,**kwargs)

    def __str__(self):
        return self.order_id

class Webvisitor(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    subject=models.CharField(max_length=50,blank=True)
    message=models.TextField(max_length=500,blank=True)

    def __str__(self):
        return self.name



    



    

