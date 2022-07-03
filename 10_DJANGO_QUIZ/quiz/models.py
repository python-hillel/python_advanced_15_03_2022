from uuid import uuid4

from django.contrib.auth import get_user_model
from django.db import models


class BaseModel(models.Model):
    create_timestamp = models.DateTimeField(auto_now_add=True)
    update_timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Exam(BaseModel):
    QUESTION_MIN_LIMIT = 3
    QUESTION_MAX_LIMIT = 100

    class LEVEL(models.IntegerChoices):
        BASIC = 0, 'Basic'
        MIDDLE = 1, 'Middle'
        ADVANCED = 2, 'Advanced'

    uuid = models.UUIDField(default=uuid4, db_index=True, unique=True)
    title = models.CharField(max_length=64)
    description = models.TextField(null=True, blank=True)
    level = models.PositiveSmallIntegerField(choices=LEVEL.choices, default=LEVEL.BASIC)

    def __str__(self):
        return self.title

    def questions_count(self):
        return self.questions.count()

    class Meta:
        verbose_name = 'Exam'
        verbose_name_plural = 'Exams'


class Question(BaseModel):
    exam = models.ForeignKey(Exam, related_name='questions', on_delete=models.CASCADE)
    order_num = models.PositiveSmallIntegerField()
    text = models.CharField(max_length=2048)
    image = models.ImageField(null=True, blank=True, upload_to='questions/')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'


class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    text = models.CharField(max_length=1024)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Choice'
        verbose_name_plural = 'Choices'


class Result(BaseModel):
    class STATE(models.IntegerChoices):
        NEW = 0, "New"
        FINISHED = 1, "Finished"

    user = models.ForeignKey(get_user_model(), related_name='results', on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, related_name='results', on_delete=models.CASCADE)
    state = models.PositiveSmallIntegerField(default=STATE.NEW, choices=STATE.choices)
    uuid = models.UUIDField(default=uuid4, db_index=True, unique=True)
    current_order_number = models.PositiveSmallIntegerField(default=0)
    num_correct_answers = models.PositiveSmallIntegerField(default=0)
    num_incorrect_answers = models.PositiveSmallIntegerField(default=0)

    class Meta:
        verbose_name = 'Result'
        verbose_name_plural = 'Results'

    def update_result(self, order_number, question, selected_choices):
        correct_choice = [choice.is_correct for choice in question.choices.all()]
        correct_answer = True
        for k in zip(selected_choices, correct_choice):
            correct_answer &= (k[0] == k[1])

        self.num_correct_answers += int(correct_answer)
        self.num_incorrect_answers += 1 - int(correct_answer)
        self.current_order_number = order_number

        if order_number == question.exam.questions.count():
            self.state = self.STATE.FINISHED

        self.save()

    def points(self):
        return max(0, self.num_correct_answers - self.num_incorrect_answers)
