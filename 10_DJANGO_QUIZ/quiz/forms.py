from django import forms
from django.core.exceptions import ValidationError

from quiz.models import Choice


class QuestionInlineFormSet(forms.BaseInlineFormSet):
    def clean(self):
        if not (self.instance.QUESTION_MIN_LIMIT <= len(self.forms) <= self.instance.QUESTION_MAX_LIMIT):
            raise ValidationError(
                f'Кол-во вопросов должно быть в диапазоне '
                f'от {self.instance.QUESTION_MIN_LIMIT} '
                f'до {self.instance.QUESTION_MAX_LIMIT}'
            )


class ChoiceInlineFormSet(forms.BaseInlineFormSet):
    def clean(self):
        num_correct_answers = sum(form.cleaned_data['is_correct'] for form in self.forms)

        if num_correct_answers == 0:
            raise ValidationError('Необходимо выбрать как минимум 1 вариант.')

        if num_correct_answers == len(self.forms):
            raise ValidationError('НЕ разрешено выбирать все варианты')


class ChoiceForm(forms.ModelForm):
    is_selected = forms.BooleanField(required=False)

    class Meta:
        model = Choice
        fields = ['text']


ChoicesFormSet = forms.modelformset_factory(
    model=Choice,
    form=ChoiceForm,
    extra=0
)
