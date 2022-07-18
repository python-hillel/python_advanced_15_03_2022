from django.urls import path
from django.views.generic import TemplateView

from .views import AccountLoginView
from .views import AccountLogoutView
# from .views import AccountRegisterDoneView
from .views import AccountRegisterView
from .views import AccountUpdateProfileView
from .views import account_profile_view
from .views import user_activate

app_name = 'accounts'

urlpatterns = [
    path('registration/activate/<str:sign>/', user_activate, name='register_activate'),
    # path('registration/done/', AccountRegisterDoneView.as_view(), name='register_done'),
    path('registration/done/', TemplateView.as_view(template_name='accounts/register_done.html'), name='register_done'),
    path('registration/', AccountRegisterView.as_view(), name='registration'),
    path('login/', AccountLoginView.as_view(), name='login'),
    path('logout/', AccountLogoutView.as_view(), name='logout'),
    path('profile/', account_profile_view, name='profile'),
    path('profile_change/', AccountUpdateProfileView.as_view(), name='profile_change'),
]
