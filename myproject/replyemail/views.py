from django.shortcuts import render
from django.views import View
from django.core.mail import send_mail
from myproject.settings import EMAIL_HOST_USER
from .form import ReplyEmailForm


class ReplyEmail(View):
    def get(self, request):
        return render(self.request, 'replyemail/replyemail.html', {'form' : ReplyEmailForm})

    def post(self, request):
        email = self.request.POST.get('email', '')
        name = self.request.POST.get('name', '')
        subject = self.request.POST.get('subject', '')
        message = self.request.POST.get('message', '')

        fullmessage = 'To '+name+'.'+'\n\n'+message

        
        try:
            send_mail(
                subject=subject,
                message=fullmessage,
                from_email=EMAIL_HOST_USER,
                recipient_list=[email],
                fail_silently=False,
            )
            msg = 'Successful'

        except:
            msg = 'Unsuccessful'

        return render(self.request, 'replyemail/afterreplyemail.html', {'msg' : msg})
        
        

