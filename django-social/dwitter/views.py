from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Profile
from dwitter.forms import CustomUserCreationForm
from .forms import ItemForm, FileForm
from django.core.files.storage import  FileSystemStorage


def dashboard(request):
    form = ItemForm()
    return render(request, "dwitter/dashboard.html", {"form": form})


def create_item(request):
    form = ItemForm(request.POST)
    file = FileForm(request.POST)
    if request.method == "POST":
        if file.is_valid():
            instance = ModelWithFileField(file_field=request.FILES['file'])
            instance.save()
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return redirect("my_items", pk=request.user.profile.pk)
    return render(request, "dwitter/create_item.html", {"form": form, "file": file})


def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "dwitter/profile_list.html", {"profiles": profiles})


def profile(request, pk):

    profile = Profile.objects.get(pk=pk)

    if request.method == "POST":

        current_user_profile = request.user.profile

        data = request.POST

        action = data.get("trust")

        if action == "trust":

            current_user_profile.trust.add(profile)

        elif action == "untrust":

            current_user_profile.trust.remove(profile)

        current_user_profile.save()

    return render(request, "dwitter/profile.html", {"profile": profile})


def my_items(request, pk):
    items = request.user.items
    return render(request, "dwitter/my_items.html", {"items": items})


def register(request):

    if request.method == "GET":

        return render(

            request, "dwitter/register.html",

            {"form": CustomUserCreationForm}

        )

    elif request.method == "POST":

        form = CustomUserCreationForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect(reverse("dashboard"))
