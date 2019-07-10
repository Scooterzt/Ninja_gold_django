from django.shortcuts import render, HttpResponse, redirect
import random

def index(request):
    if "your_gold" not in request.session:
        request.session["your_gold"] = 0 
    return render(request,"ninja_app/index.html")

def process_money(request):
    location = request.POST["location"]
    if location == "farm":
        request.session["your_gold"]+= random.randint(10,20) 
    elif location == "cave":
        request.session["your_gold"] += random.randint(5,10)
    elif location == "house":
        request.session["your_gold"] += random.randint(2,5)
    else:
        request.session["your_gold"] += random.randint(-50,50)
    request.session["location"] = location
    return redirect("/")
def reset(request):
    request.session.pop("your_gold")
    return redirect("/")