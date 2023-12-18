# survey/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .forms import SurveyForm
from .models import SurveyResponse

class SurveyView(View):
    template_name = 'survey/survey.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request):
        form = SurveyForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = SurveyForm(request.POST)
        if form.is_valid():
            ip_address = self.get_client_ip(request)
            if SurveyResponse.objects.filter(ip_address=ip_address).exists():
                return HttpResponseForbidden("You have already submitted a response.")
            response = form.save(commit=False)
            response.ip_address = ip_address
            response.save()
            return HttpResponseForbidden("Your response has been submitted.")
        return render(request, self.template_name, {'form': form})

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip