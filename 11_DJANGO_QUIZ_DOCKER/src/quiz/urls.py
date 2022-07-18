from django.urls import path

from .views import ExamDetailView
from .views import ExamListView
from .views import ExamResultCreateView
from .views import ExamResultDetailView
from .views import ExamResultQuestionView
from .views import ExamResultUpdateView

app_name = 'quiz'

urlpatterns = [
    path('', ExamListView.as_view(), name='list'),
    path('<uuid:uuid>/', ExamDetailView.as_view(), name='details'),
    path('<uuid:uuid>/result/create/', ExamResultCreateView.as_view(), name='result_create'),
    path('<uuid:uuid>/result/<uuid:res_uuid>/details/', ExamResultDetailView.as_view(), name='result_details'),
    path('<uuid:uuid>/result/<uuid:res_uuid>/update/', ExamResultUpdateView.as_view(), name='result_update'),
    path('<uuid:uuid>/result/<uuid:res_uuid>/question/next/', ExamResultQuestionView.as_view(), name='question'),
    # path('<uuid:uuid>/result/<uuid:res_uuid>/question/<int:order_num>/', ExamResultQuestionView.as_view(),
    #      name='question'),
]
