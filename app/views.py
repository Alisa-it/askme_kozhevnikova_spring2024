from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def settings(request):
    return render(request, "settings.html")


def ask(request):
    return render(request, "ask.html")


def question(request):
    return render(request, "question.html")


def login(request):
    return render(request, "login.html")


def register(request):
    return render(request, "signup.html")


def tag(request):
    return render(request, "tag.html")


def hot(request):
    return render(request, "hot.html")
