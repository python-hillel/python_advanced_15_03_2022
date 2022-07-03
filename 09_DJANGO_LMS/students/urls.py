from django.urls import path

from .views import ListStudentView
from .views import UpdateStudentView
from .views import create_student
from .views import delete_student

# CRUD - Create, Read, Update, Delete

app_name = 'students'

urlpatterns = [
    path('', ListStudentView.as_view(), name='list'),                              # Read
    path('create/', create_student, name='create'),                   # Create
    path('update/<int:identity>/', UpdateStudentView.as_view(), name='update'),          # Update
    path('delete/<int:pk>/', delete_student, name='delete'),          # Delete
]
