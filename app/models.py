from django.contrib.auth.models import User
from django.db import models
from django.db.models import Count


class QuestionManager(models.Manager):
    def get_by_time(self):
        return self.filter().order_by('-created_at').annotate(num_answers=Count('answer')).all()

    def get_by_tag(self, category):

        return self.filter(tags__name=category)

    def hot(self):

        return self.filter().order_by('-votes_count').annotate(num_answers=Count('answer'))

    def get_question(self, question_id):

        return self.filter(id=question_id)


class AnswerManager(models.Manager):
    def get_answer(self, que_id):
        return self.filter(question_id=que_id)


class Profile(models.Model):

    user = models.OneToOneField(User, unique=True, on_delete=models.PROTECT)
    avatar = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.user.username


class Tag(models.Model):

    name = models.CharField(max_length=255, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Question(models.Model):

    title = models.CharField(max_length=255)
    body = models.CharField(max_length=255)
    tags = models.ManyToManyField(Tag)
    votes_count = models.IntegerField(default=0)

    autor = models.ForeignKey(Profile, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = QuestionManager()

    def __str__(self):
        return f'"{self.title}" by {self.autor.user.username}'


class Answer(models.Model):

    body = models.CharField(max_length=255)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)
    votes_count = models.IntegerField(default=0)

    autor = models.ForeignKey(Profile, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = AnswerManager()
    def __str__(self):
        return f'{self.autor.user.username} to "{self.question.title}": "{self.body}"'


class QuestionVote(models.Model):

    VOTE_TYPE = [(1, 'liked'), (-1, 'disliked')]
    content = models.ForeignKey(Question, on_delete=models.CASCADE)
    autor = models.ForeignKey(Profile, on_delete=models.CASCADE)
    vote = models.IntegerField(choices=VOTE_TYPE, default=0)

    def __str__(self):
        return f'{self.content} vote: {self.vote}'


class AnswerVote(models.Model):

    VOTE_TYPE = [(1, 'liked'), (-1, 'disliked')]
    content = models.ForeignKey(Answer, on_delete=models.CASCADE)
    autor = models.ForeignKey(Profile, on_delete=models.CASCADE)
    vote = models.IntegerField(choices=VOTE_TYPE, default=0)

    def __str__(self):
        return f'{self.content} vote: {self.vote}'
