from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.utils import timezone
from .models import Student
from .forms import StudentForm, ContactForm

def home(request):
    students = Student.objects.all().order_by("-id")
    count = request.session.get("visit_count", 0) + 1
    request.session["visit_count"] = count
    response = render(request, "portal/home.html", {"students": students, "visit_count": count})
    response.set_cookie("last_visit", timezone.localtime().strftime("%Y-%m-%d %H:%M:%S"), max_age=604800, httponly=True, samesite="Lax")
    return response

def register(request):
    form = StudentForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("home")
    return render(request, "portal/register.html", {"form": form})

def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        item = form.save()
        send_mail(item.subject, item.message, None, ["admin@example.com"], fail_silently=False)
        return redirect("home")
    return render(request, "portal/contact.html", {"form": form})
