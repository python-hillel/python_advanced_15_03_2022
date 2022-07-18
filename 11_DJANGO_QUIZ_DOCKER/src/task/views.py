from celery.result import AsyncResult

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .tasks import create_task


def home(request):
    return render(request, "task/home.html")


@csrf_exempt
def run_task(request):
    if request.POST:
        task_type = request.POST.get("type")
        task = create_task.delay(task_type)

        return JsonResponse({"task_id": task.id}, status=202)


@csrf_exempt
def get_status(request, task_id):
    if request.method == 'GET':
        task_result = AsyncResult(task_id)
        result = {
            "task_id": task_id,
            "task_status": task_result.status,
            "task_result": '' if task_result.result is None else str(task_result.result)
        }

        return JsonResponse(result, status=200)
