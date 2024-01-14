from django.shortcuts import render
from django.core.mail import EmailMessage
from django.utils.encoding import smart_text
from .models import Images
import base64

def home(request):
    context = {}
    images = Images.objects.all()
    context["images"] = images

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        email_host_password = 'pyfd yleb wubu wnfr'
        encoded_password = base64.b64encode(email_host_password.encode('utf-8')).decode('utf-8')

        email_message = EmailMessage(
            subject=smart_text(name + " : " + subject),
            body=smart_text(message),
            to=["sawarinsteven@gmail.com"],
            headers={"Reply-To": smart_text(email)}
        )

        email_message.connection = (email_message.connection or {}).copy()
        email_message.connection['password'] = encoded_password

        try:
            email_message.send()
        except Exception as e:
            print(f"Error al enviar el correo electrónico: {e}")

    return render(request, "index.html", context)
