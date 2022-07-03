import random

from core.models import BaseModel

from django.db import models


class Teacher(BaseModel):
    class Meta:
        db_table = 'teachers'

    salary = models.PositiveIntegerField(default=10000)

    def __str__(self):
        return f'{self.last_name} {self.first_name} - {self.salary}'

    @classmethod
    def _generate(cls):
        obj = super()._generate()
        obj.salary = random.randint(10000, 99999)
        obj.save()
