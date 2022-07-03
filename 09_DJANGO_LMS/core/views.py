from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse


def index(request):
    return render(request, 'index.html')


class UpdateBaseView:
    model = None
    success_url = None
    template_name = None
    form_class = None

    @classmethod
    def update(cls, request, pk):
        model_obj = get_object_or_404(cls.model, pk=pk)

        if request.method == 'POST':
            form = cls.form_class(request.POST, instance=model_obj)
            if form.is_valid():
                form.save()

                return HttpResponseRedirect(reverse(cls.success_url))
        else:
            form = cls.form_class(instance=model_obj)

        return render(request, cls.template_name, {'form': form})
