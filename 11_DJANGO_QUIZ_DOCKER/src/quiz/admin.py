from django.contrib import admin

from .forms import ChoiceInlineFormSet
from .forms import QuestionInlineFormSet
from .models import Choice
from .models import Exam
from .models import Question
from .models import Result


class ChoiceInline(admin.TabularInline):
    model = Choice
    fields = ['text', 'is_correct']
    # show_change_link = True
    formset = ChoiceInlineFormSet
    extra = 0


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]


class QuestionInline(admin.TabularInline):
    model = Question
    fields = ['text', 'order_num']
    # show_change_link = True
    extra = 0
    formset = QuestionInlineFormSet
    ordering = ('order_num', )


class ExamAdmin(admin.ModelAdmin):
    # readonly_fields = ['uuid']
    exclude = ['uuid']
    inlines = [QuestionInline]


admin.site.register(Exam, ExamAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Result)
