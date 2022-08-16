import json
from pydoc import describe
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import os
from django.views.decorators.csrf import csrf_exempt
import googleapiclient.discovery
from django.http import JsonResponse

from .models import Movie, User,MovieView

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = "AIzaSyCy4oWmtMKr1JqY6HZftcKs_HeBnhQs7DA"
youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey = DEVELOPER_KEY)
def index(request):
    
    moives =list(Movie.objects.all().order_by("-timestamp"))
    to_respone = []
    for movie in moives:
        try:
            request_youtube = youtube.videos().list(part="snippet",id=movie.link)
            response = request_youtube.execute()
            title = response["items"][0]["snippet"]["title"]
            description = response["items"][0]["snippet"]["description"]
            # print(title)
            movie = MovieView(title = title,creator_mail = movie.creator.email,description= description,link = movie.link)
            to_respone.append(movie)
        except:
            continue
    return render(request, "movie/index.html",{"movies":to_respone})


@csrf_exempt
def insert(request):
    if request.method=="POST":
        data = json.loads(request.body)
        linkId = data["link"]
        user = User.objects.get(pk = request.user.id)
        movie = Movie(creator=user,link=linkId)
        movie.save()
        #should use try catch
        try:
            request_youtube = youtube.videos().list(part="snippet",id=linkId)
            response = request_youtube.execute()
            title = response["items"][0]["snippet"]["title"]
            description = response["items"][0]["snippet"]["description"]
        except:
            JsonResponse({"message":"Not found"},status = 401)
    return JsonResponse({"message":"Uploaded succesfully","title":title,"description":description,"creator":user.email,"link":linkId},status = 200)

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "movie/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "movie/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "movie/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "movie/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "movie/register.html")
