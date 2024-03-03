import pyotp
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail


def send_otp(request):
    totp = pyotp.TOTP(pyotp.random_base32(), interval=60)
    otp = totp.now()

    request.session['otp_secret_key'] = totp.secret
    valid_date = datetime.now() + timedelta(minutes=3)
    request.session['otp_valid_date'] = str(valid_date)

#    print(f"Your one-time-password is:{otp}")
#    request.session['username'] = username
    user = request.POST.get('username')
    password = request.POST.get('password')
    USER = authenticate(request, username=user, password=password)
    email = USER.email
    subject = 'OTP request'
    message = f"Your one-time-password is:{otp}"
    email = email
    from_email = settings.EMAIL_HOST_USER
    send_mail(subject, message, from_email, [email])    

