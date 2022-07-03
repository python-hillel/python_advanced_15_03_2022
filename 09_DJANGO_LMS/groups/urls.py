from django.urls import path

from .views import CreateGroupView
from .views import DeleteGroupView
from .views import ListGroupView
from .views import UpdateGroupView

# CRUD - Create, Read, Update, Delete

app_name = 'groups'

urlpatterns = [
    path('', ListGroupView.as_view(), name='list'),                              # Read
    path('create/', CreateGroupView.as_view(), name='create'),                   # Create
    path('update/<int:pk>/', UpdateGroupView.as_view(), name='update'),          # Update
    path('delete/<int:pk>/', DeleteGroupView.as_view(), name='delete'),          # Delete
]
