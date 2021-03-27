from django.shortcuts import render as ren, redirect
from django.http import HttpResponse as res, JsonResponse as jres
from .models import Contact
from django.http import HttpRequest as req
from django.contrib import messages
from django.contrib.auth.models import User, auth


def contact(request):
    done = False
    if request.method == "POST":
        fullname = request.POST.get('fullname', 'unknown')
        phone_number = request.POST.get('phone', 'unknown')
        email = request.POST.get('email', 'unknown')
        comment = request.POST.get('comment', 'unknown')

        if len(phone_number) >= 10:
            contact = Contact(full_name=fullname, email=email,
                              ph_no=phone_number, comments=comment)
            contact.save()
            done = True
        else:
            messages.warning(request, "enter correct phone number")

        if done:
            messages.success(request, f"thank you {fullname} to contact us.")

    return ren(request, "acc/contact.html")


def SignIn(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/blg/')
        else:
            messages.info(request, "invalid user")
            return redirect('/blg')
    return res("404 not found")

    # return ren(request, "acc/sign-in.html")


def SignOut(request):
    auth.logout(request)
    return redirect("/blg/")


def Register(request):
    if request.method == "POST":
        username = request.POST["username"]
        fname = request.POST["firstname"]
        lname = request.POST["lastname"]
        email = request.POST["email"]
        password_1 = request.POST["password"]
        password_2 = request.POST["confirmpassword"]

        if password_1 == password_2:
            user = User.objects.create_user(
                username=username, email=email, password=password_1)
            user.first_name = fname
            user.last_name = lname
            user.save()
            messages.success(request, f"Thank you {fname}.. ")
            return redirect("/blg/")
        else:
            messages.warning(request, "Password don't march! Try again")
            return redirect("/blg/")
    else:
        return res("404, not found")
