from django.db import models


class Profile(models.Model):

    login = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='static/img/', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):

    name = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Question(models.Model):

    title = models.CharField(max_length=255)
    body = models.CharField(max_length=255)
    tags = models.ManyToManyField(Tag)
    votes_count = models.IntegerField(default=0)

    autor = models.ForeignKey(Profile, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Answer(models.Model):

    body = models.CharField(max_length=255)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)
    votes_count = models.IntegerField(default=0)

    autor = models.ForeignKey(Profile, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class QuestionVotes(models.Model):

    VOTE_TYPE = [(1, 'liked'), (-1, 'disliked')]
    content_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    autor = models.ForeignKey(Profile, on_delete=models.CASCADE)
    vote = models.IntegerField(choices=VOTE_TYPE, default=0)


class AnswerVotes(models.Model):

    VOTE_TYPE = [(1, 'liked'), (-1, 'disliked')]
    content_id = models.ForeignKey(Answer, on_delete=models.CASCADE)
    autor = models.ForeignKey(Profile, on_delete=models.CASCADE)
    vote = models.IntegerField(choices=VOTE_TYPE, default=0)
