from django.contrib.auth import login #, authenticate
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string

from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView
# from django.views.generic.edit import BaseFormView, UpdateView, DeleteView

from django.contrib.auth.models import User
from core.tokens import account_activation_token
from core.forms import SignUpForm, ProfileForm
from core.models import Profile
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from resolutions import settings


def get_activation_link(request, user=None):
    '''
    Function creates the activation link and
    sends it to the user using Django smtp
    mailing services.
    '''
    current_site = get_current_site(request)
    subject = 'Activate Your MySite Account'
    message = render_to_string('user/account_activation_email.html', {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
    })
    user.email_user(subject, message)

def get_activation_link_sendgrid(request, user=None):
    '''
    Functions creates the activation link and
    sends it to the user using SENDGRID package.
    '''
    if user is None:
        return False
    # import pdb; pdb.set_trace()
    current_site = get_current_site(request)
    message = render_to_string('user/account_activation_email.html', {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
    })
    mail = EmailMultiAlternatives(
        subject="Activate Your MySite Account",
        body=message,
        from_email=settings.ADMIN_EMAIL_ADDRESS,
        to=[user.email],
        headers={"Reply-To": "support@sendgrid.com"}
    )
    # Add template
    mail.template_id = 'user/account_activation_email.html'

    # Replace substitutions in sendgrid template
    mail.substitutions = {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
    }
    # import pdb; pdb.set_trace()
    mail.send()

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        profileform = ProfileForm(request.POST, request.FILES)
        if form.is_valid() and profileform.is_valid():
            # import pdb ; pdb.set_trace()
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            # Refreshing will sync up the user profile with user instance
            user.refresh_from_db()
            # if form.cleaned_data.get('attribute') == 'user':
            #     user.profile = Profile(attribute=Profile.USER)
            # else:
            #     user.profile = Profile(attribute=Profile.DRIVER)
            # Adding the user profile
            user.profile.attribute = profileform.cleaned_data.get('attribute')
            user.profile.image = profileform.cleaned_data.get('image')
            user.profile.bio = profileform.cleaned_data.get('bio')
            user.profile.location = profileform.cleaned_data.get('location')
            user.profile.birth_date = profileform.cleaned_data.get('birth_date')
            user.profile.gender = profileform.cleaned_data.get('gender')
            user.save()
            # Generates the email varification link
            try:
                get_activation_link(request, user=user)
                print("Worked the Django Way!!")
            except:
                print("Trying to send mail via sendgrid module")
                get_activation_link_sendgrid(request, user=user)
                print("Worked!!")
            return redirect('account_activation_sent')
            # Simple Registrations
            # form.save()
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password)
            # login(request, user)
            # return redirect('/truck/list/')
    else:
        form = SignUpForm()
        profileform = ProfileForm()
    return render(request, 'user/register.html', {'forms': [form, profileform]})


def account_activation_sent(request):
    '''
    Email activation link sent
    '''
    return render(request, 'user/account_activation_sent.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        # Activating the user after email conformations
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('/truck/list/')
    else:
        return render(request, 'account_activation_invalid.html')

# def details(request, pk):
#     if request.method == 'GET':

class UserDetailView(DetailView):
    model = User
    template_name='user/details.html'
    context_object_name = 'userObj'

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        # import pdb ; pdb.set_trace()
        return context

def update(request, pk, template_name='user/updates.html'):
    # import pdb ; pdb.set_trace()
    if int(request.user.pk) is not int(pk):
        from django.http import HttpResponseNotFound
        return HttpResponseNotFound('<h1>Page not found</h1>')
    if request.method == 'POST':
        userform = SignUpForm(request.POST or None, request.FILES, instance=request.user)
        profileform = ProfileForm(request.POST or None, request.FILES, instance=request.user.profile)
        if userform.is_valid() and profileform.is_valid():
            # import pdb ; pdb.set_trace()
            userform.save()
            profileform.save()
            # profileform.save()
            '''user = form.save(commit=False)
            user.save()
            # Refreshing will sync up the user profile with user instance
            user.refresh_from_db()
            # if form.cleaned_data.get('attribute') == 'user':
            #     user.profile = Profile(attribute=Profile.USER)
            # else:
            #     user.profile = Profile(attribute=Profile.DRIVER)
            # Adding the user profile
            user.profile.attribute = form.cleaned_data.get('attribute')
            user.profile.image = form.cleaned_data.get('image')
            user.profile.bio = form.cleaned_data.get('bio')
            user.profile.location = form.cleaned_data.get('location')
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.profile.gender = form.cleaned_data.get('gender')
            user.save()'''
            # Generates the email varification link
            # get_activation_link(request, user=user)
            return redirect('/account/%s/' % (pk,))
            # Simple Registrations
            # form.save()
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password)
            # login(request, user)
            # return redirect('/truck/list/')
    else:
        user = get_object_or_404(User, pk=pk)
        # import pdb ; pdb.set_trace()
        form = SignUpForm(request.POST or None, instance=user)
        profile = get_object_or_404(Profile, user=user)
        profileform = ProfileForm(request.POST or None, instance=profile)
    return render(request, 'user/updates.html', {'userform': [form, profileform]})
