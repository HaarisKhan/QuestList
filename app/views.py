from django.core.urlresolvers import reverse
from django.shortcuts import render, HttpResponse, HttpResponseRedirect, render_to_response
from django.template.context_processors import csrf
from django.contrib.auth import authenticate, login, logout
from . import models, forms

# Create your views here.


def index(request):
    return render(request, 'main/index.html')


def login_view(request):
    if request.POST:
        login_form = forms.PersonForm(request.POST)
        if login_form.is_valid():
            login_form.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'main/login.html', {'form': login_form})
    else:
        login_form = forms.PersonForm()
        args = {}
        args.update(csrf(request))
        args['form'] = login_form

        return render_to_response('main/login.html', args)


def signup(request):
    if request.POST:
        signup_form = forms.CreatePersonForm(request.POST)
        if signup_form.is_valid():
            email = signup_form['username'].value()

            models.Person.objects.create(username=email)

            signup_form.save()

            authenticate_user = authenticate(username = signup_form.cleaned_data['username'], password = signup_form.cleaned_data['password1'])
            login(request, authenticate_user)

            return HttpResponseRedirect(reverse('home'))
        else:
            return render(request, 'main/signup.html', {'form': signup_form})
    else:
        return render(request, 'main/signup.html', {'form': forms.CreatePersonForm()})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))