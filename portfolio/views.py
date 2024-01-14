from django.shortcuts import render
from django.core.mail import EmailMessage
from django.utils.encoding import smart_bytes
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

        # Modifica la contraseña antes de usarla en la autenticación SMTP
        email_host_password = 'pyfd yleb wubu wnfr'  # Reemplaza con tu contraseña real
        encoded_password = base64.b64encode(email_host_password.encode('utf-8')).decode('utf-8')

        email_message = EmailMessage(
            subject=smart_bytes(name + " : " + subject),
            body=smart_bytes(message),
            to=["sawarinsteven@gmail.com"],
            headers={"Reply-To": smart_bytes(email)}
        )

        # Configura el servidor SMTP con la contraseña codificada
        email_message.connection = (email_message.connection or {}).copy()
        email_message.connection['password'] = encoded_password

        # Asegúrate de manejar excepciones adecuadamente al enviar el correo electrónico.
        try:
            email_message.send()
        except Exception as e:
            # Manejo de errores (puedes personalizar según tus necesidades)
            print(f"Error al enviar el correo electrónico: {e}")

    return render(request, "index.html", context)
