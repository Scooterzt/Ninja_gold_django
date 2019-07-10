from django.shortcuts import render, HttpResponse, redirect
import random

def index(request):
    if "your_gold" not in request.session:
        request.session["your_gold"] = 0
    if "messages" not in request.session:
        request.session["messages"] = []
    return render(request,"ninja_app/index.html")

def process_money(request):
    location = request.POST["location"]
    if location == "farm":
        your_gold = random.randint(10,20) 
    elif location == "cave":
        your_gold = random.randint(5,10)
    elif location == "house":
        your_gold = random.randint(2,5)
    else:
        your_gold = random.randint(-50,50)

    if your_gold > 0:
        request.session["messages"].insert(0, f"<p>Earned {str(your_gold)} gold from the {location}</p>")
    else:
        request.session["messages"].insert(0, f"<p>Entered a {location} and lost {str(your_gold)} gold...</p>")
    request.session["your_gold"] += your_gold
    return redirect("/")
def reset(request):
    request.session.pop("your_gold")
    request.session.pop("messages")
    return redirect("/")