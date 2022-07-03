import datetime

from dateutil.relativedelta import relativedelta

from django.core.validators import MinLengthValidator
from django.db import models

from faker import Faker

from .validators import adult_validator


class BaseModel(models.Model):
    class Meta:
        abstract = True

    first_name = models.CharField(
        max_length=100,
        verbose_name='first name',
        validators=[MinLengthValidator(2)],
        db_column='first_name'
    )
    last_name = models.CharField(
        max_length=100,
        verbose_name='last name',
        validators=[MinLengthValidator(2)],
        db_column='last_name'
    )
    birthday = models.DateField(
        default=datetime.date.today,
        validators=[adult_validator]
        # validators=[AdultValidator(20)]
    )
    phone_number = models.CharField(
        max_length=25,
        null=True,
    )

    def get_age(self):
        return relativedelta(datetime.date.today(), self.birthday).years

    @classmethod
    def _generate(cls):
        fk = Faker()
        obj = cls(
            first_name=fk.first_name(),
            last_name=fk.last_name(),
            birthday=fk.date_between(start_date='-65y', end_date='-15y'),
            phone_number=fk.phone_number()
        )

        obj.save()

        return obj

    @classmethod
    def generate(cls, cnt):
        for _ in range(cnt):
            cls._generate()
