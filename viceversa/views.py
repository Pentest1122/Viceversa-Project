from itertools import count
from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def reverse(request):
    getting_text = request.GET["usertext"]
    count_words= getting_text.split()
    num_of_words = len(count_words)
    reversed_text = getting_text[::-1]
    return render(request, "reverse.html", {"usertext": getting_text, "reversedtext": reversed_text, "num_of_words": num_of_words})