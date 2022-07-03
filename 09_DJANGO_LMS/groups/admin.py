from django.contrib import admin

from groups.models import Group
from students.models import Student


class TeachersInlineTable(admin.TabularInline):
    model = Group.teachers.through
    extra = 0
    can_delete = False

    fields = [
        'first_name',
        'last_name',
        'salary',
    ]

    readonly_fields = fields

    def has_add_permission(self, request, obj):
        return False

    def first_name(self, obj):
        return obj.teacher.first_name

    def last_name(self, obj):
        return obj.teacher.last_name

    def salary(self, obj):
        return obj.teacher.salary


class StudentsInlineTable(admin.TabularInline):
    model = Student
    fields = [
        'first_name',
        'last_name',
        'birthday',
        'phone_number',
    ]

    extra = 0
    readonly_fields = fields
    can_delete = False
    # [
    #     'first_name',
    #     'last_name',
    # ]
    # show_change_link = True
    #

    def has_add_permission(self, request, obj):
        return False

    # def has_delete_permission(self, request, obj=None):
    #     return False


class GroupAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'start_date',
        'end_date',
        'headman'
    ]

    fields = [
        'name',
        ('start_date', 'end_date'),
        'headman',
        'teachers',
        ('create_datetime', 'update_datetime')
    ]

    readonly_fields = ['create_datetime', 'update_datetime']

    inlines = [StudentsInlineTable, TeachersInlineTable]

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['headman'].widget.can_add_related = False
        return form


admin.site.register(Group, GroupAdmin)