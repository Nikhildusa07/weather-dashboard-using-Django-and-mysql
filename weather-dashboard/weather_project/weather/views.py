import requests

from django.shortcuts import render, redirect

from .models import User, Weather


def register(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        User.objects.create(
            username=username,
            password=password
        )

        return redirect("/login/")

    return render(request, "register.html")


def login(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        try:

            User.objects.get(
                username=username,
                password=password
            )

            return redirect("/home/")

        except User.DoesNotExist:

            return render(
                request,
                "login.html",
                {"error": "Invalid Username or Password"}
            )

    return render(request, "login.html")


def weather_api(request):

    response = requests.get(
        "http://api.weatherapi.com/v1/current.json?key=058b00539ee0452699692353261206&q=Karimnagar&aqi=no"
    )

    weather_data = response.json()

    Weather.objects.create(
        city=weather_data["location"]["name"],
        temperature=weather_data["current"]["temp_c"],
        humidity=weather_data["current"]["humidity"],
        condition=weather_data["current"]["condition"]["text"]
    )

    return render(
        request,
        "home.html",
        weather_data
    )