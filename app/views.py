from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from app.models import Question, Answer


def paginate(request, objects_list, per_page):

    page_num = request.GET.get('page', 1)
    paginator = Paginator(objects_list, per_page)

    try:
        obj = paginator.page(page_num)

    except PageNotAnInteger:
        obj = paginator.page(1)

    except EmptyPage:
        obj = paginator.page(paginator.num_pages)

    return obj


def index(request):
    que = Question.objects.get_by_time()

    page_obj = paginate(request, que, 20)
    return render(request, "index.html", {"questions": page_obj})


def settings(request):
    return render(request, "settings.html")


def ask(request):
    return render(request, "ask.html")


def question(request, question_id):
    que = Question.objects.get_question(question_id)
    ans = Answer.objects.get_answer(question_id)
    page_obj = paginate(request, ans, 10)
    return render(request, "question.html", {"question": que[0], "answers": page_obj})


def login(request):
    return render(request, "login.html")


def register(request):
    return render(request, "signup.html")


def tag(request, tag_name):
    que = Question.objects.get_by_tag(tag_name)

    page_obj = paginate(request, que, 10)
    return render(request, "tag.html", {"questions": page_obj, "tag": tag_name})


def hot(request):
    que = Question.objects.hot()

    page_obj = paginate(request, que, 10)
    return render(request, "hot.html", {"questions": page_obj})
