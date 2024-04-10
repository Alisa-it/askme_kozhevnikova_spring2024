from django.core.management import BaseCommand, CommandError
from random import randint, choice
from django.utils.crypto import get_random_string
from app.models import *


class Command(BaseCommand):
    def add_arguments(self, parse):
        parse.add_argument('ratio', type=int, help='[ratio]')

    def handle(self, *args, **options):
        ratio = options['ratio']

        users = [User.objects.create_user(username=f'user_{get_random_string(7)}{i}', email=f'u{i}@user.com', password='a1b2c3d4e5f6', first_name=f'Userr{i}') for i in range(ratio)]

        profiles = [Profile(user=u) for u in users]
        Profile.objects.bulk_create(profiles)

        tags = [Tag(name=f'tag_{get_random_string(4)}{i}') for i in range(ratio)]
        Tag.objects.bulk_create(tags)

        questions = [Question(title=f'Question {i}', body=f'Text of question', votes_count=randint(0, ratio*200), autor=choice(profiles)) for i in range(ratio*10)]
        Question.objects.bulk_create(questions)

        answers = [Answer(body=f'Answer{i}', question=choice(questions), votes_count=randint(0, ratio*20), autor=choice(profiles)) for i in range(ratio*100)]
        Answer.objects.bulk_create(answers)
