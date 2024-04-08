from django.core.paginator import Paginator
from django.shortcuts import render

QUESTIONS = [
    {
        "title": f"Question {i}",
        "text": f"This is question number {i}",
        "id": i,
    }
    for i in range(95)
]
ANSWERS = [
    {
        "text": f"This is very interesting answer number {i}",
    }
    for i in range(5)
]

TAGS = [
    {
        "name": tag,
    }
    for tag in ['blabla', 'tag', 'meme']
]


def paginate(request, objects_list, per_page):
    page_num = request.GET.get('page', 1)
    paginator = Paginator(objects_list, per_page)
    obj = paginator.page(page_num)
    return obj


def index(request):
    page_obj = paginate(request, QUESTIONS, 20)
    return render(request, "index.html", {"questions": page_obj, "tags": TAGS})


def settings(request):
    return render(request, "settings.html")


def ask(request):
    return render(request, "ask.html")


def question(request, question_id):
    item = QUESTIONS[question_id]
    return render(request, "question.html", {"questions": item, "answers": ANSWERS, "tags": TAGS})


def login(request):
    return render(request, "login.html")


def register(request):
    return render(request, "signup.html")


def tag(request, tag_name):
    page_obj = paginate(request, QUESTIONS[10:], 10)
    return render(request, "tag.html", {"questions": page_obj, "tag": tag_name, "tags": TAGS})


def hot(request):
    page_obj = paginate(request, QUESTIONS[18:], 10)
    return render(request, "hot.html", {"questions": page_obj, "tags": TAGS})
