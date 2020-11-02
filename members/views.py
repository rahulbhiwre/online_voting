from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.views.generic import TemplateView, CreateView
from .forms import SignUpForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from members.models import Profile
from django.http import HttpResponse
from .models import Poll
import pickle
from phe import paillier
from django.contrib.auth.decorators import login_required
import random


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')


class home(LoginRequiredMixin,TemplateView):
    template_name = 'users/home.html'
    login_url = reverse_lazy('firstpage')
    

def vote(request,user_id):
    if request.user.is_authenticated:

        poll = Poll()      # there is only one object inside poll model 
        user = User.objects.get(pk=user_id)
        check = not(user.profile.voted)

        pickle_in=open("pub.pickle","rb")

        public_key=pickle.load(pickle_in)

        if request.method == 'POST' and check:
            selected_option = request.POST['poll']
            if selected_option == 'option1':
                k=1
            elif selected_option == 'option2':
                k=2
            elif selected_option == 'option3':
                k=3
            else:
                return HttpResponse(400, 'Invalid form')

            j=10**(7*(k-1))
            l=public_key.encrypt(j)

            poll.sum_total=poll.sum_total+l
            poll.on_going(poll.sum_total)
            poll.save()
            
            user.profile.voted = True     # vote is done
            user.save()

            return render(request, 'users/thanks.html')

        else:
            if not(check):
                # if user is allready votted then redirect to thanks page
                return render(request, 'users/voted.html')
            else:
                # if user is not votted then show him poll page
                return render(request, 'users/vote.html')

    else:
        return redirect('login')


def voted(request):
    return render(request,'users/voted.html')


def index(request):
    return render(request,'users/index.html')


global no
no=0

def validateotp(request):
    global no
    if request.method == 'POST' :
        otp=request.POST.get('otp','')
        if (int(otp) == int(no)):
            return redirect('home')
        else:
            messages.info(request, "Invalid OTP Enter Correct OTP")
            return render(request,'users/validateotp.html')

    else:
        no=random.randrange(1000,9999)
        subject = 'Thank You for Being a responsible citizen. !'
        message = "Your OTP for voting confirmation is : {} ".format(no)
        from_email = settings.EMAIL_HOST_USER
        u=request.user
        #print(u.email)
        to_list = [u.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)
        return render(request,'users/validateotp.html')


def result(request):

    poll=Poll()
    no = poll.total()    # taking the result from server
    s_no = str(no)       

    bjp = s_no[-7::1]          # spliting of sum string
    cong = s_no[-14:-7:1]
    other = s_no[-15::-1]

    context = {
        "bjp":bjp,"cong":cong,"other":other,
    }
    return render(request,'users/result.html',context)