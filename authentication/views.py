from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth.views import PasswordResetView 
from django.contrib.auth.models import User
from django.urls import reverse_lazy
import logging
logger = logging.getLogger(__name__)

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('login')
        else:
            # Display errors if form is invalid
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            print('Form is valid')
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                print('User authenticated')
                login(request, user)
                return redirect('home')  # Redirect to the home page
            else:
                print('User not authenticated')
                messages.error(request, 'Invalid email or password.')
        else:
            print('Form is invalid')
            messages.error(request, 'Please correct the following errors.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})






class CustomPasswordResetView(PasswordResetView):
    template_name = 'password_reset_form.html'
    success_url = reverse_lazy('password_reset_done')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        try:
            user = User.objects.get(email=email)
            send_mail(
                'Password Reset Request',
                'You have requested a password reset. Please click the following link to reset your password: {}'.format(self.request.build_absolute_uri(reverse_lazy('password_reset_confirm', kwargs={'uidb64': user.id, 'token': 'token'}))),
                settings.EMAIL_HOST_USER,  # Use your own email address as the sender
                [email],  # Use the recipient's email address
                fail_silently=False,
            )
            messages.success(self.request, 'Password reset email has been sent.')
        except User.DoesNotExist:
            messages.error(self.request, 'Invalid email address.')
        except Exception as e:
            logger.error(f"Error sending password reset email: {e}")
            messages.error(self.request, 'An error occurred while sending the password reset email. Please try again later.')
        return super().form_valid(form)