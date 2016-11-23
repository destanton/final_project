from django import forms
from django.core.mail import send_mail


class ContactForm(forms.Form):
    sender = forms.CharField(max_length=50)
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        sender = self.cleaned_data["sender"]
        message = self.cleaned_data["message"]
        subject = "Contact Form Submission!"
        body = """Hey Guys! You got a new contact form submission:
        From: {}
        Message: {}
        """.format(sender, message)
        recipient_list = ["tdhdesapp@gmail.com"]
        send_mail(subject, body, 'Do Not Reply <do_not_replay@domain.com>', recipient_list)
