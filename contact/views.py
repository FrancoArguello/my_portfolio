from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage


# Create your views here.
def contact(request):
    contact_form = ContactForm()
    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)

        if contact_form.is_valid():
            fullname = request.POST.get('fullname', '')
            email = request.POST.get('email', '')
            phone = request.POST.get('phone', '')
            message = request.POST.get('message', '')

        # send email
        email = EmailMessage(
            'mensaje de contacto recibido',
            'Mensaje enviado por {}\nDatos de contacto\nEmail: {}\nTeléfono: {}\nMensaje:\n{}'.format(
                fullname, email, phone, message),
            email,
            ['cba9028243d9ae@inbox.mailtrap.io'],
            reply_to=[email],
        )
        try:
            email.send()
            # esto nos modifica nuestra url y nos pone un ok al final
            return redirect(reverse('contact') + '?ok')
        except:
            # si no se pudo enviar el mail
            return redirect(reverse('contact') + '?error')

    return render(request, 'contact/contact.html', {'form': contact_form})
