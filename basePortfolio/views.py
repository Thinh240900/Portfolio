from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


# Create your views here.


class HomePageView(View):
    template_name = 'basePortfolio/home.html'
    def get(self, request):
        return render(request, self.template_name)


def health(request):
    return HttpResponse("Healthy", status=200)