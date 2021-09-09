from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect
from .utils import *
from django.urls import reverse
from django.shortcuts import redirect
import random
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .paytm import generate_checksum, verify_checksum
import datetime


# Create your views here.

def home(request):
    
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        
        if uid.role=="chairman":
            cid=Chairman.objects.get(user_id=uid)
            mall = Member.objects.all()
            c_mall = Member.objects.all().count()
            nall = NoticeBoard.objects.all()
            c_nall = NoticeBoard.objects.all().count()
            vall = Visitors.objects.all()
            c_vall = Visitors.objects.all().count()
            eall = Event.objects.all()

            return render(request,"chairman/index.html",{'uid':uid,'cid':cid,'mall':mall,'eall':eall,'c_mall':str(c_mall),'nall':nall,'c_nall':str(c_nall),'vall':vall,'c_vall':str(c_vall)})

        elif uid.role=="member":
            mid=Member.objects.get(user_id=uid)
            mall = Member.objects.all()
            c_mall = Member.objects.all().count()
            nall = NoticeBoard.objects.all()
            c_nall = NoticeBoard.objects.all().count()
            vall = Visitors.objects.all()
            c_vall = Visitors.objects.all().count()
            eall = Event.objects.all()
            c_eall = Event.objects.all().count()

            return render(request,"chairman/index1.html",{'uid':uid,'mid':mid,'mall':mall,'eall':eall,'c_mall':str(c_mall),'nall':nall,'c_nall':str(c_nall),'vall':vall,'c_vall':str(c_vall),'c_eall':str(c_eall)})

        else:
            wid=Watchman.objects.get(user_id=uid)
            mall = Member.objects.all()
            c_mall = Member.objects.all().count()
            nall = NoticeBoard.objects.all()
            c_nall = NoticeBoard.objects.all().count()
            vall = Visitors.objects.all()
            c_vall = Visitors.objects.all().count()
            eall = Event.objects.all()
            c_eall = Event.objects.all().count()

            return render(request,"chairman/index2.html",{'uid':uid,'wid':wid,'mall':mall,'eall':eall,'c_mall':str(c_mall),'nall':nall,'c_nall':str(c_nall),'vall':vall,'c_vall':str(c_vall),'c_eall':str(c_eall)})
            
    else:
        return render(request,"chairman/home.html")
    
def reset_password(request):
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        newpassword = request.POST['newpassword']
        repassword = request.POST['repassword']

        uid = User.objects.get(email=email)
        if uid.is_verfied:
            pass
        else:
            if uid.password==password and newpassword==repassword:
                uid.password=newpassword  #set your new password
                uid.is_verfied=True
                uid.save()  #update
                
                s_msg="successfully reset password"
                return render(request,"chairman/login.html",{'s_msg':s_msg})
                #return HttpResponsePermanentRedirect(reverse('login'))
            else:
                o_msg="Newpassword and confirmpassword aere not same "
                return render(request,"chairman/resetpassword.html",{'o_msg':o_msg}) 

    else:
        return render(request,"chairman/resetpassword.html")

def login(request):
    if "email" in request.session:
        return redirect("home")

    else:
        try:
            if request.POST:
                uid = User.objects.get(email=request.POST['email'])
                if uid.password==request.POST['password']:
                    if uid.role=="chairman":
                        cid=Chairman.objects.get(user_id=uid)
                        if uid.is_verfied:                            
                            request.session['email']=uid.email
                            mall = Member.objects.all()
                            c_mall = Member.objects.all().count()
                            nall = NoticeBoard.objects.all()
                            c_nall = NoticeBoard.objects.all().count()
                            vall = Visitors.objects.all()
                            c_vall = Visitors.objects.all().count()
                            eall = Event.objects.all()

                            return render(request,"chairman/index.html",{'uid':uid,'cid':cid,'mall':mall,'c_mall':str(c_mall),'nall':nall,'eall':eall,'c_nall':str(c_nall),'vall':vall,'c_vall':str(c_vall)})
                        else:
                            return render(request,"chairman/resetpassword.html",{'uid':uid})                       
                        
                    elif uid.role=="member":
                        #member and watchmen  login code
                        mid=Member.objects.get(user_id=uid)

                        if uid.is_verfied:
                            request.session['email']=uid.email
                            mid=Member.objects.get(user_id=uid)
                            mall = Member.objects.all()
                            c_mall = Member.objects.all().count()
                            nall = NoticeBoard.objects.all()
                            c_nall = NoticeBoard.objects.all().count()
                            vall = Visitors.objects.all()
                            c_vall = Visitors.objects.all().count()
                            eall = Event.objects.all()
                            c_eall = Event.objects.all().count()
                            return render(request,"chairman/index1.html",{'uid':uid,'mid':mid,'mall':mall,'eall':eall,'c_mall':str(c_mall),'nall':nall,'c_nall':str(c_nall),'vall':vall,'c_vall':str(c_vall),'c_eall':str(c_eall)})
                        else:
                            return render(request,"chairman/resetpassword.html",{'uid':uid})

                    else:
                        wid=Watchman.objects.get(user_id=uid)

                        if uid.is_verfied:
                            request.session['email']=uid.email
                            mall = Member.objects.all()
                            c_mall = Member.objects.all().count()
                            nall = NoticeBoard.objects.all()
                            c_nall = NoticeBoard.objects.all().count()
                            vall = Visitors.objects.all()
                            c_vall = Visitors.objects.all().count()
                            eall = Event.objects.all()
                            c_eall = Event.objects.all().count()
                            return render(request,"chairman/index2.html",{'uid':uid,'wid':wid,'mall':mall,'eall':eall,'c_mall':str(c_mall),'nall':nall,'c_nall':str(c_nall),'vall':vall,'c_vall':str(c_vall),'c_eall':str(c_eall)})
                        else:
                            return render(request,"chairman/resetpassword.html",{'uid':uid})

                else:
                    p_msg="invalid password"
                    return render(request,"chairman/login.html",{'p_msg':p_msg})


            else:
                return render(request,"chairman/login.html")
        except:
            e_msg="invalid Email or Password"
            return render(request,"chairman/login.html",{'e_msg':e_msg})

def forgot_password(request):
    if request.POST:
        try:
            email = request.POST['email']
            uid = User.objects.get(email=email)
            if uid:
                otp=random.randint(1111,9999)
                uid.otp = otp
                uid.save() 
                sendmail("FORGOT-PASSWORD",'otp-template',email,{'otp':str(otp)})
                return render(request,'chairman/reset-password.html',{'uid':uid,'email':email})
        except:
            e_msg = "Email does not exist"
            return render(request,'chairman/forgot-password.html',{'e_msg':e_msg})
    else:
        return render(request,'chairman/forgot-password.html') 

def reset_forgot_password(request):
    if request.POST:
        email = request.POST['email']
        otp = request.POST['otp']
        newpassword = request.POST['newpassword']
        repassword = request.POST['repassword']

        uid=User.objects.get(email = email)

        if otp == str(otp):
            if newpassword==repassword:
                uid.password = newpassword
                uid.save()
                s1_msg="successfully reset password"
                return render(request,"chairman/login.html",{'s1_msg':s1_msg})
            else:
                e_msg = "new password and re password was not same"
                return render(request,'chairman/reset-password',{'e_msg':e_msg})
        else:
            o_msg = "invalid OTP"
            return render(request,'chairman/reset-password',{'o_msg':o_msg})
    return render(request,'chairman/reset-password')       



def logout(request):
    if "email" in request.session:
        del request.session['email']
        return render(request,"chairman/home.html")
    else:
        return render(request,"chairman/home.html")
    
def chairman_profile(request):
    uid = User.objects.get(email=request.session['email'])
    cid = Chairman.objects.get(user_id=uid)
    return render(request,'chairman/profile.html',{'uid':uid,'cid':cid})

def reset_profile_password(request):
    uid = User.objects.get(email=request.session['email'])
    cid = Chairman.objects.get(user_id=uid)

    currentpassword=request.POST['currentpassword']
    newpassword=request.POST['newpassword']

    if uid.password == currentpassword:
        uid.password=newpassword
        uid.save()
        return render(request,"chairman/login.html")

    else:
        #msg="invalid password"
        return render(request,'chairman/profile.html',{'uid':uid,'cid':cid})

def reset_profile(request):
    uid = User.objects.get(email=request.session['email'])
    cid = Chairman.objects.get(user_id=uid)

    if request.POST:

        cid.firstname=request.POST['firstname']
        cid.lastname=request.POST['lastname']
        
        cid.contact=request.POST['contact']
        cid.house_no=request.POST['house_no']
        cid.vehicle_details=request.POST['vehicle_details']
        cid.family_members=request.POST['family_members']
        cid.occupation=request.POST['occupation']
        cid.job_address=request.POST['job_address']
        cid.blood_grp=request.POST['blood_grp']
        
        cid.marital_status=request.POST['marital_status']
        
        if request.FILES:
            cid.profile_pic=request.FILES['profile_pic']
            cid.save()

        
        cid.save()  
        return render(request,'chairman/profile.html',{'uid':uid,'cid':cid})                  
    return render(request,'chairman/profile.html',{'uid':uid,'cid':cid})

def add_member(request):
    uid = User.objects.get(email=request.session['email'])
    cid = Chairman.objects.get(user_id=uid)
    
    if request.POST:
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        contact = request.POST['contact']
        contact=request.POST['contact']
        house_no=request.POST['house_no']
        vehicle_details=request.POST['vehicle_details']
        family_members=request.POST['family_members']
        occupation=request.POST['occupation']
        job_address=request.POST['job_address']
        blood_grp=request.POST['blood_grp']
        # birthdate=request.POST['birthdate']
        marital_status=request.POST['marital_status']
         
        role = request.POST['role']
        li=["43","89","37","76","92","56","88"]
        ch=random.choice(li)
        password = firstname[1:]+contact[3:6]+email[3:6]+ch

        if role=="member":
            mall=Member.objects.all()
            uid = User.objects.create(email=email,password=password,role=role)
            if request.FILES:
                profile_pic = request.FILES['profile_pic']            
                mid = Member.objects.create(user_id=uid,firstname=firstname,contact=contact,lastname=lastname,profile_pic=profile_pic,house_no=house_no,vehicle_details=vehicle_details,family_members=family_members,occupation=occupation,job_address=job_address,blood_grp=blood_grp,marital_status=marital_status)
            else:
                mid = Member.objects.create(user_id=uid,firstname=firstname,contact=contact,lastname=lastname,house_no=house_no,vehicle_details=vehicle_details,family_members=family_members,occupation=occupation,job_address=job_address,blood_grp=blood_grp,marital_status=marital_status) 
            subject="WELCOME TO Skyline Residency"
            sendmail(subject,'maintemplate',email,{'firstname':firstname,'password':password})
           
            
            return render(request,"chairman/viewmember.html",{'uid':uid,'cid':cid,'mall':mall})

        return render(request,"chairman/addmember.html",{'uid':uid,'cid':cid})

    return render(request,"chairman/addmember.html",{'uid':uid,'cid':cid})

def view_member(request):
    uid = User.objects.get(email=request.session['email'])
    cid = Chairman.objects.get(user_id=uid)
    mall = Member.objects.all()

    return render(request,"chairman/viewmember.html",{'uid':uid,'cid':cid,'mall':mall})

def view_member1(request):
    uid = User.objects.get(email=request.session['email'])
    mid = Member.objects.get(user_id=uid)
    mall = Member.objects.exclude(user_id=uid)

    return render(request,"chairman/viewmember1.html",{'uid':uid,'mid':mid,'mall':mall})

def view_member_profile(request,pk):
    memberid = Member.objects.get(id = pk) #for respected selected user
    uid = User.objects.get(email=request.session['email']) #logged in user
    cid = Chairman.objects.get(user_id=uid)
    return render(request,'chairman/member-profile.html',{'uid':uid,'memberid':memberid,'cid':cid})

def view_member_profile1(request,pk):
    memberid = Member.objects.get(id = pk) #for respected selected user
    uid = User.objects.get(email=request.session['email']) #logged in user
    mid = Member.objects.get(user_id=uid)
    return render(request,'chairman/member-profile1.html',{'uid':uid,'memberid':memberid,'mid':mid})

def notice(request):
    if "email" in request.session:
        uid = User.objects.get(email=request.session['email'])
        cid = Chairman.objects.get(user_id=uid)
        if request.POST:
            nall = NoticeBoard.objects.all()
            subject = request.POST['subject']
            description = request.POST['description']
            if "noticepic" in request.FILES:
                noticepic = request.FILES['noticepic']
                nid = NoticeBoard.objects.create(chairman_id=cid,subject=subject,description=description,noticepic=noticepic)
            
            else:
                nid = NoticeBoard.objects.create(chairman_id=cid,subject=subject,description=description)


            return render(request,"chairman/notice-details.html",{'uid':uid,'cid':cid,'nall':nall})
        else:
            return render(request,"chairman/notice-page.html",{'uid':uid,'cid':cid})
    else:
        return HttpResponseRedirect(reverse('login'))

def notice_view(request):
    uid = User.objects.get(email=request.session['email'])
    cid = Chairman.objects.get(user_id=uid)

    nall = NoticeBoard.objects.all()

    return render(request,"chairman/notice-details.html",{'uid':uid,'cid':cid,'nall':nall})

def delete_notice(request,pk):
    uid = User.objects.get(email=request.session['email']) #logged in user
    cid = Chairman.objects.get(user_id=uid)
    nall = NoticeBoard.objects.all()
    noticeid = NoticeBoard.objects.get(id = pk)
    noticeid.delete()
    return render(request,'chairman/notice-details.html',{'uid':uid,'noticeid':noticeid,'cid':cid,'nall':nall})

def add_watchman(request):
    uid = User.objects.get(email= request.session['email'])
    cid = Chairman.objects.get(user_id = uid)
    if request.POST and request.FILES:
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        contact = request.POST['contact']
        address = request.POST['address']
        gov_proof = request.FILES['gov_proof']
        police_varification_doc = request.FILES['police_varification_doc']
        profile_pic=request.FILES['profile_pic']


        role = request.POST['role']
        li=["43","89","37","76","92","56","88"]
        ch=random.choice(li)
        password = firstname[1:]+contact[3:6]+email[3:6]+ch

        if role=="watchman":
            uid = User.objects.create(email=email,password=password,role=role)
            Wid = Watchman.objects.create(user_id=uid,firstname=firstname,contact=contact,lastname=lastname,address=address,gov_proof=gov_proof,police_varification_doc=police_varification_doc,profile_pic=profile_pic)
            wall = Watchman.objects.all()
            subject="WELCOME TO Skyline Residency"
            sendmail(subject,'maintemplate',email,{'firstname':firstname,'password':password})
            
            return render(request,"chairman/viewwatchman.html",{'uid':uid,'cid':cid,'wall':wall})

        return render(request,"chairman/addwatchman.html",{'uid':uid,'cid':cid})

    return render(request,"chairman/addwatchman.html",{'uid':uid,'cid':cid})

def view_watchman(request):
    uid = User.objects.get(email=request.session['email'])
    cid = Chairman.objects.get(user_id=uid)
    wall = Watchman.objects.all()

    return render(request,"chairman/viewwatchman.html",{'uid':uid,'cid':cid,'wall':wall})

def view_watchman_profile(request,pk):
    watchmanid = Watchman.objects.get(id = pk) #for respected selected user
    uid = User.objects.get(email=request.session['email']) #logged in user
    cid = Chairman.objects.get(user_id=uid)
    return render(request,'chairman/watchman-profile.html',{'uid':uid,'watchmanid':watchmanid,'cid':cid})

def member_profile(request):
    uid = User.objects.get(email=request.session['email'])
    mid = Member.objects.get(user_id=uid)
    return render(request,'chairman/profile1.html',{'uid':uid,'mid':mid})

def reset_profile1_password(request):
    uid = User.objects.get(email=request.session['email'])
    mid = Member.objects.get(user_id=uid)

    currentpassword=request.POST['currentpassword']
    newpassword=request.POST['newpassword']

    if uid.password == currentpassword:
        uid.password=newpassword
        uid.save()
        s2_msg ="password successfully updated"
        return render(request,"chairman/login.html",{'s2_msg':s2_msg})

    else:
        #msg="invalid password"
        return render(request,'chairman/profile1.html',{'uid':uid,'mid':mid})

def reset_profile1(request):
    uid = User.objects.get(email=request.session['email'])
    mid = Member.objects.get(user_id=uid)

    if request.POST:

        mid.firstname=request.POST['firstname']
        mid.lastname=request.POST['lastname']
        
        mid.contact=request.POST['contact']
        mid.firstname=request.POST['firstname']
        mid.lastname=request.POST['lastname']
        
        mid.contact=request.POST['contact']
        mid.house_no=request.POST['house_no']
        mid.vehicle_details=request.POST['vehicle_details']
        mid.family_members=request.POST['family_members']
        mid.occupation=request.POST['occupation']
        mid.job_address=request.POST['job_address']
        mid.blood_grp=request.POST['blood_grp']
        
        mid.marital_status=request.POST['marital_status']
        
        if request.FILES:
            mid.profile_pic=request.FILES['profile_pic']

        
        mid.save()                    
    return render(request,'chairman/profile1.html',{'uid':uid,'mid':mid})

def watchman_profile(request):
    uid = User.objects.get(email=request.session['email'])
    wid = Watchman.objects.get(user_id=uid)
    return render(request,'chairman/profile2.html',{'uid':uid,'wid':wid})

def reset_profile2_password(request):
    uid = User.objects.get(email=request.session['email'])
    wid = Watchman.objects.get(user_id=uid)

    currentpassword=request.POST['currentpassword']
    newpassword=request.POST['newpassword']

    if uid.password == currentpassword:
        uid.password=newpassword
        uid.save()
        s3_msg = "Sucessfully password updated"
        return render(request,"chairman/login.html",{'s3_msg':s3_msg})

    else:
        #msg="invalid password"
        return render(request,'chairman/profile2.html',{'uid':uid,'wid':wid})

def reset_profile2(request):
    uid = User.objects.get(email=request.session['email'])
    wid = Watchman.objects.get(user_id=uid)

    if request.POST:

        
        
        wid.contact=request.POST['contact']
        
        if request.FILES:
            wid.profile_pic=request.FILES['profile_pic']

        
        wid.save()                    
    return render(request,'chairman/profile2.html',{'uid':uid,'wid':wid})

def notice1_view(request):
    uid = User.objects.get(email=request.session['email'])
    mid = Member.objects.get(user_id=uid)

    nall = NoticeBoard.objects.all()

    return render(request,"chairman/notice1-details.html",{'uid':uid,'mid':mid,'nall':nall})

def notice2_view(request):
    uid = User.objects.get(email=request.session['email'])
    wid = Watchman.objects.get(user_id=uid)

    nall = NoticeBoard.objects.all()

    return render(request,"chairman/notice2-details.html",{'uid':uid,'wid':wid,'nall':nall})

def event(request):
    if "email" in request.session:
        uid = User.objects.get(email=request.session['email'])
        cid = Chairman.objects.get(user_id=uid)
        if request.POST:
            eall = Event.objects.all()
            subject = request.POST['subject']
            description = request.POST['description']
            if "eventpic" in request.FILES:
                eventpic = request.FILES['eventpic']
                eid = Event.objects.create(chairman_id=cid,subject=subject,description=description,eventpic=eventpic)
            
            else:
                eid = Event.objects.create(chairman_id=cid,subject=subject,description=description)


            return render(request,"chairman/event-details.html",{'uid':uid,'cid':cid,'eall':eall})
        else:
            return render(request,"chairman/event-page.html",{'uid':uid,'cid':cid})
    else:
        return HttpResponseRedirect(reverse('login'))

def event_view(request):
    uid = User.objects.get(email=request.session['email'])
    cid = Chairman.objects.get(user_id=uid)

    eall = Event.objects.all()

    return render(request,"chairman/event-details.html",{'uid':uid,'cid':cid,'eall':eall})

def delete_event(request,pk):
    uid = User.objects.get(email=request.session['email']) #logged in user
    cid = Chairman.objects.get(user_id=uid)
    eall = Event.objects.all()
    eventid = Event.objects.get(id = pk)
    eventid.delete()
    return render(request,'chairman/event-details.html',{'uid':uid,'eventid':eventid,'cid':cid,'eall':eall})

def event1_view(request):
    uid = User.objects.get(email=request.session['email'])
    mid = Member.objects.get(user_id=uid)

    eall = Event.objects.all()

    return render(request,"chairman/event1-details.html",{'uid':uid,'mid':mid,'eall':eall})

def event2_view(request):
    uid = User.objects.get(email=request.session['email'])
    wid = Watchman.objects.get(user_id=uid)

    eall = Event.objects.all()

    return render(request,"chairman/event2-details.html",{'uid':uid,'wid':wid,'eall':eall})

def member_complaint(request):
    if "email" in request.session:
        uid = User.objects.get(email=request.session['email'])
        mid = Member.objects.get(user_id=uid)
        if request.POST:
            subject = request.POST['subject']
            description = request.POST['description']
            if "complaintpic" in request.FILES:
                complaintpic = request.FILES['complaintpic']
                coid = Complaintmember.objects.create(member_id=mid,subject=subject,description=description,complaintpic=complaintpic)
            
            else:
                coid = Complaintmember.objects.create(member_id=mid,subject=subject,description=description)

            s_msg = "complaint add Successfully"
            
            return render(request,"chairman/complaint1-page.html",{'uid':uid,'mid':mid,'s_msg':s_msg})
        else:
            return render(request,"chairman/complaint1-page.html",{'uid':uid,'mid':mid})
    else:
        return HttpResponseRedirect(reverse('login'))

def watchman_complaint(request):
    if "email" in request.session:
        uid = User.objects.get(email=request.session['email'])
        wid = Watchman.objects.get(user_id=uid)
        if request.POST:
            subject = request.POST['subject']
            description = request.POST['description']
            if "complaintpic" in request.FILES:
                complaintpic = request.FILES['complaintpic']
                coid2 = Complaintwatchman.objects.create(watchman_id=wid,subject=subject,description=description,complaintpic=complaintpic)
            
            else:
                coid2 = Complaintwatchman.objects.create(watchman_id=wid,subject=subject,description=description)

            s_msg = "complaint add Successfully"
            
            return render(request,"chairman/complaint2-page.html",{'uid':uid,'wid':wid,'s_msg':s_msg})
        else:
            return render(request,"chairman/complaint2-page.html",{'uid':uid,'wid':wid})
    else:
        return HttpResponseRedirect(reverse('login'))

def member_complaint_view(request):
    uid = User.objects.get(email=request.session['email'])
    cid = Chairman.objects.get(user_id=uid)

    call1 = Complaintmember.objects.all()

    return render(request,"chairman/member-complaint-details.html",{'uid':uid,'cid':cid,'call1':call1})

def watchman_complaint_view(request):
    uid = User.objects.get(email=request.session['email'])
    cid = Chairman.objects.get(user_id=uid)

    call2 = Complaintwatchman.objects.all()

    return render(request,"chairman/watchman-complaint-details.html",{'uid':uid,'cid':cid,'call2':call2})

def add_visitors(request):
    if "email" in request.session:
        uid = User.objects.get(email=request.session['email'])
        wid = Watchman.objects.get(user_id=uid)
        mall= Member.objects.all()
        try:
            if request.POST:
                member_name = request.POST['member_name']
                firstname = request.POST['firstname']
                lastname = request.POST['lastname']
                date = request.POST['date']
                time = request.POST['time']
                contact = request.POST['contact']
                
                vall = Visitors.objects.create(watchman_id=wid,member_name=member_name,firstname=firstname,lastname=lastname,date=date,time=time,contact=contact)
                all =Visitors.objects.all()
                return render(request,"chairman/viewvisitors2.html",{'uid':uid,'wid':wid,'mall':mall,'all':all})
            else:
                return render(request,"chairman/add-visitors.html",{'uid':uid,'wid':wid,'mall':mall})
        except:
            return render(request,"chairman/add-visitors.html",{'uid':uid,'wid':wid,'mall':mall})
    else:
        return HttpResponseRedirect(reverse('login'))

def view_visitors(request):
    uid = User.objects.get(email=request.session['email'])
    cid = Chairman.objects.get(user_id=uid)
    vall = Visitors.objects.all()
    return render(request,"chairman/viewvisitors.html",{'uid':uid,'cid':cid,'vall':vall})

def view_visitors2(request):
    uid = User.objects.get(email=request.session['email'])
    wid = Watchman.objects.get(user_id=uid)
    all = Visitors.objects.all()
    return render(request,"chairman/viewvisitors2.html",{'uid':uid,'wid':wid,'all':all})



def maintenance(request):
    uid = User.objects.get(email=request.session['email'])
    mid = Member.objects.get(user_id=uid)
    return render(request,"chairman/pay.html",{'uid':uid,'mid':mid})

def initiate_payment(request):
    if request.method == "GET":
        return render(request, 'chairman/pay.html')
    try:
        id = request.POST['id']
        
        amount = int(request.POST['amount'])
        mid=Member.objects.get(id=id)
    except:
        return render(request, 'chairman/pay.html', context={'error': 'Wrong Accound Details or amount'})

    transaction = Transaction.objects.create(made_by=mid, amount=amount)
    transaction.save()
    merchant_key = settings.PAYTM_SECRET_KEY

    params = (
        ('MID', settings.PAYTM_MERCHANT_ID),
        ('ORDER_ID', str(transaction.order_id)),
        ('CUST_ID', str(transaction.made_by.firstname)),
        ('TXN_AMOUNT', str(transaction.amount)),
        ('CHANNEL_ID', settings.PAYTM_CHANNEL_ID),
        ('WEBSITE', settings.PAYTM_WEBSITE),
        # ('EMAIL', request.user.email),
        # ('MOBILE_N0', '9911223388'),
        ('INDUSTRY_TYPE_ID', settings.PAYTM_INDUSTRY_TYPE_ID),
        ('CALLBACK_URL', 'http://127.0.0.1:8000/callback/'),
        # ('PAYMENT_MODE_ONLY', 'NO'),
    )

    paytm_params = dict(params)
    checksum = generate_checksum(paytm_params, merchant_key)

    transaction.checksum = checksum
    transaction.save()

    paytm_params['CHECKSUMHASH'] = checksum
    print('SENT: ', checksum)
    return render(request, 'chairman/redirect.html', context=paytm_params)

@csrf_exempt
def callback(request):
    if request.method == 'POST':
        received_data = dict(request.POST)
        paytm_params = {}
        paytm_checksum = received_data['CHECKSUMHASH'][0]
        for key, value in received_data.items():
            if key == 'CHECKSUMHASH':
                paytm_checksum = value[0]
            else:
                paytm_params[key] = str(value[0])
        # Verify checksum
        is_valid_checksum = verify_checksum(paytm_params, settings.PAYTM_SECRET_KEY, str(paytm_checksum))
        if is_valid_checksum:
            received_data['message'] = "Checksum Matched"
        else:
            received_data['message'] = "Checksum Mismatched"
            return render(request, 'chairman/callback.html', context=received_data)
        return render(request, 'chairman/callback.html', context=received_data)

def maintenance_details(request):
    uid = User.objects.get(email=request.session['email'])
    cid = Chairman.objects.get(user_id=uid)
    tall = Transaction.objects.all()
    return render(request,"chairman/maintenance-details.html",{'uid':uid,'cid':cid,'tall':tall})

# def landing_page(request):
#     return render(request,'chairman/home.html')    

def web_visitor(request):
    if request.POST:
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']

        wvid=Webvisitor.objects.create(name=name,email=email,subject=subject,message=message)
        return render(request,"chairman/home.html")
    return render(request,"chairman/home.html")

def contact_list(request):
    uid = User.objects.get(email=request.session['email'])
    cid=Chairman.objects.get(user_id = uid)
    
    return render(request,"chairman/contact-list.html",{'uid':uid,'cid':cid})

def contact1_list(request):
    uid = User.objects.get(email=request.session['email'])
    mid=Member.objects.get(user_id = uid)
    
    return render(request,"chairman/contact1-list.html",{'uid':uid,'mid':mid})

def contact2_list(request):
    uid = User.objects.get(email=request.session['email'])
    wid=Watchman.objects.get(user_id = uid)
    
    return render(request,"chairman/contact2-list.html",{'uid':uid,'wid':wid})

def view_chairman1(request):
    uid = User.objects.get(email=request.session['email'])
    mid = Member.objects.get(user_id=uid)

    call= Chairman.objects.all()  
    return render(request,'chairman/view-chairman1.html',{'uid':uid,'mid':mid,'call':call})  

def view_chairman2(request):
    uid = User.objects.get(email=request.session['email'])
    wid = Watchman.objects.get(user_id=uid)

    call= Chairman.objects.all()  
    return render(request,'chairman/view-chairman2.html',{'uid':uid,'wid':wid,'call':call})

def mycomplaint1(request):
    uid = User.objects.get(email=request.session['email'])
    mid = Member.objects.get(user_id=uid)
    myc = Complaintmember.objects.filter(member_id = mid)
    return render(request,'chairman/mycomplaint1.html',{'uid':uid,'mid':mid,'myc':myc})

def delete_mycomplaint1(request,pk):
    uid = User.objects.get(email=request.session['email']) #logged in user
    mid = Member.objects.get(user_id=uid)
    call = Complaintmember.objects.filter(member_id = mid)
    complaintid = Complaintmember.objects.get(id = pk)
    complaintid.delete()
    return render(request,'chairman/mycomplaint1.html',{'uid':uid,'complaintid':complaintid,'mid':mid,'call':call})

def mycomplaint2(request):
    uid = User.objects.get(email=request.session['email'])
    wid = Watchman.objects.get(user_id=uid)
    myc = Complaintwatchman.objects.filter(watchman_id = wid)
    return render(request,'chairman/mycomplaint2.html',{'uid':uid,'wid':wid,'myc':myc})

def delete_mycomplaint2(request,pk):
    uid = User.objects.get(email=request.session['email']) #logged in user
    wid = Watchman.objects.get(user_id=uid)
    call = Complaintwatchman.objects.filter(watchman_id = wid)
    complaintid = Complaintwatchman.objects.get(id = pk)
    complaintid.delete()
    return render(request,'chairman/mycomplaint2.html',{'uid':uid,'complaintid':complaintid,'wid':wid,'call':call})


